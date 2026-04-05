def check_missing(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_negative_values(df):
    issues = {}
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        issues[col] = (df[col] < 0).sum()
    return issues