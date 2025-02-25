# Quant72

A Twitter bot built with ElizaOS and TypeScript that tracks crypto Key Opinion Leaders (KOLs) and market data, posting insights to Twitter. This project auto-posts:
KOL Token Mentions: Tokens mentioned by crypto KOLs (≥10 mentions) daily at noon.
Market Data: Token and AI agent trends from sentient.market and cookie.fun daily at 2:00 PM.
Replies: Responds to @-mentions about Solana tokens with basic analysis.
Built for collaboration, this repo integrates Python (ElizaOS) for Twitter interactions and TypeScript for market data scraping and Solana analysis.

# Road Map
*elizaOS AI Agent, single-agent, multi-actions, python-based, integral with TS agent 
*Responsibilities: Mandes(Phase_1&3), Zhou(Phase_2)

Phase_1:
	Environment setup -> 
	elizaOs env, connect to twitter, set AI model
	set up Ts Token agent for data analysis

Phase_2:
	Bulid Twitter Agent(post) ->
	function: 
		read KOL post and find out the highlight Token
		auto posting for x times of mentions(text&img)
		set character(funny, professional, present using data)
	setup: 
		pip install tweepy vaderSentiment(for track Twitter KOL post)
	step:
		1. create a posting action for the agent(post_kol_mentions.py)
		2. configure Character
		3. test
		
Phase_3:
	Build Market Tracking Agent ->
	source: 
		https://www.sentient.market/
		https://www.cookie.fun/
	function:
		get data from sources, like maketcap, token price, trends, AI Agent mind share
		analyze data
	step:
		1. find the API doc of those webs
		2. create a posting action for the agent(marketAgent.ts)
		3. integrate with elizaOs
		4. update character config
		5. test

-----------------------------------------------------------------------------------------------------
	
To be confirmed:

Phase_4:
	Bulid Twitter Agent(reply)->
	function:
		reply to those mentions on Twitter
	update character to limit the reply topics

Phase_5:
	Test and Finalize

Phase_6(future):
	Build Solana Token Agent ->
	function:
		get Token data mentioned by KOL and analyze
