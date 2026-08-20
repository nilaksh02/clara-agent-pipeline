// src/components/layout/Footer.js
// Shared footer for the app shell. Lives in layout/ next to Header/Sidebar/MainLayout.
// Adapted from the reference: fixed the logo path to this repo's assets folder.
// NOTE: this needs Footer.css (same folder) and MainLayout.js to render <Footer />.

import "./Footer.css";

const socialLinks = [
  {
    name: "Facebook",
    href: "https://www.facebook.com",
    path: "M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z",
  },
  {
    name: "Twitter / X",
    href: "https://www.twitter.com",
    path: "M18.9 3H22l-7.6 8.7L23 21h-6.9l-5.4-6.6L4.4 21H1.3l8.1-9.3L1 3h7l4.9 6 6-6zM17.7 19.1h1.7L7.4 4.8H5.6l12.1 14.3z",
  },
  {
    name: "LinkedIn",
    href: "https://www.linkedin.com",
    path: "M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.3c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V21H9z",
  },
  {
    name: "YouTube",
    href: "https://www.youtube.com",
    path: "M23 12s0-3.5-.4-5.2c-.3-.9-1-1.6-1.9-1.9C19 4.5 12 4.5 12 4.5s-7 0-8.7.4c-.9.3-1.6 1-1.9 1.9C1 8.5 1 12 1 12s0 3.5.4 5.2c.3.9 1 1.6 1.9 1.9 1.7.4 8.7.4 8.7.4s7 0 8.7-.4c.9-.3 1.6-1 1.9-1.9.4-1.7.4-5.2.4-5.2zM9.8 15.3V8.7l5.7 3.3z",
  },
  {
    name: "Instagram",
    href: "https://www.instagram.com",
    path: "M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4a6.4 6.4 0 1 0 0 12.8 6.4 6.4 0 0 0 0-12.8zm0 10.6a4.2 4.2 0 1 1 0-8.4 4.2 4.2 0 0 1 0 8.4zm6.6-10.9a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z",
  },
];

const footerLinks = [
  { label: "Contact us", href: "/contact-us" },
  { label: "Privacy policy", href: "/privacy-policy" },
  { label: "Our locations", href: "/our-locations" },
  { label: "Our Code of Conduct and Ethics", href: "/code-of-conduct-and-ethics" },
  { label: "Cookie policy", href: "/cookie-policy" },
  { label: "Accessibility", href: "/accessibility" },
];

function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-top">
        <div className="footer-brand">
          {/* Path fixed for this repo: assets/images/ (reference used assets/logo/) */}
          <img
            src="/assets/images/logo.png"
            className="footer-logo-img"
            alt="Standard Chartered"
          />
        </div>

        <div className="footer-social">
          {socialLinks.map((social) => (
            <a
              key={social.name}
              className="footer-social-link"
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={social.name}
            >
              <svg className="footer-social-icon" viewBox="0 0 24 24" aria-hidden="true">
                <path d={social.path} />
              </svg>
            </a>
          ))}
        </div>
      </div>

      <div className="footer-bottom">
        <ul className="footer-links">
          {footerLinks.map((link) => (
            <li key={link.label}>
              <a className="footer-link" href={link.href}>
                {link.label}
              </a>
            </li>
          ))}
        </ul>

        <p className="footer-copyright">
          &copy; Standard Chartered 2026
          <br />
          All Rights Reserved
        </p>
      </div>
    </footer>
  );
}

export default Footer;

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






