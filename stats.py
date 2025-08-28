
import math

def _clean_values(values):
    filtered = []
    for v in values:
        if math.isnan(v):
            continue
        if v < 0 or v > 200:
            return []
        filtered.append(v)
    return filtered


def calculate_stats(values):
    valid = _clean_values(values)

    if len(valid) == 0:
        return dict(avg=math.nan, min=math.nan, max=math.nan)

    return {
        "avg": sum(valid) / len(valid),
        "min": min(valid),
        "max": max(valid)
    }
