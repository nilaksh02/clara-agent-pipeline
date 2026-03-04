import json
import os


def generate_diff(account):

    print("Running diff generator...")

    v1_path = f"outputs/accounts/{account}/v1/account_memo.json"
    v2_path = f"outputs/accounts/{account}/v2/account_memo.json"

    print("Checking files:")
    print(v1_path)
    print(v2_path)

    if not os.path.exists(v1_path):
        print("ERROR: v1 memo not found")
        return

    if not os.path.exists(v2_path):
        print("ERROR: v2 memo not found")
        return

    with open(v1_path) as f:
        v1 = json.load(f)

    with open(v2_path) as f:
        v2 = json.load(f)

    changes = {}

    for key in v2:
        if v2[key] != v1.get(key):
            changes[key] = {
                "before": v1.get(key),
                "after": v2[key]
            }

    # Save JSON diff
    json_path = f"outputs/accounts/{account}/changes.json"

    with open(json_path, "w") as f:
        json.dump(changes, f, indent=2)

    print("JSON changelog saved at:", json_path)

    # Create human readable markdown changelog
    md_path = f"outputs/accounts/{account}/changes.md"

    with open(md_path, "w") as md:

        md.write("# Change Summary\n\n")
        md.write(f"Account: {account}\n\n")

        if not changes:
            md.write("No changes detected between v1 and v2.\n")

        for key, value in changes.items():

            md.write(f"Field Updated: {key}\n\n")

            md.write("Before:\n")
            md.write(f"{value['before']}\n\n")

            md.write("After:\n")
            md.write(f"{value['after']}\n\n")

            md.write("Reason:\n")
            md.write("Information confirmed during onboarding call.\n\n")

            md.write("---\n\n")

    print("Markdown changelog saved at:", md_path)