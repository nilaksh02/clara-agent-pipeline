import copy
from utils.schema import ACCOUNT_SCHEMA


def extract_information(transcript, account_id):
    """
    Extract structured information from transcript
    and populate the Account Memo JSON schema.
    """

    memo = copy.deepcopy(ACCOUNT_SCHEMA)
    memo["account_id"] = account_id

    text = transcript.lower()

    # ---------------------------
    # Company Name Detection
    # ---------------------------
    if "electric" in text:
        memo["company_name"] = "Electrical Service Company"

    elif "plumbing" in text or "plumber" in text:
        memo["company_name"] = "Plumbing Service Company"

    elif "hvac" in text or "heating" in text or "air conditioning" in text:
        memo["company_name"] = "HVAC Service Company"

    elif "maintenance" in text or "property maintenance" in text:
        memo["company_name"] = "Property Maintenance Company"

    # ---------------------------
    # Service Detection
    # ---------------------------
    services = []

    if "electrical" in text or "electric" in text:
        services.append("electrical services")

    if "plumbing" in text or "pipe" in text or "drain" in text:
        services.append("plumbing services")

    if "hvac" in text or "heating" in text or "air conditioning" in text:
        services.append("hvac services")

    if "maintenance" in text:
        services.append("maintenance services")

    if "installation" in text:
        services.append("installation services")

    memo["services_supported"] = services

    # ---------------------------
    # Emergency Detection
    # ---------------------------
    emergency_triggers = []

    if "emergency" in text:
        emergency_triggers.append("general emergency")

    if "power outage" in text:
        emergency_triggers.append("power outage")

    if "pipe burst" in text or "flood" in text or "major leak" in text:
        emergency_triggers.append("major plumbing emergency")

    if "heating failure" in text or "ac failure" in text:
        emergency_triggers.append("hvac system failure")

    memo["emergency_definition"] = emergency_triggers

    # ---------------------------
    # Business Hours (empty in demo stage)
    # ---------------------------
    memo["business_hours"] = {
        "days": "",
        "start": "",
        "end": "",
        "timezone": ""
    }

    # ---------------------------
    # Call Transfer Rules
    # ---------------------------
    if "transfer" in text:
        memo["call_transfer_rules"] = {
            "timeout_seconds": 60,
            "retry_count": 1
        }

    # ---------------------------
    # Emergency Routing
    # ---------------------------
    if "technician" in text or "dispatch" in text:
        memo["emergency_routing_rules"] = [
            "Transfer to technician on duty"
        ]

    # ---------------------------
    # After Hours Handling
    # ---------------------------
    if "after hours" in text or "24 hour" in text:
        memo["after_hours_flow_summary"] = (
            "Handle emergency calls and collect caller details immediately."
        )

    # ---------------------------
    # Non Emergency Routing
    # ---------------------------
    if "schedule" in text or "log" in text:
        memo["non_emergency_routing_rules"] = [
            "Log request and schedule during business hours"
        ]

    # ---------------------------
    # Missing Fields Handling
    # ---------------------------
    if memo["business_hours"]["days"] == "":
        memo["questions_or_unknowns"].append("business hours not specified")

    if memo["company_name"] == "":
        memo["questions_or_unknowns"].append("company name not detected")

    memo["notes"] = "Information extracted from demo transcript"

    return memo