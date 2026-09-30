# BLE Contract (NUS)

## UUIDs

| Role | UUID | Direction |
|---|---|---|
| NUS Service | `6E400001-B5A3-F393-E0A9-E50E24DCCA9E` | — |
| TX (Notify) | `6E400002-B5A3-F393-E0A9-E50E24DCCA9E` | Watch → Phone |
| RX (Write) | `6E400003-B5A3-F393-E0A9-E50E24DCCA9E` | Phone → Watch |
| Firmware ID (Read) | `0000FF01-0000-1000-8000-00805f9b34fb` | Phone reads, must be `AROGYA_SYNC_V1` |

MTU up to 512 requested. Advertising name prefix `AROGYA_`.

## Watch → Phone (example, v1 schema)

```json
{
  "hr": 72,
  "spo2": 97,
  "temp_body": 36.6,
  "steps": 8432,
  "sleep_stage": "awake",
  "env_temp": 28.0,
  "humidity": 55.0,
  "pressure": 1013.0,
  "air_quality": 42,
  "battery": 85,
  "calories": 337,
  "sensors": {"tmp117": true, "lsm6dso": true, "bme680": true, "max30102": true},
  "alerts": {
    "heat_stress": {"flag": false, "score": 0.0},
    "dehydration": {"flag": false},
    "resp_distress": {"flag": false},
    "fall_detected": false
  },
  "emergency": {"sos": false}
}
```

Notes:

- `sleep_stage` is reserved; v1.0 always sends `"awake"`.
- `resp_distress.flag` is reserved; v1.0 always `false`.
- `air_quality` is a coarse 0–100 band from gas resistance, not certified IAQ.

## Phone → Watch (example)

```json
{
  "config": {"hr_max": 120, "hr_min": 50, "spo2_min": 92, "temp_max": 38.5, "aqi_max": 100},
  "preferences": {"alert_sensitivity": "high", "notify_mode": "vibration", "sync_interval": 30},
  "commands": {"sos": false, "reset_alerts": false, "fall_detection": true},
  "time_sync": {"epoch": 1789016644, "tz_offset": 19800},
  "user_profile": {"name": "", "age": 0, "height": 170.0, "weight": 65.0}
}
```

## Versioning

Any schema break requires bumping the firmware ID (e.g. `AROGYA_SYNC_V2`) and
updating `data/schema.json` in this repo.
