import logging
import logging.handlers
from datetime import datetime
import os
import pandas as pd

import requests

now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = "Checking this line of code"
except KeyError:
    SOME_SECRET = "Token not available!"

df_out = pd.DataFrame()
df_out[['Date','Message']] = [[formatted_date_time,'File added']]


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    logger.info(f"Data appended to the file - {formatted_date_time}")
    SOME_SECRET = "Checking this line of code"
    df_out.to_csv('Final_Output/output.csv',index=False)



