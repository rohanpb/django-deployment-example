# 🔗 AbellFi: ICP-Powered Decentralized Trading Infrastructure

AbellFi is a non-open-source, AI-driven crypto investment platform that integrates deeply with the **Internet Computer Protocol (ICP)**. It enables secure, decentralized, and automated cross-chain trading powered by ICP smart contracts (canisters), with built-in ECDSA signing and multi-wallet support.

This repository contains the **canister logic** powering our backend infrastructure, including transaction management, EVM wallet generation, and cross-chain execution—leveraging features like **HTTPS outcalls**, **ECDSA signatures**, and **Chain Fusion**.

---

## 🌐 Project Overview

AbellFi democratizes access to institutional-grade crypto investment strategies by combining:

- **Decentralized execution on Internet Computer**
- **AI-driven investment models**
- **Cross-chain trade support**
- **Secure, self-custodial wallet management**

Our primary goal is to make advanced trading strategies available to all crypto users while ensuring transparency, security, and decentralization through ICP.

---

## 📐 Architecture & Tech Stack

### ⚙️ Core Architecture

```mermaid
graph TD
  A[Frontend (Next.js)]
  B[ICP Canisters]
  C[Polygon RPC Node]
  D[Management Canister]
  E[Django Backend]

  A --> B
  A --> E
  E --> B
  B --> C
  B --> D
Frontend: Next.js

Backend: Django REST Framework

Canisters: Rust (ic-cdk)

Chain Integration: Polygon via Chain Fusion, HTTPS outcalls, and ECDSA

Authentication: IdentityKit, Plug Wallet

✅ Milestones & Progress
Milestone 1
 Integrated IdentityKit (Internet Identity) for user authentication

 Linked user sessions in Django using ICP principals

 Demoed complete login/authentication flow

Milestone 2
 Developed Django service layer to interface with ICP canisters using ic-py

 Created event queue + worker architecture for trade event processing

 Simulated and passed stress tests for 50K concurrent users

 Demoed end-to-end trade execution via Plug wallet and ICP canisters

Milestone 3
 Developed ECDSA-based canister logic for deriving user EVM wallets

 Integrated Polygon chain support via Chain Fusion (ic-alloy)

 Implemented key canister methods:

approve_token

swap_token

swap_token_admin

withdraw_erc_20

withdraw_native_token

 Connected these methods to Django backend and frontend UI

 Demoed cross-chain transaction from login → execution → confirmation on dashboard

💡 How It Works
Run Locally
bash
Copy code
# Start the local replica
dfx start --background

# Deploy canisters
dfx deploy

# (Optional) Generate candid interface
npm run generate

# Start frontend dev server
npm start
Access frontend at: http://localhost:8080

Access replica at: http://localhost:4943?canisterId=<your_canister_id>

Frontend Environment Notes
If deploying frontend without DFX:

Set DFX_NETWORK=ic manually

Override process.env.DFX_NETWORK in declarations if needed

Optionally, set env_override in dfx.json
