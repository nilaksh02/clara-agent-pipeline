import json
import os


def update(account):

    v1_path = f"outputs/accounts/{account}/v1/account_memo.json"

    with open(v1_path) as f:
        memo = json.load(f)

    onboarding_file = f"dataset/{account}/onboarding.txt"

    if os.path.exists(onboarding_file):

        with open(onboarding_file) as f:
            onboarding_text = f.read().lower()

        # --- Business Hours Confirmation ---
        if "business hours" in onboarding_text or "monday" in onboarding_text:
            memo["business_hours"] = {
                "days": "Mon-Fri",
                "start": "08:00",
                "end": "17:00",
                "timezone": "EST"
            }

        # --- Emergency Routing Confirmation ---
        if "emergency" in onboarding_text or "technician" in onboarding_text:
            memo["emergency_routing_rules"] = [
                "Transfer emergency calls to technician on duty"
            ]

        # --- Non Emergency Handling ---
        if "schedule" in onboarding_text or "log" in onboarding_text:
            memo["non_emergency_routing_rules"] = [
                "Log request and schedule during business hours"
            ]

        memo["notes"] = "Updated using onboarding transcript"

    # --- Save v2 output ---
    output = f"outputs/accounts/{account}/v2"
    os.makedirs(output, exist_ok=True)

    with open(f"{output}/account_memo.json", "w") as f:
        json.dump(memo, f, indent=2)