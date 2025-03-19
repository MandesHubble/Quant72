import asyncio
import logging
import signal
import os
from datetime import datetime
from dotenv import load_dotenv
from src.ccxtProvider import CCXTProvider

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global flag for controlling the update loop
running = True

def handle_shutdown(signum, frame):
    """Handle shutdown signals gracefully"""
    global running
    logger.info("Received shutdown signal. Cleaning up...")
    running = False

async def fetch_market_data():
    """Fetch and save market data"""
    provider = CCXTProvider()
    try:
        logger.info("Fetching market data...")
        await provider.fetch_and_save_market_data()
        logger.info("Market data collection completed successfully!")
    except asyncio.CancelledError:
        logger.info("Market data collection was cancelled.")
    except Exception as e:
        logger.error(f"Error fetching market data: {e}")
    finally:
        # Ensure resources are properly closed
        try:
            await provider.ccxt_client.close()
        except Exception as e:
            logger.error(f"Error closing CCXT client: {e}")

async def scheduled_updates():
    """Run market data updates at specified intervals"""
    global running
    
    # Get update interval from environment variable (default to 30 minutes)
    interval_minutes = int(os.getenv('UPDATE_INTERVAL', 30))
    logger.info(f"Starting scheduled updates every {interval_minutes} minutes")
    
    while running:
        start_time = datetime.now()
        logger.info(f"Starting market data update at {start_time}")
        
        try:
            await fetch_market_data()
        except Exception as e:
            logger.error(f"Error in scheduled update: {e}")
        
        if not running:
            break
            
        # Calculate sleep time for next update
        elapsed = (datetime.now() - start_time).total_seconds()
        sleep_time = max(0, interval_minutes * 60 - elapsed)
        
        logger.info(f"Next update in {sleep_time/60:.2f} minutes")
        try:
            await asyncio.sleep(sleep_time)
        except asyncio.CancelledError:
            break

if __name__ == "__main__":
    # Register signal handlers
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    
    try:
        # Run the scheduled updates
        asyncio.run(scheduled_updates())
    except KeyboardInterrupt:
        logger.info("Program interrupted by user.")
    finally:
        logger.info("Shutting down...")