import streamlit as st
import os
import json

BASE = "outputs/accounts"

st.set_page_config(page_title="Clara Agent Pipeline Dashboard", layout="wide")

st.title("Clara Agent Automation Pipeline")

if not os.path.exists(BASE):
    st.error("No processed accounts found.")
    st.stop()

# Only show accounts that actually have output files
accounts = []

for account in os.listdir(BASE):
    v2_file = os.path.join(BASE, account, "v2", "account_memo.json")
    if os.path.exists(v2_file):
        accounts.append(account)

if not accounts:
    st.warning("No processed accounts available yet.")
    st.stop()

st.sidebar.header("Accounts")
selected_account = st.sidebar.selectbox("Select Account", accounts)

account_path = os.path.join(BASE, selected_account)

v1_path = os.path.join(account_path, "v1", "account_memo.json")
v2_path = os.path.join(account_path, "v2", "account_memo.json")
changes_path = os.path.join(account_path, "changes.json")

st.subheader("Pipeline Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Accounts Processed", len(accounts))
col2.metric("Agent Versions", len(accounts) * 2)
col3.metric("Change Logs Generated", len(accounts))

st.divider()

if os.path.exists(v2_path):

    with open(v2_path) as f:
        memo = json.load(f)

    st.subheader("Account Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Company Name:", memo.get("company_name"))
        st.write("Account ID:", memo.get("account_id"))

        st.write("Services Supported")
        st.write(memo.get("services_supported"))

        st.write("Emergency Definitions")
        st.write(memo.get("emergency_definition"))

    with col2:
        st.write("Business Hours")
        st.json(memo.get("business_hours"))

        st.write("Emergency Routing Rules")
        st.write(memo.get("emergency_routing_rules"))

        st.write("Non Emergency Routing Rules")
        st.write(memo.get("non_emergency_routing_rules"))

st.divider()

if os.path.exists(changes_path):

    with open(changes_path) as f:
        changes = json.load(f)

    st.subheader("Changes (v1 → v2)")

    if changes:
        for field, change in changes.items():

            st.markdown(f"### {field}")

            col1, col2 = st.columns(2)

            with col1:
                st.write("Before")
                st.write(change["before"])

            with col2:
                st.write("After")
                st.write(change["after"])

    else:
        st.write("No changes detected.")