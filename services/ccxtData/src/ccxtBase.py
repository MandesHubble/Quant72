import ccxt.async_support as ccxt
import asyncio
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class CCXTBase:
    def __init__(self):
        self.exchange = ccxt.binance({
            'enableRateLimit': True,
            'options': {
                'defaultType': 'spot'
            },
            'timeout': 30000,  # 30 seconds timeout
            'rateLimit': 1000,  # Rate limit in milliseconds
        })

    async def initialize(self):
        """Initialize the exchange and load markets"""
        try:
            await self.exchange.load_markets()
            logger.info(f"Initialized {self.exchange.id} exchange with {len(self.exchange.markets)} markets")
        except Exception as e:
            logger.error(f"Error initializing exchange: {e}")
            raise

    async def fetch_tickers(self) -> Dict:
        """Fetch ticker data for all markets"""
        try:
            tickers = await self.exchange.fetch_tickers()
            return tickers
        except Exception as e:
            logger.error(f"Error fetching tickers: {e}")
            return {}

    async def fetch_ticker(self, symbol: str) -> Dict:
        """Fetch ticker for a specific symbol"""
        try:
            ticker = await self.exchange.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            logger.error(f"Error fetching ticker for {symbol}: {e}")
            return {}

    async def fetch_orderbook(self, symbol: str) -> Dict:
        """Fetch order book for a specific symbol"""
        try:
            orderbook = await self.exchange.fetch_order_book(symbol)
            return orderbook
        except Exception as e:
            logger.error(f"Error fetching orderbook for {symbol}: {e}")
            return {}

    async def fetch_trades(self, symbol: str) -> List[Dict]:
        """Fetch recent trades for a specific symbol"""
        try:
            trades = await self.exchange.fetch_trades(symbol)
            return trades
        except Exception as e:
            logger.error(f"Error fetching trades for {symbol}: {e}")
            return []

    async def fetch_ohlcv(self, symbol: str, timeframe: str = '1d') -> List[Dict]:
        """Fetch OHLCV data for a specific symbol"""
        try:
            ohlcv = await self.exchange.fetch_ohlcv(symbol, timeframe)
            return ohlcv
        except Exception as e:
            logger.error(f"Error fetching OHLCV for {symbol}: {e}")
            return []

    async def close(self):
        """Close the exchange connection"""
        try:
            await self.exchange.close()
            logger.info("Closed exchange connection")
        except Exception as e:
            logger.error(f"Error closing exchange connection: {e}")