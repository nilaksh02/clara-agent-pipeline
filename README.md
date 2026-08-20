/* src/pages/dashboard/Dashboard.css
   RM Dashboard (US01) — Standard Chartered visual identity.

   SCOPE MARKERS:
   [PAGE]   = specific to this dashboard page, safe to own/change freely
   [COMMON] = shared component look (cards / button / badge). If the team has a
              shared stylesheet these should eventually move there. */

:root {
  --sc-blue: #0072aa;
  --sc-blue-dark: #005e8c;
  --sc-blue-bright: #0473ea;
  --sc-green: #21aa47;
  --sc-green-bright: #38d200;
  --sc-light-blue: #78add2;

  --text-primary: #1a2b3c;
  --text-secondary: #5a6b7b;
  --text-muted: #8a97a5;

  --background: #f4f7fa;
  --surface: #ffffff;
  --border: #e3e9ef;
  --border-light: #eef2f6;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;

  --status-error-bg: #fdecec;
  --status-error-text: #c0392b;
  --status-warning-bg: #fff6e5;
  --status-warning-text: #b7791f;
  --status-success-bg: #eaf6ec;
  --status-success-text: #21aa47;

  --sc-gradient: linear-gradient(120deg, #005e8c 0%, #0072aa 40%, #0e8f6e 75%, #21aa47 100%);
}

.dashboard-page {
  font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
  background: var(--background);
  padding: 28px 32px;
  color: var(--text-primary);
  max-width: 1440px;
  margin: 0 auto;
}

/* ---- [PAGE] Branded gradient hero header ---- */
.dashboard-hero {
  background: var(--sc-gradient);
  border-radius: var(--radius-lg);
  padding: 28px 32px;
  color: #fff;
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 94, 140, 0.25);
}
.dashboard-hero::after {
  content: "";
  position: absolute;
  right: -60px; top: -60px;
  width: 240px; height: 240px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 50%;
}
.dashboard-hero::before {
  content: "";
  position: absolute;
  right: 40px; bottom: -80px;
  width: 180px; height: 180px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 50%;
}
.dashboard-hero-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  position: relative;
  z-index: 1;
  gap: 16px;
}
.dashboard-title {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.01em;
  margin: 0;
  color: #fff;
}
.dashboard-subtitle {
  font-size: 14px;
  opacity: 0.85;
  margin: 6px 0 0 0;
}
.dashboard-hero-actions { display: flex; gap: 12px; flex-shrink: 0; }
.dashboard-hero-btn-ghost {
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #fff;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  font-size: 14px; font-weight: 600; cursor: pointer;
}
.dashboard-hero-btn-white {
  background: #fff; color: var(--sc-blue-dark);
  border: none;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  font-size: 14px; font-weight: 600; cursor: pointer;
}

/* ---- [COMMON] Product summary cards ---- */
.dashboard-product-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 18px;
  margin-top: 24px;
}
.dashboard-product-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 20px;
  box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.dashboard-product-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(16, 24, 40, 0.08);
}
.dashboard-product-card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.dashboard-product-card-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.dashboard-product-icon {
  width: 38px; height: 38px;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  background: #e8f2f8; color: var(--sc-blue);
}
.dashboard-product-icon svg { width: 20px; height: 20px; }
.dashboard-product-card-count {
  font-size: 30px; font-weight: 700;
  color: var(--text-primary); line-height: 1;
}
.dashboard-product-card-value {
  font-size: 13px; color: var(--text-muted); margin-top: 8px;
}

/* ---- [PAGE] Priority Customers panel ---- */
.dashboard-priority-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  margin-top: 26px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
}
.dashboard-priority-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid var(--border-light);
  gap: 16px;
}
.dashboard-priority-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
  display: flex;
  align-items: center;
  gap: 10px;
}
.dashboard-priority-title::before {
  content: "";
  width: 4px; height: 18px;
  background: var(--sc-gradient);
  border-radius: 2px;
}
.dashboard-search-input {
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 9px 14px;
  font-size: 14px;
  color: var(--text-primary);
  min-width: 260px;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
.dashboard-search-input:focus {
  outline: none;
  border-color: var(--sc-blue);
  box-shadow: 0 0 0 3px rgba(0, 114, 170, 0.12);
}

.dashboard-priority-table { width: 100%; border-collapse: collapse; }
.dashboard-priority-table thead th {
  text-align: left;
  font-size: 11px; font-weight: 700; letter-spacing: 0.05em;
  text-transform: uppercase; color: var(--sc-blue);
  background: #f0f6fa;
  padding: 13px 24px;
  border-bottom: 1px solid var(--border);
}
.dashboard-priority-table tbody td {
  padding: 15px 24px;
  font-size: 14px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-light);
}
.dashboard-priority-table tbody tr:last-child td { border-bottom: none; }
.dashboard-priority-table tbody tr { transition: background 0.12s ease; }
.dashboard-priority-table tbody tr:hover { background: #f6fafd; }

/* [PAGE] gradient avatar in the name cell */
.dashboard-name-cell { display: flex; align-items: center; gap: 12px; font-weight: 600; }
.dashboard-avatar {
  width: 34px; height: 34px;
  border-radius: 50%;
  background: var(--sc-gradient);
  color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; font-weight: 700;
  flex-shrink: 0;
}

/* ---- [COMMON] View button ---- */
.dashboard-view-btn {
  background: var(--surface);
  color: var(--sc-blue);
  border: 1px solid var(--sc-blue);
  border-radius: var(--radius-sm);
  padding: 6px 16px;
  font-size: 13px; font-weight: 600; cursor: pointer;
  transition: background 0.15s ease;
}
.dashboard-view-btn:hover { background: #eaf3f8; }

/* ---- [COMMON] Priority badge ---- */
.dashboard-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.02em;
}
.dashboard-badge-high { background: var(--status-error-bg); color: var(--status-error-text); }
.dashboard-badge-medium { background: var(--status-warning-bg); color: var(--status-warning-text); }
.dashboard-badge-low { background: var(--status-success-bg); color: var(--status-success-text); }

/* Responsive */
@media (max-width: 768px) {
  .dashboard-page { padding: 16px; }
  .dashboard-hero-row { flex-direction: column; }
  .dashboard-priority-header { flex-direction: column; align-items: flex-start; }
  .dashboard-search-input { width: 100%; min-width: 0; }
  .dashboard-priority-table { display: block; overflow-x: auto; white-space: nowrap; }
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






