# Build and Release (how real binaries are produced)

This docs-only repo **does not vendor** `firmware.bin` or APKs. Releases attach
only docs + synthetic sample. Real binaries are produced as follows and their
SHA-256 published in release notes:

## Firmware (ESP32-S3, private source)

```bash
pio run -e esp32s3_touch_147
# output: .pio/build/esp32s3_touch_147/firmware.bin
sha256sum .pio/build/esp32s3_touch_147/firmware.bin
pio run --target upload
pio device monitor --baud 115200
```

Requirements: PlatformIO 6.x, USB, ESP32-S3 board. Dual-OTA partition layout
documented in `hardware-overview.md`.

## App (private source)

```bash
./gradlew assembleDebug
# output: app/build/outputs/apk/debug/app-debug.apk
./gradlew assembleRelease
adb install app/build/outputs/apk/debug/app-debug.apk
```

Requirements: Android Studio Hedgehog+, JDK 17, SDK 34, physical BLE-capable device.

## GitHub Release process

1. Tag `vX.Y.Z` on the source repo that contains the built commit.
2. CI builds both artifacts from clean checkout (see `.github/workflows/release.yml`
   template in this repo for the docs/sample job).
3. Attach `firmware.bin`, `app-*.apk`, `vitals_sample.csv`, `docs-bundle.zip`
   plus `SHA256SUMS.txt`.
4. Never commit opaque `.bin`/`.apk` to git history — Releases only.

If a Release in this docs repo lacks `firmware.bin`/APK, that means no audited
source build was promoted — nothing is forged to fill the gap.
