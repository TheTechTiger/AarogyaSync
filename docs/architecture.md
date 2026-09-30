# Architecture

```mermaid
flowchart LR
    subgraph Watch["ESP32-S3 Watch"]
        S[Sensors: PPG + Temp + IMU + Env] --> FW[Firmware tick 100ms]
        FW --> UI[Touch display + haptics]
        FW -->|NUS notify 1Hz| BLEA[BLE NUS TX]
        BLEB[BLE NUS RX] --> FW
    end
    subgraph Phone["Android App"]
        BLEM[BLE Central] --> REPO[Repository + threshold mapping]
        REPO --> VM[ViewModels]
        VM --> UI2[Compose dashboards]
        VM --> SMS[SMS + GPS SOS]
        REPO --> DB[(Room + DataStore)]
    end
    BLEA -->|JSON vitals| BLEM
    BLEM -->|JSON config| BLEB
```

## Data flow

1. Watch reads sensors, derives HR/SpO2/steps/alerts, updates display.
2. Watch notifies JSON vitals packet at ~1 Hz.
3. Phone decodes, maps to UI state, persists profile/contacts/settings locally.
4. Phone writes back config (thresholds, prefs, time sync, user profile).
5. On SOS/fall, phone sends SMS with snapshot + location link.

No server, no MQTT, no FCM in v1.0.
