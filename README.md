// src/pages/dashboard/PriorityCustomerTable.js
// US01 table. Added a gradient avatar (initials) in the name cell — [PAGE] level,
// this component is yours. Logic unchanged.

import PriorityBadge from "../../components/ui/PriorityBadge";
import { formatCurrency, formatDate } from "./dashboard.utils";

// derive up-to-2-letter initials from a name
function initials(name) {
  return name
    .split(" ")
    .map((w) => w[0])
    .slice(0, 2)
    .join("")
    .toUpperCase();
}

export default function PriorityCustomerTable({ customers, onSelectCustomer }) {
  return (
    <table className="dashboard-priority-table">
      <thead>
        <tr>
          <th>NAME</th>
          <th>PRIORITY</th>
          <th>DUE DATE</th>
          <th>CATEGORY</th>
          <th>REASON</th>
          <th>AMOUNT</th>
          <th>ACTION</th>
        </tr>
      </thead>
      <tbody>
        {customers.map((c) => (
          <tr key={c.id}>
            <td>
              <span className="dashboard-name-cell">
                <span className="dashboard-avatar">{initials(c.name)}</span>
                {c.name}
              </span>
            </td>
            <td>
              <PriorityBadge level={c.priority} />
            </td>
            <td>{formatDate(c.dueDate)}</td>
            <td>{c.category}</td>
            <td>{c.reason}</td>
            <td>{formatCurrency(c.amount)}</td>
            <td>
              <button className="dashboard-view-btn" onClick={() => onSelectCustomer?.(c.id)}>
                View
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}


// src/components/ui/ProductCard.js
// [COMMON COMPONENT] — adds a category icon + restructures the card top.
// Check with the team before merging, since all 7 pages share this component.
// The icon is derived from the label, so NO change to mockdata is needed.

import { formatCurrency } from "../../pages/dashboard/dashboard.utils";

const ICONS = {
  FD: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11M20 10v11M8 14v3M12 14v3M16 14v3" />
    </svg>
  ),
  "Mutual Fund": (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M3 3v18h18M7 15l4-4 3 3 5-6" />
    </svg>
  ),
  Bond: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M4 4h16v16H4zM8 9h8M8 13h8M8 17h5" />
    </svg>
  ),
  Insurance: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z" />
    </svg>
  ),
  "Portfolio Management": (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M4 7h16v13H4zM9 7V4h6v3" />
    </svg>
  ),
};

export default function ProductCard({ label, count, totalValue }) {
  return (
    <div className="dashboard-product-card">
      <div className="dashboard-product-card-top">
        <span className="dashboard-product-card-label">{label}</span>
        <span className="dashboard-product-icon">{ICONS[label] || null}</span>
      </div>
      <div className="dashboard-product-card-count">{count}</div>
      <div className="dashboard-product-card-value">{formatCurrency(totalValue)}</div>
    </div>
  );
}

# Clara Agent Automation Pipeline

## Overview

This project implements a **zero-cost automation pipeline** that converts demo call transcripts into a preliminary AI answering agent configuration and updates the configuration after onboarding.

The system processes demo and onboarding transcripts, extracts structured information, generates a **Retell Agent Draft Specification**, and applies updates when onboarding information is received.

The pipeline supports:

* Automated extraction of structured account data
* Generation of Retell agent configuration drafts
* Versioned updates after onboarding
* Change tracking between versions
* Batch processing of multiple accounts
* Operational dashboard and logging

The entire pipeline runs **without paid APIs or services**.

---

# Architecture

```
Demo Transcript
      ↓
Extraction Engine
      ↓
Account Memo JSON (v1)
      ↓
Agent Spec Generator
      ↓
Retell Agent Draft (v1)

Onboarding Transcript
      ↓
Onboarding Update Engine
      ↓
Account Memo JSON (v2)
      ↓
Agent Spec Generator
      ↓
Retell Agent Draft (v2)

Version Diff Engine
      ↓
Change Log (JSON + Markdown)
```

## Dataset Note

Demo and onboarding transcripts are excluded from this repository
to comply with the assignment requirement of not publishing raw
customer data.

To run the pipeline locally, place transcripts in the following format:

dataset/
   <account_id>/
      demo.txt
      onboarding.txt

---

# System Components

### 1. Transcript Extraction

Demo transcripts are processed to extract structured business information including:

* company name
* services supported
* business hours
* emergency definitions
* call routing rules

Extraction is implemented using **rule-based parsing** to comply with the **zero-cost constraint**.

---

### 2. Account Memo Generation

Extracted data is stored as a structured **Account Memo JSON**:

```
outputs/accounts/<account_id>/v1/account_memo.json
```

This memo acts as the **source of truth** for agent configuration.

---

### 3. Agent Configuration Generator

Using the extracted memo, the system generates a **Retell Agent Draft Specification** containing:

* agent name
* system prompt
* call routing logic
* emergency handling protocol
* fallback behavior

Example location:

```
outputs/accounts/<account_id>/v1/agent_spec.json
```

---

### 4. Onboarding Update Pipeline

Onboarding transcripts update the existing account memo.

The updated configuration is stored as:

```
outputs/accounts/<account_id>/v2/account_memo.json
outputs/accounts/<account_id>/v2/agent_spec.json
```

---

### 5. Change Tracking

Differences between v1 and v2 are automatically generated.

Two files are produced:

**Machine readable diff**

```
changes.json
```

**Human readable explanation**

```
changes.md
```

This allows quick understanding of:

* what changed
* previous values
* updated values
* onboarding confirmation

---

# Folder Structure

```
clara-agent-pipeline
│
├ dataset
│   └ <account_id>
│       ├ demo.txt
│       └ onboarding.txt
│
├ outputs
│   └ accounts
│       └ <account_id>
│           ├ v1
│           │   ├ account_memo.json
│           │   └ agent_spec.json
│           │
│           ├ v2
│           │   ├ account_memo.json
│           │   └ agent_spec.json
│           │
│           ├ changes.json
│           └ changes.md
│
├ scripts
│   ├ extract_demo.py
│   ├ generate_agent.py
│   ├ apply_onboarding.py
│   ├ diff_generator.py
│   └ dashboard.py
│
├ utils
│   ├ extractor.py
│   ├ schema.py
│   └ retell_mock.py
│
├ workflows
│   └ pipeline_design.md
│
├ logs
│   └ pipeline.log
│
├ run_pipeline.py
├ README.md
├ requirements.txt
├ dashboard.py
└ .gitignore
```

---

# How to Run

Clone the repository and run:

```
python run_pipeline.py
```

The pipeline will:

1. Extract structured information from demo transcripts
2. Generate preliminary agent configuration (v1)
3. Apply onboarding updates
4. Generate updated agent configuration (v2)
5. Produce version diffs and change logs

Outputs are saved in:

```
outputs/accounts/
```

---

# Dashboard

A simple operational dashboard is included to summarize processed accounts.

Run:

```
python scripts/dashboard.py
```

This displays:

* accounts processed
* services detected
* emergency definitions
* business hours

Example output:

```
Pipeline Summary

Accounts processed: 5
Agent drafts created: 5
Onboarding updates applied: 5
Diffs generated: 5
```

---

# Logging

Pipeline execution logs are written to:

```
logs/pipeline.log
```

This provides traceability for batch runs.

---

## Dashboard

A Streamlit dashboard is provided to visualize processed accounts
and configuration changes.

Run:

streamlit run dashboard.py

---

# Retell Integration

If Retell API access is unavailable, the system generates a **Retell Agent Draft Specification** which can be manually imported into Retell.

A **mock Retell integration layer** is included to simulate agent creation.

```
utils/retell_mock.py
```

---

# Pipeline Properties

### Idempotent Execution

The pipeline is **safe to run multiple times**.

Running the pipeline again regenerates outputs based on the latest transcripts without creating duplicate artifacts.

---

# Design Decisions

* **Rule-based extraction** was used to avoid paid LLM APIs
* **JSON storage** ensures transparency and reproducibility
* **Versioned configuration** enables clear onboarding updates
* **Modular scripts** improve maintainability
* **Mock integration layer** simulates external API behavior

---

# Limitations

* Rule-based extraction may miss nuanced context
* Transcript formatting assumptions may affect detection accuracy
* Retell agent creation is simulated rather than API-driven

---

# Future Improvements

* Local open-source LLM extraction (Whisper + small LLM)
* Visual web dashboard
* Direct Retell API integration
* Advanced entity extraction using NLP models
* Automatic transcript ingestion pipeline






