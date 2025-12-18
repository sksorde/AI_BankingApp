
def summarize_transactions(df):
    debits = df[df["type"]=="Debit"]["amount"].sum()
    credits = df[df["type"]=="Credit"]["amount"].sum()
    return f"You spent {abs(debits)} rupees and received {credits} rupees this month."
