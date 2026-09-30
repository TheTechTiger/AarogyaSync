# Methodology

Problem Statement 26181 asks for a privacy-preserving, on-device health companion:
continuous vitals + environment sensing, anomaly detection, disaster-aware alerts,
offline operation, SOS.

## 1. Sensing (watch)

- Body: heart rate (PPG peak detection), SpO2 (ratio-of-ratios), body temperature
  (digital sensor), steps/calories (IMU actigraphy).
- Environment: ambient temperature, humidity, pressure, gas resistance → coarse
  air-quality band.
- Motion: 6-axis IMU with hardware free-fall / wake / tap interrupts for fall
  detection.
- Sampling: ~100 ms sensor tick, ~1 Hz BLE notify to phone. Touch display for
  local vitals view + haptics.

## 2. Inference — threshold rules (v1.0, no ML)

Current public behavior is **deterministic thresholds**, not a trained model:

- `heat_stress = body_temp >= cfg.temp_max` (default 38.5 °C)
- `dehydration = body_temp >= cfg.temp_max + 0.5`
- `heat_score = clamp((T - (max-1)) / 1.5, 0..1)`
- Phone-side display status: SOS > fall > `hr > 120` > `spo2 < 92` > stable.
- `resp_distress` and `sleep_stage` are **not computed** in v1.0 (reserved fields).

Why thresholds first: deterministic on MCU, auditable for a hackathon, no training
data or TFLite-Micro dependency. See `limitations-and-roadmap.md` for the planned
migration to a tiny quantized anomaly model.

## 3. Communication (BLE NUS)

Watch is NUS peripheral, phone is central. Full contract in `ble-contract.md`.
Phone rejects devices whose firmware-ID characteristic ≠ `AROGYA_SYNC_V1`.
No cloud transport in v1.0 — Room + DataStore on phone only.

## 4. Alerting + SOS

- Watch: vibration + screen status on fall / heat / SOS command.
- Phone: alert list sorted by severity; SMS with vitals + Google Maps link to
  user-configured emergency contacts; GPS via Fused Location Provider with
  "Location: Unavailable" fallback.
- No auto-dial, no background foreground-service in this docs release.

## 5. Privacy

- No `INTERNET` permission required for core monitoring in v1.0.
- Health packets stay on BLE + local DB. Cloud-sync toggle exists in design but
  performs no upload in v1.0.
- Synthetic sample in `data/` is randomly generated — contains zero real user data.

## 6. Evaluation notes

Reproducible without hardware:

1. Read `ble-contract.md`.
2. Run `python3 tools/generate_synthetic_sample.py --seed 42 --n 1000`.
3. Validate with `python3 tools/validate_dataset.py`.
4. Feed rows through the documented threshold rules to reproduce alert labels.
