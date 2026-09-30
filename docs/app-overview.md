# App Overview (no app source in this repo)

- Stack: Kotlin, Jetpack Compose + Material 3, MVVM + Repository, Room + DataStore,
  Kotlinx Serialization, Play-Services Location.
- Screens: Home (vitals), Alerts (severity-sorted), Trends (weekly scaffold),
  Ask (assistant placeholder), Profile, Emergency Contacts, Pair Device, Settings.
- Pairing: scan `AROGYA_` prefix → GATT → read firmware ID → accept only
  `AROGYA_SYNC_V1`.
- SOS: manual button + auto on `sos`/`fall_detected`; SMS via `SmsManager` with
  `HR/SpO2/Temp` snapshot + Maps link; contacts stored in Room.
- Permissions: Bluetooth scan/connect, location (BLE + SOS), SMS, camera/gallery
  (avatar). Core monitoring needs no internet.
- Local-first: no vitals-history table in v1.0; trends/daily-summary are UI
  scaffolds pending the roadmap in `limitations-and-roadmap.md`.
