import os
import pandas as pd
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

def send_dynamic_report():
    # 1. Hämta data dynamiskt från den senaste körningen
    df = pd.read_csv('if_insurance_claims.csv')
    fraud_cases = df[df['is_fraud'] == 1]
    
    num_cases = len(fraud_cases)
    total_risk = fraud_cases['amount'].sum()
    
    # 2. Setup för e-post (från din .env)
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    DESTINATION = "z.ibrahimi1996@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = f'🚨 Risk-analys slutförd: {num_cases} avvikelser identifierade'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = DESTINATION

    # 3. Det dynamiska meddelandet
    msg.set_content(f"""Hej Lily,

Den automatiserade granskningen av inkomna skadeärenden är nu slutförd.

Analysen har identifierat {num_cases} högriskärenden som kräver omedelbar uppföljning. 
Det sammanlagda exponerade värdet för dessa ärenden uppgår till {total_risk:,.0f} SEK.

Se bifogad rapport (PDF) för en detaljerad sammanställning av riskfaktorer och prioriteringsordning.

Med vänlig hälsning,
LILY (Risk Intelligence System)""")

    # 4. Bifoga PDF
    try:
        with open('If_Executive_Summary.pdf', 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename='If_Executive_Summary.pdf')
        
        # 5. Skicka
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Dynamiskt mail skickat! (Värde: {total_risk:,.0f} SEK)")
    except Exception as e:
        print(f"❌ Fel vid utskick: {e}")

# Kör funktionen sist i ditt script
send_dynamic_report()
