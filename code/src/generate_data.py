import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Define industry codes, risk ratings, and credit types
industry_codes = ['FIN', 'TECH', 'MANUF', 'HEALTH', 'EDU', 'TRANSPORT']
credit_facility_types = ['Revolving Credit', 'Term Loan', 'Bridge Loan', 'Syndicated Loan']
risk_ratings = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'C', 'D']
flagged_reasons = ["AML Violation", "Over-leverage", "High FX Risk", "Liquidity Concern", "Credit Utilization High"]
remediation_actions = ["Increase Collateral", "Enhanced Due Diligence", "Regulatory Compliance Check", "Credit Risk Review"]

def generate_corporate_loan_data(num_rows=10000):
    data = []
    for _ in range(num_rows):
        customer_id = fake.uuid4()
        industry = random.choice(industry_codes)
        risk_rating = random.choice(risk_ratings)
        loan_amount = random.randint(50000, 10000000)
        outstanding_balance = random.randint(10000, loan_amount)
        origination_date = fake.date_between(start_date="-5y", end_date="today")
        maturity_date = fake.date_between(start_date="today", end_date="+10y")
        credit_type = random.choice(credit_facility_types)

        # Risk & Compliance Features
        aml_flag = random.choices([0, 1], weights=[90, 10])[0]  # 10% flagged
        fraud_score = random.randint(0, 10)
        kyc_score = random.randint(50, 100)
        sanctions_flag = random.choices([0, 1], weights=[95, 5])[0]
        exposure_breached = random.choices([0, 1], weights=[85, 15])[0]

        # AI Labels
        flagged_status = random.choices([0, 1, 2], weights=[70, 20, 10])[0]
        flagged_reason = random.choice(flagged_reasons) if flagged_status > 0 else "None"
        remediation_action = random.choice(remediation_actions) if flagged_status > 0 else "None"

        data.append([
            customer_id, industry, risk_rating, loan_amount, outstanding_balance,
            origination_date, maturity_date, credit_type, aml_flag, fraud_score,
            kyc_score, sanctions_flag, exposure_breached, flagged_status, flagged_reason, remediation_action
        ])

    return pd.DataFrame(data, columns=[
        "CustomerID", "IndustryCode", "InternalRating", "LoanAmount", "OutstandingBalance",
        "OriginationDate", "MaturityDate", "CreditFacilityType", "AML_Flag", "FraudRiskScore",
        "KYC_ComplianceScore", "SanctionsCheckFlag", "ExposureLimitBreached", "AI_Label", "FlaggedReason", "RemediationAction"
    ])

# Generate dataset
df = generate_corporate_loan_data(10000)

# Save file for Kaggle

df.to_csv(r'C:\Anu\hackathon\corporate_loan_ai_data.csv', index=False)
