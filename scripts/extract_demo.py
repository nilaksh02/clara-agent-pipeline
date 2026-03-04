import os
import json
from utils.extractor import extract_information


def run(account):

    demo_path = f"dataset/{account}/demo.txt"

    with open(demo_path) as f:
        transcript = f.read()

    memo = extract_information(transcript, account)

    output_path = f"outputs/accounts/{account}/v1"

    os.makedirs(output_path, exist_ok=True)

    with open(f"{output_path}/account_memo.json", "w") as f:
        json.dump(memo, f, indent=2)