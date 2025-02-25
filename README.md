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
