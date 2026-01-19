import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ladda datan
df = pd.read_csv('if_insurance_claims.csv')

# 2. Feature Engineering (Gör om datum till siffror modellen förstår)
df['policy_start'] = pd.to_datetime(df['policy_start'])
df['claim_date'] = pd.to_datetime(df['claim_date'])
df['days_to_claim'] = (df['claim_date'] - df['policy_start']).dt.days

# Välj ut relevanta kolumner (Features)
# Vi skippar ID och telefonnummer i själva träningen
features = ['amount', 'days_to_claim']
X = df[features]
y = df['is_fraud']

# Hantera kategorisk data (incident_type)
X = pd.concat([X, pd.get_dummies(df['incident_type'])], axis=1)

# 3. Splitta i träning och test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Träna modellen
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Utvärdera
y_pred = model.predict(X_test)

print("--- MODELLENS PRESTANDA ---")
print(classification_report(y_test, y_pred))

# 6. Visualisera "Feature Importance" (Vad var viktigast för att hitta fusk?)
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(5).plot(kind='barh')
plt.title('Vilka faktorer avslöjar fusket?')
plt.show()
