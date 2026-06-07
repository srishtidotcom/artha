# 🪙 Artha — Loan Sales Agent — Build Log

> *अर्थ (Artha) — wealth, meaning, purpose*

Artha is an end-to-end **Agentic AI platform** built for a large-scale NBFC that sells personal loans across India. A Master Agent orchestrates multiple specialized Worker Agents to handle the complete loan journey — from the first "hello" to a signed sanction letter — entirely through a conversational web chatbot.

---


| Name | Role |
|------|------|
| Srishti | Builder |

---

## 📌 What Artha Does

A customer clicks a digital ad or opens a marketing email and lands on the chatbot. From that moment, Artha takes over:

1. **Greets & understands** the customer's loan needs
2. **Negotiates** amount, tenure, and interest rate
3. **Verifies** KYC details against CRM records
4. **Underwrites** the loan using live credit score + eligibility rules
5. **Requests a salary slip** if needed and validates EMI affordability
6. **Generates a PDF sanction letter** on approval — or explains rejection clearly
7. **Closes the conversation** naturally, like a human sales executive would

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Web Chatbot UI                   │
│              (Customer-facing interface)            │
└─────────────────────┬───────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────┐
│               Master Agent (Artha)                  │
│         Orchestrator · Conversation Manager         │
└──┬──────────┬──────────┬──────────┬─────────────────┘
   │          │          │          │
   ▼          ▼          ▼          ▼
Sales     Verifi-    Under-     Sanction
Agent     cation     writing    Letter
          Agent      Agent      Generator
   │          │          │
   ▼          ▼          ▼
Offer     CRM        Credit
Mart      Server     Bureau
API                  API
```


## ⚙️ System Prerequisites

Make sure the following are installed before you begin:

- **Python 3.11+** — `python --version`
- **Git** — for version control
- **VS Code** — recommended editor
- **OpenAI or Anthropic API key** — for LLM calls
- **Postman / Bruno** *(optional)* — for testing mock APIs

---

## 📁 Folder Structure

```
artha-loan-agent/
├── backend/
│   ├── agents/
│   │   ├── master_agent.py
│   │   ├── sales_agent.py
│   │   ├── verification_agent.py
│   │   ├── underwriting_agent.py
│   │   └── sanction_letter.py
│   ├── mock_apis/
│   │   ├── crm_server.py
│   │   ├── credit_bureau.py
│   │   └── offer_mart.py
│   ├── data/
│   │   ├── customers.json
│   │   └── dummy_salary_slip.pdf
│   ├── outputs/           # generated sanction letters land here
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── chat.js
│   └── style.css
└── README.md
```

---

## 🚀 Environment Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/artha-loan-agent.git
cd artha-loan-agent
```

### 2. Create & activate a virtual environment
```bash
cd backend
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
.\\venv\\Scripts\\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
fastapi
uvicorn
langgraph          # or crewai — pick one
openai             # or anthropic
reportlab
python-multipart
httpx
requests
python-dotenv
```

### 4. Set up environment variables

Create a `.env` file inside `backend/`:
```env
OPENAI_API_KEY=sk-...
CRM_BASE_URL=http://localhost:8001
CREDIT_BUREAU_URL=http://localhost:8002
OFFER_MART_URL=http://localhost:8003
```

> ⚠️ Add `.env` to `.gitignore` immediately — never commit API keys.

---

## 🛠️ Step-by-Step Build Plan

### Phase 1 — Project Setup & Data

- [ ] **Step 1** — Initialize repo, folder structure, virtual environment, install dependencies
- [ ] **Step 2** — Create `customers.json` with 10+ dummy customers (name, age, city, income, credit score, pre-approved limit, KYC details)
- [ ] **Step 3** — Build three FastAPI mock APIs:
  - `GET /customer/{id}` → KYC data (port 8001)
  - `GET /credit-score/{id}` → score out of 900 (port 8002)
  - `GET /offers/{id}` → pre-approved loan limit (port 8003)

### Phase 2 — Worker Agents

- [ ] **Step 4** — **Sales Agent** — discusses loan needs, negotiates amount/tenure/rate, captures intent. Conversational and persuasive.
- [ ] **Step 5** — **Verification Agent** — calls CRM mock, confirms KYC (name, phone, address), flags mismatches.
- [ ] **Step 6** — **Underwriting Agent** — calls credit bureau, applies eligibility rules:
  - Score < 700 → **Reject**
  - Loan ≤ pre-approved limit → **Instant approve**
  - Loan ≤ 2× limit → **Request salary slip**, approve only if EMI ≤ 50% of salary
  - Loan > 2× limit → **Reject**
- [ ] **Step 7** — **Salary slip upload** — file upload endpoint + dummy PDF. Underwriting Agent reads mock salary value and validates.
- [ ] **Step 8** — **Sanction Letter Generator** — generates a formatted PDF (customer name, amount, tenure, EMI, interest rate, date) using ReportLab.

### Phase 3 — Master Agent & Orchestration

- [ ] **Step 9** — Design the orchestration graph: `Greet → Sales → Verify → Underwrite → (Upload?) → Sanction/Reject → Close`
- [ ] **Step 10** — Wire Master Agent ↔ Worker Agents with full handoff logic
- [ ] **Step 11** — Handle edge cases: rejection flows, KYC mismatch retry, salary slip re-request, mid-conversation abandonment

### Phase 4 — Frontend Chatbot UI

- [ ] **Step 12** — Build web chat interface (React or plain HTML/JS), connect to backend via REST or WebSocket, support file upload
- [ ] **Step 13** — Show sanction letter download link in chat on approval

### Phase 5 — Testing & Demo

- [ ] **Step 14** — End-to-end happy path: eligible customer → sanction letter
- [ ] **Step 15** — Test all edge cases (rejection, salary slip, KYC mismatch)
- [ ] **Step 16** — Polish conversation quality — tone, persuasiveness, naturalness
- [ ] **Step 17** — Record demo walkthrough: ad click → chat → verification → underwriting → letter downloaded

---

## 🔑 Key Design Decisions

| Decision | Choice |
|----------|--------|
| Agent framework | LangGraph *(recommended)* or CrewAI |
| LLM | GPT-4o or Claude Sonnet |
| Sales Agent temperature | ~0.5 (creative, conversational) |
| Underwriting Agent temperature | ~0.1 (precise, rule-based) |
| Mock API ports | CRM: 8001 · Credit Bureau: 8002 · Offer Mart: 8003 |
| Salary slip | Dummy PDF with hardcoded salary value for EMI validation |
| Sanction letters | Saved to `backend/outputs/` as `sanction_{customer_id}.pdf` |

---

## 💻 Commands Cheat Sheet

```bash
# Start all services (run each in a separate terminal)
uvicorn main:app --reload --port 8000           # Master Agent backend
uvicorn mock_apis.crm_server:app --port 8001    # CRM mock
uvicorn mock_apis.credit_bureau:app --port 8002 # Credit Bureau mock
uvicorn mock_apis.offer_mart:app --port 8003    # Offer Mart mock

# Dependency management
pip install -r requirements.txt
pip freeze > requirements.txt

# Git workflow
git add .
git commit -m "your message"
git push origin main
```

---

## 📋 Underwriting Rules (Quick Reference)

```
Credit score < 700            → REJECT
Loan > 2× pre-approved limit  → REJECT
Loan ≤ pre-approved limit     → INSTANT APPROVE ✅
Loan between 1×–2× limit      → REQUEST SALARY SLIP
  └─ EMI ≤ 50% of salary      → APPROVE ✅
  └─ EMI > 50% of salary      → REJECT ❌
```

---


