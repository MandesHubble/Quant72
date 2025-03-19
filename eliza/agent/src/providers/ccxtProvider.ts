import { IAgentRuntime, elizaLogger, Memory, Provider } from "@elizaos/core";
import * as fs from "fs";
const ccxtProvider: Provider = {
    
    get: async (runtime: IAgentRuntime, message: Memory) => {
        const exchangeRatesData = fs.readFileSync("/home/mandes/Quant72/services/ccxtData/output/exchange_rates.json", "utf8");
        const orderbooksData = fs.readFileSync("/home/mandes/Quant72/services/ccxtData/output/orderbooks.json", "utf8");
        const tradesData = fs.readFileSync("/home/mandes/Quant72/services/ccxtData/output/trades.json", "utf8");
        const ohlcvData = fs.readFileSync("/home/mandes/Quant72/services/ccxtData/output/ohlcv.json", "utf8");
        const tickersData = fs.readFileSync("/home/mandes/Quant72/services/ccxtData/output/tickers.json", "utf8");
        const data = tickersData+exchangeRatesData+orderbooksData+tradesData+ohlcvData;
        
        elizaLogger.log("CCXT Provider get called: ", data);
        return "generate tweet about Tokens analysis by using these data and follow these rules. Rules: 1.Add $Token_name withour pairs when you mention the token in the tweet, for example $BMT instead of $BMT/USDT. 2.Add atleast 3 hashtags for the tweet, like #crypto, #blockchain, #$Token_name. Tickers data:" + tickersData 
        + "Exchange rates data:" + exchangeRatesData
        + "Orderbooks data:" + orderbooksData
        + "Trades data:" + tradesData
        + "OHLCV data:" + ohlcvData;
    }


}

export { ccxtProvider };