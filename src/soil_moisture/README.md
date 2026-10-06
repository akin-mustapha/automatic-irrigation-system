# README

```sh
python3 -m src.soil_moisture.gateway
```

## Cron JOb Setup

```sh
crontab -e

```

```txt
0 */2 * * * /Users/kunmi/workspace/projects/engineering/repository/automatic-irrigation-system/venv/bin/python3 /Users/kunmi/workspace/projects/engineering/repository/automatic-irrigation-system/src/soil_moisture/log_sensor_data.py >> /Users/kunmi/workspace/projects/engineering/repository/automatic-irrigation-system/log_sensor_data.log 2>&1
```
