from typing import Dict

def compute_bmi(weight_kg: float, height_cm: float) -> float:
    """Return BMI rounded to one decimal place."""
    if height_cm <= 0: raise ValueError("height must be positive")
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m * height_m)
    return round(bmi, 1)

def fever_severity(temp_c: float) -> str:
    """
    Simple heuristic tool for fever severity.
    """
    if temp_c >= 40.0:
        return "high"
    if temp_c >= 38.0:
        return "moderate"
    if temp_c >= 37.5:
        return "low"
    return "none"
