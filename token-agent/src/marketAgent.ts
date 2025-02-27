import ccxt from "ccxt";
import { ChartJSNodeCanvas } from "chartjs-node-canvas";
import * as fs from "fs";

interface MarketData {
  tokenName: string;
  price?: number;
  volume?: number;
  timestamp?: number;
  source: string;
}

async function trackMarket(): Promise<void> {
  const binance = new ccxt.binance({ enableRateLimit: true });
  const results: MarketData[] = [];
  const symbol = "SOL/USDT";

  try {
    const ohlcv = await binance.fetchOHLCV(symbol, "1h", undefined, 24);
    ohlcv.forEach(([timestamp, open, high, low, close, volume]) => {
      results.push({
        tokenName: symbol.split("/")[0],
        price: close,
        volume,
        timestamp,
        source: "Binance",
      });
    });
  } catch (e) {
    console.error(`Binance OHLCV fetch failed:`, e);
  }

  const width = 800;
  const height = 400;
  const backgroundColour = 'white'
  const chartJSNodeCanvas = new ChartJSNodeCanvas({ width, height, backgroundColour });
  const configuration = {
    type: "line" as const,
    data: {
      labels: results.map(r => new Date(r.timestamp!).toLocaleTimeString()),
      datasets: [{
        label: `${symbol} Price (USD)`,
        data: results.map(r => r.price ?? null),
        borderColor: "rgba(75, 192, 192, 1)",
        fill: false,
      }],
    },
    options: {
      scales: {
        x: { display: true, title: { display: true, text: "Time (Last 24h)" } },
        y: { display: true, title: { display: true, text: "Price (USD)" } },
      },
    },
  };
  const imageBuffer = await chartJSNodeCanvas.renderToBuffer(configuration);
  fs.writeFileSync("../eliza/output/market_graph.png", imageBuffer);

  const latest = results[results.length - 1];
  const text = `Market Update: ${latest.tokenName} - Price: $${latest.price || "N/A"}, 24h Volume: ${latest.volume || "N/A"} (${latest.source})`;
  fs.writeFileSync("../eliza/output/market.json", JSON.stringify({ text }));
}

trackMarket().catch(console.error);