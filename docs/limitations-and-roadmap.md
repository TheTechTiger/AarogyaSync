# Limitations and Roadmap (honest)

v1.0 is a functional prototype, not PS-complete. Major gaps:

1. **No ML model.** Anomaly detection is fixed thresholds. No TFLite/ONNX,
   no training, no risk scores. `resp_distress` never fires; `sleep_stage`
   is constant.
2. **No disaster feed.** No heat-wave/AQI/flood/cyclone integration, no
   background worker, no push.
3. **No baselines/trends.** No vitals-history table; Trends screen is empty;
   BP shown in some builds is a placeholder.
4. **Environment unused on phone.** Env fields are transported but not displayed
   or assessed in v1.0.
5. **Single-target scale.** One watch design, one phone role; no Wear OS, no
   fleet/backend.

## Roadmap

- P0: Room `VitalSample` history → 7-day baseline → phone-side risk engine
  (documented thresholds first, then tiny quantized model with training script
  and eval metrics committed alongside weights).
- P1: Disaster cache (Open-Meteo, offline Room cache, periodic worker) +
  environment UI + IMU actigraphy sleep staging.
- P2: Real trends/daily summary, SOS foreground service, provider CSV export,
  README de-overclaiming, CI + device-in-the-loop BLE test.

Out of scope for hackathon: clinical validation, multi-device fleet,
regulatory (HIPAA/DPDP) certification.
