# Data — SYNTHETIC SAMPLE ONLY

> **Disclosure:** everything under `data/synthetic_sample/` is **synthetically
> generated** by `tools/generate_synthetic_sample.py` (seeded RNG). It contains
> **zero real sensor recordings, zero patient data**, and must not be presented
> as collected data, training data, or clinical evidence.

Purpose: let reviewers exercise the BLE JSON schema, threshold rules, and UI
without hardware.

- `vitals_sample.csv` — 1000 rows, 1 Hz-like synthetic vitals + env + labels.
- `schema.json` — column contract mirroring `docs/ble-contract.md`.

Regenerate:

```bash
python3 tools/generate_synthetic_sample.py --seed 42 --n 1000
python3 tools/validate_dataset.py
```

Label logic (matches `docs/methodology.md` thresholds):

- `heat_stress = temp_body >= 38.5`
- `dehydration = temp_body >= 39.0`
- `alert = SOS > fall > hr>120 > spo2<92 > heat/dehydration > stable`

Do not train or claim an Edge-AI model from this sample.
