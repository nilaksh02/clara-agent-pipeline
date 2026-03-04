import os

from scripts.extract_demo import run
from scripts.generate_agent import generate_agent
from scripts.apply_onboarding import update
from scripts.diff_generator import generate_diff


DATASET_DIR = "dataset"
LOG_DIR = "logs"


def pipeline():
    """
    Main orchestration pipeline.

    Flow:
    Demo Transcript → Account Memo v1 → Agent Spec v1
    Onboarding Transcript → Account Memo v2 → Agent Spec v2
    → Generate Change Log
    """

    if not os.path.exists(DATASET_DIR):
        print("Dataset folder not found.")
        return

    accounts = os.listdir(DATASET_DIR)

    if not accounts:
        print("No accounts found in dataset.")
        return

    os.makedirs(LOG_DIR, exist_ok=True)

    print("\nStarting Clara Agent Automation Pipeline\n")

    for account in accounts:

        account_path = os.path.join(DATASET_DIR, account)

        if not os.path.isdir(account_path):
            continue

        print(f"Processing account: {account}")

        # log start
        with open(f"{LOG_DIR}/pipeline.log", "a") as log:
            log.write(f"Starting pipeline for account: {account}\n")

        # Step 1 — Extract data from demo call
        print("  → Extracting demo transcript information")
        run(account)

        # Step 2 — Generate preliminary agent configuration (v1)
        print("  → Generating Retell agent configuration v1")
        generate_agent(account, "v1")

        # Step 3 — Apply onboarding updates
        print("  → Applying onboarding updates")
        update(account)

        # Step 4 — Generate updated agent configuration (v2)
        print("  → Generating Retell agent configuration v2")
        generate_agent(account, "v2")

        # Step 5 — Generate version diff
        print("  → Creating configuration changelog")
        generate_diff(account)

        # log completion
        with open(f"{LOG_DIR}/pipeline.log", "a") as log:
            log.write(f"Completed pipeline for account: {account}\n")

        print("  ✓ Completed\n")

    print("Pipeline execution finished successfully.")


if __name__ == "__main__":
    pipeline()