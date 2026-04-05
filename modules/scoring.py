def calculate_quality_score(missing, duplicates):
    score = 100
    score -= (missing * 0.4)
    score -= (duplicates * 0.3)
    return max(score, 0)