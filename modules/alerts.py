def generate_alerts(missing, duplicates, impact):
    alerts = []

    if impact > 100000:
        alerts.append(("HIGH", f"High revenue impact: ₹{impact}"))

    if missing > 0:
        alerts.append(("MEDIUM", f"Missing values: {missing}"))

    if duplicates > 0:
        alerts.append(("LOW", f"Duplicate records: {duplicates}"))

    return alerts