import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import logging
from dotenv import load_dotenv

from .ccxtBase import CCXTBase

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class CCXTProvider:
    def __init__(self):
        self.ccxt_client = CCXTBase()
        
        # Load configuration from environment variables
        self.MIN_VOLUME = float(os.getenv('MIN_VOLUME', 10000000))
        self.MIN_PRICE = float(os.getenv('MIN_PRICE', 0.00000100))
        self.MIN_PRICE_CHANGE = float(os.getenv('MIN_PRICE_CHANGE', 5.0))
        self.BATCH_SIZE = int(os.getenv('BATCH_SIZE', 50))
        self.MIN_ORDER_VALUE = float(os.getenv('MIN_ORDER_VALUE', 100000))
        self.MIN_TRADE_VALUE = float(os.getenv('MIN_TRADE_VALUE', 50000))
        self.MIN_ORDER_COUNT = int(os.getenv('MIN_ORDER_COUNT', 5))
        self.MAX_ORDERS = int(os.getenv('MAX_ORDERS', 100))
        self.MAX_TRADES = int(os.getenv('MAX_TRADES', 100))
        
        # Set up output directories from environment variables
        self.data_output_dir = Path(os.getenv('DATA_OUTPUT_DIR', '/home/mandes/Quant72/services/ccxtData/output'))
        self.md_output_dir = Path(os.getenv('MD_OUTPUT_DIR', '/home/mandes/Quant72/eliza/characters/knowledge/LucasTravers'))
        
        self.data_output_dir.mkdir(parents=True, exist_ok=True)
        self.md_output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Initialized CCXTProvider with:")
        logger.info(f"- Data output directory: {self.data_output_dir}")
        logger.info(f"- MD output directory: {self.md_output_dir}")
        logger.info(f"- Update interval: {os.getenv('UPDATE_INTERVAL', 30)} minutes")
        logger.info(f"- Min volume: {self.MIN_VOLUME}")
        logger.info(f"- Min price: {self.MIN_PRICE}")
        logger.info(f"- Min price change: {self.MIN_PRICE_CHANGE}%")

    async def fetch_and_save_market_data(self):
        """Fetch and save all market data"""
        try:
            await self.ccxt_client.initialize()
            timestamp = datetime.now().isoformat()

            # Fetch and save tickers
            logger.info("Fetching tickers...")
            tickers = await self.ccxt_client.fetch_tickers()
            filtered_tickers = self._filter_tickers(tickers)
            logger.info(f"Found {len(filtered_tickers)} significant pairs out of {len(tickers)} total pairs")
            
            await self._save_json_file("tickers.json", {
                "timestamp": timestamp,
                "total_pairs": len(tickers),
                "filtered_pairs": len(filtered_tickers),
                "data": filtered_tickers
            })
            await self._save_md_file("tickers.md", filtered_tickers, "Tickers")

            # Fetch and save exchange rates only for filtered tickers
            logger.info("Fetching exchange rates...")
            rates = await self._fetch_exchange_rates(filtered_tickers.keys())
            await self._save_json_file("exchange_rates.json", {
                "timestamp": timestamp,
                "total_pairs": len(rates),
                "data": rates
            })
            await self._save_md_file("exchange_rates.md", rates, "Exchange Rates")

            # Process other data in batches
            symbols = list(filtered_tickers.keys())
            for i in range(0, len(symbols), self.BATCH_SIZE):
                batch = symbols[i:i + self.BATCH_SIZE]
                logger.info(f"Processing batch {i//self.BATCH_SIZE + 1} of {(len(symbols) + self.BATCH_SIZE - 1)//self.BATCH_SIZE}")
                
                # Fetch batch data in parallel
                orderbooks, trades, ohlcv = await self._fetch_batch_data(batch)
                
                # Save the batch data
                await self._save_batch_data(timestamp, orderbooks, trades, ohlcv)

        except asyncio.CancelledError:
            logger.info("Operation was cancelled. Cleaning up...")
            raise
        except Exception as e:
            logger.error(f"Error in fetch_and_save_market_data: {e}")
            raise
        finally:
            await self.ccxt_client.close()

    async def _fetch_exchange_rates(self, symbols: List[str]) -> Dict:
        """Fetch exchange rates for filtered symbols"""
        rates = {}
        for symbol in symbols:
            try:
                await asyncio.sleep(0.1)  # Rate limiting
                ticker = await self.ccxt_client.fetch_ticker(symbol)
                if ticker:
                    rates[symbol] = {
                        'last': ticker.get('last'),
                        'bid': ticker.get('bid'),
                        'ask': ticker.get('ask'),
                        'volume': ticker.get('baseVolume'),
                        'percentage': ticker.get('percentage'),
                        'timestamp': ticker.get('timestamp')
                    }
            except Exception as e:
                logger.error(f"Error fetching rate for {symbol}: {e}")
        return rates

    async def _fetch_orderbooks(self, symbols: List[str]) -> Dict:
        """Fetch order books for a batch of symbols"""
        orderbooks = {}
        for symbol in symbols:
            try:
                await asyncio.sleep(0.1)  # Rate limiting
                orderbook = await self.ccxt_client.fetch_orderbook(symbol)
                if orderbook:
                    orderbooks[symbol] = orderbook
            except Exception as e:
                logger.error(f"Error fetching orderbook for {symbol}: {e}")
        return orderbooks

    async def _fetch_trades(self, symbols: List[str]) -> Dict:
        """Fetch trades for a batch of symbols"""
        trades = {}
        for symbol in symbols:
            try:
                await asyncio.sleep(0.1)  # Rate limiting
                trade_data = await self.ccxt_client.fetch_trades(symbol)
                if trade_data:
                    trades[symbol] = trade_data
            except Exception as e:
                logger.error(f"Error fetching trades for {symbol}: {e}")
        return trades

    async def _fetch_ohlcv(self, symbols: List[str]) -> Dict:
        """Fetch OHLCV data for a batch of symbols"""
        ohlcv_data = {}
        for symbol in symbols:
            try:
                await asyncio.sleep(0.1)  # Rate limiting
                ohlcv = await self.ccxt_client.fetch_ohlcv(symbol)
                if ohlcv:
                    ohlcv_data[symbol] = ohlcv
            except Exception as e:
                logger.error(f"Error fetching OHLCV for {symbol}: {e}")
        return ohlcv_data

    async def _save_batch_data(self, timestamp: str, orderbooks: Dict, trades: Dict, ohlcv: Dict):
        """Save batch data to files"""
        await self._save_json_file("orderbooks.json", {"timestamp": timestamp, "data": orderbooks})
        await self._save_md_file("orderbooks.md", orderbooks, "Order Books")
        
        await self._save_json_file("trades.json", {"timestamp": timestamp, "data": trades})
        await self._save_md_file("trades.md", trades, "Trades")
        
        await self._save_json_file("ohlcv.json", {"timestamp": timestamp, "data": ohlcv})
        await self._save_md_file("ohlcv.md", ohlcv, "OHLCV Data")

    def _filter_tickers(self, tickers: Dict) -> Dict:
        """Filter tickers based on volume, price, and price change"""
        filtered_tickers = {}
        for symbol, ticker in tickers.items():
            if (ticker.get('quoteVolume', 0) >= self.MIN_VOLUME and 
                ticker.get('last', 0) >= self.MIN_PRICE):
                
                price_change_pct = ticker.get('percentage', 0)
                if price_change_pct is not None and abs(price_change_pct) >= self.MIN_PRICE_CHANGE:
                    filtered_tickers[symbol] = ticker

        return filtered_tickers

    async def _save_json_file(self, filename: str, data: Dict):
        """Save JSON file with proper error handling"""
        try:
            file_path = self.data_output_dir / filename
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            logger.info(f"Saved {filename} to {file_path}")
        except Exception as e:
            logger.error(f"Error saving {filename}: {e}")

    async def _save_md_file(self, filename: str, data: Dict, title: str):
        """Save markdown file with market data"""
        try:
            file_path = self.md_output_dir / filename
            with open(file_path, 'w') as f:
                f.write(f"# {title}\n\n")
                for key, value in data.items():
                    f.write(f"## {key}\n")
                    f.write(f"{json.dumps(value, indent=2)}\n\n")
            logger.info(f"Saved {filename} to {file_path}")
        except Exception as e:
            logger.error(f"Error saving {filename}: {e}")

    async def _fetch_batch_data(self, batch: List[str]) -> tuple[Dict, Dict, Dict]:
        """Fetch order books, trades, and OHLCV data for a batch of symbols in parallel"""
        orderbooks = {}
        trades = {}
        ohlcv_data = {}
        
        async def fetch_symbol_data(symbol: str):
            try:
                await asyncio.sleep(0.1)  # Rate limiting
                orderbook = await self.ccxt_client.fetch_orderbook(symbol)
                trade_data = await self.ccxt_client.fetch_trades(symbol)
                ohlcv = await self.ccxt_client.fetch_ohlcv(symbol)
                
                # Apply filters
                filtered_orderbook = self._filter_orderbook(orderbook)
                filtered_trades = self._filter_trades(trade_data)
                
                return symbol, filtered_orderbook, filtered_trades, ohlcv
            except Exception as e:
                logger.error(f"Error fetching data for {symbol}: {e}")
                return symbol, {}, [], []

        # Fetch data for all symbols in parallel
        results = await asyncio.gather(*[fetch_symbol_data(symbol) for symbol in batch])
        
        # Process results
        for symbol, orderbook, trade_data, ohlcv in results:
            if orderbook:  # Only store if there are significant orders
                orderbooks[symbol] = orderbook
            if trade_data:  # Only store if there are significant trades
                trades[symbol] = trade_data
            if ohlcv:
                ohlcv_data[symbol] = ohlcv

        return orderbooks, trades, ohlcv_data

    def _filter_orderbook(self, orderbook: Dict) -> Dict:
        """Filter significant orders from orderbook"""
        if not orderbook:
            return {}
            
        filtered_bids = []
        filtered_asks = []

        # Filter bids
        for price, amount in orderbook.get('bids', []):
            order_value = price * amount
            if order_value >= self.MIN_ORDER_VALUE:
                filtered_bids.append([price, amount])

        # Filter asks
        for price, amount in orderbook.get('asks', []):
            order_value = price * amount
            if order_value >= self.MIN_ORDER_VALUE:
                filtered_asks.append([price, amount])

        # Only return if we have enough significant orders
        if len(filtered_bids) + len(filtered_asks) >= self.MIN_ORDER_COUNT:
            return {
                'bids': filtered_bids[:self.MAX_ORDERS],
                'asks': filtered_asks[:self.MAX_ORDERS],
                'timestamp': orderbook.get('timestamp')
            }
        return {}

    def _filter_trades(self, trades: List[Dict]) -> List[Dict]:
        """Filter significant trades"""
        if not trades:
            return []
            
        filtered_trades = []
        for trade in trades:
            price = trade.get('price', 0)
            amount = trade.get('amount', 0)
            trade_value = price * amount
            
            if trade_value >= self.MIN_TRADE_VALUE:
                filtered_trades.append(trade)

        return filtered_trades[:self.MAX_TRADES] 
        