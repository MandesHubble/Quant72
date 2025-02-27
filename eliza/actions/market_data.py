import json
import subprocess

def post_market_data():
  subprocess.run(["node", "../token-agent/dist/marketAgent.js"])
  with open("output/market.json", "r") as f:
    data = json.load(f)
  return {"text": data["text"], "image": "output/market_graph.png"}
