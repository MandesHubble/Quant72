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
Ensure the following tools are installed with these specific versions (or later, if compatible):

- **WSL** (Ubuntu recommended) on Windows.
- **Node.js**: v20.18.3
- **npm**: v10.8.2 (comes with Node.js)
- **pnpm**: v9.15.0
- **Python**: v3.12.3 (or compatible version in virtual environment)
- **Git**: v2.39.2 (or later)
- **Twitter API Keys** (create an app at [developer.x.com](https://developer.x.com))
  
## Setup Instructions for Developers

### 1. Install System Prerequisites (Ubuntu WSL)
```bash
sudo apt update
sudo apt install -y build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev libpng-dev python3-dev g++ python3 python3-pip python3-venv git
sudo ln -s /usr/bin/python3 /usr/bin/python
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g pnpm
```

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
- **Dependencies**:
  - `@0glabs/0g-ts-sdk@0.2.1`
  - `@coinbase/coinbase-sdk@0.10.0`
  - `@deepgram/sdk@3.11.1`
  - `@elizaos-plugins/adapter-sqlite@<version>` (linked: `packages/adapter-sqlite`)
  - `@injectivelabs/sdk-ts@1.14.41`
  - `@vitest/eslint-plugin@1.0.1`
  - `amqplib@0.10.5`
  - `bs58@5.0.0`
  - `csv-parse@5.6.0`
  - `langdetect@0.2.1`
  - `ollama-ai-provider@0.16.1`
  - `optional@0.1.4`
  - `pnpm@9.15.0`
  - `sharp@0.33.5`
  - `ws@8.18.0`
  - `zod@3.24.1`
- ##Dev Dependencies**:
  - `@biomejs/biome@1.9.4`
  - `@commitlint/cli@18.6.1`
  - `@commitlint/config-conventional@18.6.3`
  - `@types/jest@29.5.14`
  - `cli@<version>` (linked: `packages/cli`)
  - `concurrently@9.1.0`
  - `cross-env@7.0.3`
  - `husky@9.1.7`
  - `jest@29.7.0`
  - `lerna@8.1.5`
  - `nodemon@3.1.7`
  - `only-allow@1.2.1`
  - `turbo@2.4.2`
  - `typedoc@0.26.11`
  - `typescript@5.6.3`
  - `viem@2.21.58`
  - `vite@5.4.12`
  - `vitest@3.0.5`

---

## Phase 3: Build Market Tracking Agent
- **Assigned**: Mandes
- **Data Sources**:
  - CCXT, https://docs.ccxt.com/
  - Binance, https://binance-docs.github.io/apidocs/spot/en/
- **Function**:
  - Get data from source, like maketcap, token price, trends, AI Agent mind share
  - Analyze data
- **Steps**:
  1. Find API doc of those webs
  2. Create posting action for agent (`marketAgent.ts`)
  3. Integrate with elizaOs
  4. Update character config
  5. Test
- **Dependencies**:
  - `@solana/web3.js@1.98.0`
  - `axios@1.8.1`
  - `canvas@3.1.0`
  - `ccxt@4.4.62`
  - `chart.js@3.9.1`
  - `chartjs-node-canvas@4.1.6`
  - `cheerio@1.0.0`
  - `typescript@5.7.3`
- **Dev Dependencies**:
  - `@types/node@22.13.5`
  - `ts-node@10.9.2`

---

## To Be Confirmed

### Phase 4: Build Twitter Agent (Reply)
- **Function**:
  - Reply those mentions on Twitter
  - Update character to limit the reply topics

### Phase 5: Test and Finalize

### Phase 6 (Future): Build Solana Token Agent
- **Function**:
  - Get Token data mentioned by KOL and analyze

---
