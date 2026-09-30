#!/usr/bin/env python3
"""Validate synthetic sample against thresholds. Fails on inconsistency."""
import csv, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "synthetic_sample" / "vitals_sample.csv"
def label(r):
    if r["sos"] == "1": return "sos"
    if r["fall_detected"] == "1": return "fall"
    if int(r["hr"]) > 120: return "high_hr"
    if int(r["spo2"]) < 92: return "low_spo2"
    if r["dehydration"] == "1": return "dehydration"
    if r["heat_stress"] == "1": return "heat_stress"
    return "stable"
rows = list(csv.DictReader(open(P)))
assert len(rows) > 0, "empty sample"
bad = [(i, r["label"], label(r)) for i, r in enumerate(rows) if r["label"] != label(r)]
if bad:
    print(f"FAIL: {len(bad)} label mismatches, e.g. {bad[:3]}"); sys.exit(1)
print(f"OK: {len(rows)} synthetic rows consistent. SYNTHETIC ONLY — not real data.")
