import json
import os


def generate_agent(account, version="v1"):

    memo_path = f"outputs/accounts/{account}/{version}/account_memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    prompt = f"""
You are Clara, a professional AI call answering assistant for {memo['company_name']}.

BUSINESS HOURS FLOW
1. Greet the caller politely.
2. Ask the purpose of the call.
3. Collect caller name and phone number.
4. Determine if the issue is emergency or non-emergency.
5. Transfer call to the appropriate technician.
6. If transfer fails, apologize and inform the caller a dispatcher will call back.
7. Ask if they need anything else.
8. Close the call politely.

AFTER HOURS FLOW
1. Greet the caller.
2. Ask the purpose of the call.
3. Confirm whether it is an emergency.
4. If emergency:
   - collect name
   - phone number
   - service address
5. Attempt transfer to emergency contact.
6. If transfer fails reassure the caller a technician will follow up shortly.
7. Ask if they need anything else.
8. Close politely.
"""

    agent = {
        "agent_name": f"{memo['company_name']} Clara Agent",
        "voice_style": "professional calm",
        "version": version,
        "system_prompt": prompt,
        "variables": {
            "timezone": memo["business_hours"]["timezone"],
            "business_hours": memo["business_hours"],
            "services": memo["services_supported"]
        },
        "call_transfer_protocol": "Transfer emergency calls immediately to technician.",
        "fallback_protocol": "If transfer fails after 60 seconds, log callback and reassure caller."
    }

    path = f"outputs/accounts/{account}/{version}"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)