@echo off
echo 🚀 STARTING IF RISK-INTELLIGENCE PIPELINE...

:: 1. Aktivera venv
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

:: 2. Generera Data
echo 📊 Generating synthetic insurance data...
python data_generation.py

:: 3. Träna modell & analysera fusk
echo 🤖 Training AI model...
python model_training.py

:: 4. Generera PDF
echo 📄 Generating executive report and sending email...
python final_report.py

:: 5. Skicka E-post
echo 📄 sending email...
python 3_mail_sender.py

echo ✅ PIPELINE COMPLETE! Check your inbox, Lily.
pause
