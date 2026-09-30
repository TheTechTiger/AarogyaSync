# Release notes template

## AarogyaSync vX.Y.Z — <date>

- Docs bundle + synthetic sample attached (SHA-256 in SHA256SUMS.txt).
- Firmware / app builds (only if promoted from audited source):
  - `firmware.bin` — built via `pio run -e esp32s3_touch_147`, SHA256: `<hex>`
  - `app-debug.apk` / `app-release.apk` — built via `./gradlew assemble*`, SHA256: `<hex>`
  - Source commit: `<repo>@<sha>`
- If firmware/APK absent: no source build was promoted for this tag. Nothing forged.
- Sample data is SYNTHETIC (seed 42) — not collected, not clinical.
