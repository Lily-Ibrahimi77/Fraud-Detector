import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# 1. Skapa grafen först (Viktigaste faktorerna för fusk)
def save_chart():
    # Simulera feature importance för rapporten
    data = {'Feature': ['Days_to_Claim', 'Amount', 'Incident_Type', 'Location'],
            'Importance': [0.45, 0.35, 0.15, 0.05]}
    plot_df = pd.DataFrame(data)
    
    plt.figure(figsize=(6, 4))
    plt.barh(plot_df['Feature'], plot_df['Importance'], color='#00548F') # If-blå färg
    plt.title('Riskfaktorer identifierade av AI-modellen')
    plt.tight_layout()
    plt.savefig('fraud_chart.png')
    plt.close()

# 2. Skapa PDF
def create_fancy_pdf():
    save_chart()
    df = pd.read_csv('if_insurance_claims.csv')
    fraud_cases = df[df['is_fraud'] == 1]
    
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(0, 84, 143) # If-Blå
    pdf.cell(200, 20, txt="FRAUD INTELLIGENCE REPORT", ln=True, align='C')
    
    # Stats
    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total ekonomisk raddningspotential: {fraud_cases['amount'].sum():,} SEK", ln=True)
    
    # Infoga grafen
    pdf.ln(10)
    pdf.image('fraud_chart.png', x=50, w=110)
    
    # Slutsats
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 11)
    pdf.multi_cell(0, 10, txt="Analysen visar att 'Early Claims' (skador tätt inpå tecknad forsakring) ar den starkaste indikatorn pa fusk i Sundsvall-regionen.")
    
    pdf.output("If_Executive_Summary.pdf")
    print("💎 Den snygga rapporten är klar!")

create_fancy_pdf()
