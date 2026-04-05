def revenue_loss_due_to_missing(df):
    if 'Sales' in df.columns:
        missing_count = df['Sales'].isnull().sum()
        avg_sales = df['Sales'].mean()
        return missing_count * avg_sales
    return 0