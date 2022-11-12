import logging

CHANNEL_NAME = '#iss-alerts'

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('logs/iss_logs.log', 'a', 'utf-8')],
    format="LEVEL===%(levelname)s TIMESTAMP===%(asctime)s TEXT===%(message)s"
)

logger = logging.getLogger('iss_logger')
