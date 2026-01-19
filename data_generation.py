import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('sv_SE')
data = []

# Skapa 1000 rader
for i in range(5000):
    policy_start = fake.date_between(start_date='-2y', end_date='today')
    # Normalt sett sker skadan efter ett tag
    claim_date = policy_start + timedelta(days=random.randint(1, 365))
    amount = random.randint(2000, 45000)
    phone = fake.phone_number()
    is_fraud = 0
    
    # --- INJICERA FUSK-MÖNSTER ---
    rand = random.random()
    if rand < 0.02: # 2% "Burn-in" fusk (skada direkt efter start)
        claim_date = policy_start + timedelta(days=random.randint(0, 3))
        is_fraud = 1
    elif rand < 0.04: # 2% Outliers (extremt höga belopp)
        amount = random.randint(150000, 500000)
        is_fraud = 1
    
    data.append([
        f"CLM-{1000+i}", f"POL-{5000+i}", policy_start, claim_date, 
        amount, random.choice(['Vattenskada', 'Inbrott', 'Bilolycka', 'Glasskada']),
        phone, is_fraud
    ])

df = pd.DataFrame(data, columns=[
    'claim_id', 'policy_id', 'policy_start', 'claim_date', 
    'amount', 'incident_type', 'phone_number', 'is_fraud'
])

# Injicera "Frequent Flyer" (samma nummer på flera claims)
for _ in range(5):
    suspicious_phone = "070-123 45 67"
    df.loc[random.randint(0, 999), ['phone_number', 'is_fraud']] = [suspicious_phone, 1]

df.to_csv('if_insurance_claims.csv', index=False)
print("Dataset skapat: if_insurance_claims.csv")
