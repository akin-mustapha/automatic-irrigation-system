"""
Script reads a single soil moisture data point from a serial port,
sends it to AWS DynamoDB, closes the serial connection, and exits.
Designed to be triggered periodically via cron.
"""

import logging
import time
from datetime import datetime, timezone
from uuid import uuid4
import serial
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
table = dynamodb.Table("plant_sensor_data")


def get_serial_connection():
    """
    Establishes a serial connection to the Arduino.
    Returns the serial connection object or None.
    """
    port = "/dev/cu.usbmodem11101"  # Update with your serial port
    baud_rate = 9600
    timeout = 1  # Timeout in seconds

    try:
        ser = serial.Serial(port, baud_rate, timeout=timeout)
        logger.info(f"Connected to serial port: {port} at {baud_rate} baud.")
        return ser
    except serial.SerialException as e:
        logger.error(f"Error connecting to serial port: {e}")
        return None


def save_to_dynamodb(sensor_value):
    sensor_name = "soil_moisture"
    uuid = str(uuid4())
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    table.put_item(
        Item={
            "id": uuid,
            "timestamp": timestamp,
            "sensor": sensor_name,
            "value": sensor_value,
        }
    )
    logger.info(f"Data sent to DynamoDB: {sensor_value} at {timestamp}")


def main():
    ser = get_serial_connection()

    if ser is None:
        logger.error("Failed to establish serial connection. Exiting.")
        return

    # Wait up to 15 seconds for a valid reading from Arduino
    timeout_seconds = 15
    start_time = time.time()
    reading_saved = False

    try:
        # Flush old serial data in buffer so we get fresh data
        ser.reset_input_buffer()

        while time.time() - start_time < timeout_seconds:
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8", errors="ignore").rstrip()

                if line.startswith("Sensor Value:"):
                    try:
                        sensor_value = int(line.split(":")[1].strip())
                        save_to_dynamodb(sensor_value)
                        reading_saved = True
                        break  # Got reading, exit loop
                    except ValueError as ve:
                        logger.error(
                            f"Could not parse sensor value from '{line}': {ve}"
                        )

            time.sleep(0.1)

        if not reading_saved:
            logger.warning(
                f"No valid sensor reading received within {timeout_seconds} seconds."
            )

    finally:
        # ALWAYS close the serial port before exiting so cron can run it next time
        ser.close()
        logger.info("Serial port closed.")


if __name__ == "__main__":
    main()
