import { IAgentRuntime, elizaLogger, Memory, Provider } from "@elizaos/core";
import * as fs from "fs";
import path from "path";

const ccxtProvider: Provider = {
    
    get: async (runtime: IAgentRuntime, message: Memory) => {
        const workspaceRoot = process.env.WORKSPACE_ROOT || '/default/path'; 
        const dataDir = path.join(workspaceRoot, 'services/ccxtData/output');
 
        const exchangeRatesData = fs.readFileSync(path.join(dataDir, "exchange_rates.json"), "utf8");
        const orderbooksData = fs.readFileSync(path.join(dataDir, "orderbooks.json"), "utf8");
        const tradesData = fs.readFileSync(path.join(dataDir, "trades.json"), "utf8");
        const ohlcvData = fs.readFileSync(path.join(dataDir, "ohlcv.json"), "utf8");
        const tickersData = fs.readFileSync(path.join(dataDir, "tickers.json"), "utf8");
        const data = tickersData+exchangeRatesData+orderbooksData+tradesData+ohlcvData;
        
        elizaLogger.log("CCXT Provider get called: ", data);

        return 'Generate tweet about Tokens analysis by using these data and follow these rules. Rules: 1.Add $Token_name withour pairs when you mention the token in the tweet (e.g. $BMT instead of $BMT/USDT). 2.Add atleast 3 hashtags for the tweet (e.g. #crypto, #blockchain, #$Token_name). Tickers data:' + tickersData 
        + "Exchange rates data:" + exchangeRatesData
        + "Orderbooks data:" + orderbooksData
        + "Trades data:" + tradesData
        + "OHLCV data:" + ohlcvData;
    }


}

export { ccxtProvider };