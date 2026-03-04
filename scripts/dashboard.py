import os
import json

BASE = "outputs/accounts"

print("\n==============================")
print(" Clara Agent Pipeline Summary ")
print("==============================\n")

if not os.path.exists(BASE):
    print("No processed accounts found.")
    exit()

accounts = os.listdir(BASE)

print("Accounts processed:", len(accounts))
print("----------------------------------\n")

for account in accounts:

    account_path = os.path.join(BASE, account)
    v2_path = os.path.join(account_path, "v2", "account_memo.json")

    if os.path.exists(v2_path):

        with open(v2_path) as f:
            memo = json.load(f)

        print("Account:", account)
        print("Company:", memo.get("company_name"))
        print("Services:", ", ".join(memo.get("services_supported", [])))
        print("Emergency:", ", ".join(memo.get("emergency_definition", [])))
        print("Business Hours:", memo.get("business_hours"))
        print("----------------------------------")