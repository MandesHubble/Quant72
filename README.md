# Quant72

A Twitter bot built with [ElizaOS](https://github.com/ai16z/eliza) and TypeScript that tracks crypto Key Opinion Leaders (KOLs) and market data, posting insights to Twitter. This project auto-posts:

- **KOL Token Mentions**: Tokens mentioned by crypto KOLs (≥5 mentions) daily at 12:00 PM (noon).
- **Market Data**: Token and AI agent trends from [sentient.market](https://www.sentient.market/) and [cookie.fun](https://www.cookie.fun/) daily at 2:00 PM.
- **Replies**: Responds to @-mentions about Solana tokens with basic analysis (planned).

Built for collaboration, this repo integrates Python (ElizaOS) for Twitter interactions and TypeScript for market data scraping and Solana analysis.

---

## Features

### KOL Token Mentions
- Tracks tweets from a predefined list of crypto KOLs.
- Posts the most-mentioned token (if ≥5 mentions) with sentiment analysis at noon daily.

### Market Tracking
- Scrapes token prices from [sentient.market](https://www.sentient.market/) and AI agent mindshare from [cookie.fun](https://www.cookie.fun/).
- Posts a market update (e.g., top token by price) at 2 PM daily.

### Mention Replies
- Responds to @-mentions with basic Solana token data (e.g., supply) via TypeScript analysis (planned).

---

## Prerequisites

- **WSL** (Ubuntu recommended) on Windows.
- **Node.js** and `pnpm` (`npm install -g pnpm`).
- **Python 3.10+** with `pip` and `venv`.
- **Git** for version control.
- **Twitter API Keys** (create an app at [developer.x.com](https://developer.x.com)).

---
# Roadmap

*ElizaOS AI Agent: Single-agent, multi-actions, Python-based, integrated with a TypeScript agent.*  
*Team Responsibilities: Mandes (Phase 1 & 3), Zhou (Phase 2)*

---

## Phase 1: Environment Setup
- **Assigned**: Mandes
- **Tasks**:
  - Environment setup ->
  - elizaOs env, connect to twitter, set AI model
  - set up Ts Token agent for data analysis
- **Steps**:
  1. Clone `https://github.com/ai16z/eliza` into `eliza/`, install dependencies.
  2. Configure Twitter API in `eliza/.env`.
  3. Initialize `token-agent/` with TypeScript, `@solana/web3.js`, etc.
  4. Create `eliza/output/` for data handoff.

---

## Phase 2: Build Twitter Agent (Post)
- **Assigned**: Zhou
- **Function**:
  - Read KOL post and find out the highlight Token
  - Auto posting for x times of mentions (text & img)
  - Set character (funny, professional, present using data)
- **Setup**:
  - `pip install tweepy vaderSentiment` (for track Twitter KOL post)
- **Steps**:
  1. Create posting action for agent (`post_kol_mentions.py`)
  2. Configure Character
  3. Test

---

## Phase 3: Build Market Tracking Agent
- **Assigned**: Mandes
- **Sources**:
  - [https://www.sentient.market/](https://www.sentient.market/)
  - [https://www.cookie.fun/](https://www.cookie.fun/)
- **Function**:
  - Get data from source, like maketcap, token price, trends, AI Agent mind share
  - Analyze data
- **Steps**:
  1. Find API doc of those webs
  2. Create posting action for agent (`marketAgent.ts`)
  3. Integrate with elizaOs
  4. Update character config
  5. Test

---

## To Be Confirmed

### Phase 4: Build Twitter Agent (Reply)
- **Function**:
  - Reply those mentions on Twitter
  - Update character to limit the reply topics

### Phase 5: Test and Finalize
