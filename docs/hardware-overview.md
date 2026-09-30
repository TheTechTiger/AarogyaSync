# Hardware Overview (no firmware source in this repo)

| Component | Part | Interface |
|---|---|---|
| MCU | ESP32-S3 (dual-core, PSRAM) | — |
| Display | ST7789 320×172 landscape, touch | SPI DMA + I2C touch |
| Body temp | Digital temp sensor | I2C 0x48 |
| IMU | 6-axis accel/gyro | I2C |
| Environment | Temp/humidity/pressure/gas | I2C |
| PPG | Red/IR pulse sensor | I2C |
| Haptics | Vibration motor | GPIO out |

All sensors share one I2C bus; motion/temp/PPG use GPIO interrupt lines for
fall, threshold, and data-ready events. 16 MB flash with dual-OTA slots in
production firmware (not included here).

Safety notes: wearable prototype only — no medical certification, no sealed
enclosure rating, battery fuel-gauge is approximate. Do not use for diagnosis.
