# AarogyaSync — Personal Health Companion (Public Docs Release)

Privacy-preserving wearable + mobile companion for real-time health monitoring and early warning.
Smart India Hackathon 2026 — Problem Statement 26181 (Qualcomm, MedTech/HealthTech).

> **What this repo is:** public, docs-only release. It describes system design,
> BLE contract, methodology, and a clearly-labeled **synthetic sample dataset**
> for API/UI development. It does **not** contain the private firmware/app source,
> real user data, or clinical models.
>
> **What this repo is not:** no collected patient data, no trained Edge-AI weights,
> no clinical validation. Threshold-based on-device alerts only — see
> `docs/limitations-and-roadmap.md`.

## Contents

| Path | Description |
|---|---|
| `docs/methodology.md` | Sensing → inference (thresholds) → alert → SOS pipeline |
| `docs/architecture.md` | Hardware + app + BLE data flow |
| `docs/ble-contract.md` | NUS UUIDs, JSON schemas, firmware-ID gating |
| `docs/hardware-overview.md` | Parts, I2C topology, power/safety notes (no firmware source) |
| `docs/app-overview.md` | Screens, SOS flow, permissions, local-first storage |
| `docs/limitations-and-roadmap.md` | Honest gaps + path to Edge-AI |
| `docs/build-and-release.md` | How real `firmware.bin` + APK releases are produced |
| `data/` | Synthetic sample only — see `data/README.md` |
| `tools/generate_synthetic_sample.py` | Deterministic generator for the sample |
| `.github/workflows/` | CI validates docs + dataset; release attaches docs + sample |

## Quick links

- BLE contract: [`docs/ble-contract.md`](docs/ble-contract.md)
- Synthetic sample: [`data/README.md`](data/README.md)
- Roadmap: [`docs/limitations-and-roadmap.md`](docs/limitations-and-roadmap.md)

## Releases

GitHub Releases on tags `v*` attach:

- `docs-bundle.zip` (all markdown in this repo)
- `vitals_sample.csv` + `schema.json` from `data/synthetic_sample/`

Real `firmware.bin` (ESP32-S3) and `app-debug.apk` / `app-release.apk` are **only**
attached when built from versioned source via the workflow in
`docs/build-and-release.md`. This docs-only repo never commits opaque binaries.

## Status

Prototype v1.0.0 (Sept 2026). Local-first, offline-capable, threshold alerts +
manual/auto SOS with SMS + GPS link. No ML model shipped.

## License

MIT — see [LICENSE](LICENSE).
