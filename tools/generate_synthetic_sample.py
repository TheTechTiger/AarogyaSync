#!/usr/bin/env python3
"""Deterministic SYNTHETIC vitals generator. Not real data. Seed fixed for repro."""
import argparse, csv, random
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "synthetic_sample" / "vitals_sample.csv"

def gen(seed: int, n: int):
    rng = random.Random(seed)
    rows = []
    steps = 8000
    t = 0
    for i in range(n):
        t += 1
        hr = int(rng.gauss(74, 8))
        spo2 = int(rng.gauss(97, 1.2))
        temp = round(rng.gauss(36.7, 0.4), 1)
        # inject rare events so labels exercise all branches
        r = rng.random()
        fall = sos = False
        if r < 0.005:
            fall = True; hr = rng.randint(110, 135)
        elif r < 0.008:
            sos = True
        elif r < 0.03:
            temp = round(rng.uniform(38.6, 39.4), 1); hr = rng.randint(105, 125)
        elif r < 0.05:
            spo2 = rng.randint(88, 91)
        hr = max(40, min(200, hr)); spo2 = max(70, min(100, spo2))
        steps += rng.randint(0, 3)
        heat = temp >= 38.5
        dehy = temp >= 39.0
        if sos: label = "sos"
        elif fall: label = "fall"
        elif hr > 120: label = "high_hr"
        elif spo2 < 92: label = "low_spo2"
        elif dehy: label = "dehydration"
        elif heat: label = "heat_stress"
        else: label = "stable"
        rows.append([i, hr, spo2, temp, steps,
                      round(rng.gauss(28, 3), 1), round(rng.gauss(55, 10), 1),
                      round(rng.gauss(1013, 5), 1), rng.randint(20, 90),
                      max(5, 87 - i // 200),
                      int(fall), int(sos), int(heat), int(dehy), label])
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n", type=int, default=1000)
    a = ap.parse_args()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = gen(a.seed, a.n)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ts", "hr", "spo2", "temp_body", "steps_cum", "env_temp",
                    "humidity", "pressure", "air_quality", "battery",
                    "fall_detected", "sos", "heat_stress", "dehydration", "label"])
        w.writerows(rows)
    print(f"wrote {OUT} ({len(rows)} rows, seed={a.seed}) SYNTHETIC ONLY")

if __name__ == "__main__":
    main()
