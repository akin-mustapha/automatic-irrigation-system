"""
Script reads soil moisture data from a serial port and sends it to an AWS dynamodb table.
"""

import logging
from datetime import datetime, timezone
from uuid import uuid4
import serial
import time
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
table = dynamodb.Table("plant_sensor_data")


def get_serial_connection():
    """
    Establishes a serial connection to the Arduino.
    Returns the serial connection object.
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
        time.sleep(2)
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

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").rstrip()

            if line.startswith("Sensor Value:"):
                sensor_value = int(line.split(":")[1].strip())
                save_to_dynamodb(sensor_value)


if __name__ == "__main__":
    main()
