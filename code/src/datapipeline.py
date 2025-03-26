import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load generated dataset
df = pd.read_csv("C:\Anu\hackathon\corporate_loan_ai_data.csv")

# Encode categorical features
label_encoders = {}
for col in ["IndustryCode", "InternalRating", "CreditFacilityType", "FlaggedReason", "RemediationAction"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features and target
X = df.drop(columns=["CustomerID", "AI_Label"])
y = df["AI_Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save preprocessed data
X_train.to_csv(r'C:\Anu\hackathon\X_train.csv', index=False)
X_test.to_csv(r'C:\Anu\hackathon\X_test.csv', index=False)
y_train.to_csv(r'C:\Anu\hackathon\y_train.csv', index=False)
y_test.to_csv(r'C:\Anu\hackathon\y_test.csv', index=False)
print("hehe done")