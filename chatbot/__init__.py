import logging.config

import concurrent_log_handler  # pyright: ignore # noqa F401
import dotenv

from chatbot.env import CURRENT_ENV, Env

dotenv.load_dotenv()

logging.config.fileConfig(
    "./log.dev.conf" if CURRENT_ENV is Env.DEV else "./log.conf",
    disable_existing_loggers=False,
)
