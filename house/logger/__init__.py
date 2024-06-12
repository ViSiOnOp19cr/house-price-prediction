import logging 
import os

from from_root import from_root
from datetime import datetime

LOG_FILE= f"{datetime.now().strfile('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'
#from_root returns root directory

logs_path = os.path.join(from_root(),log_dir,LOG_FILE)


os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    #asctime - gives date and time
    #name - name of logger that generated log message
    #levelname - inserts sevirity level of log (debug,info,warning,error,critical)
    #message - inserts actual log message
    level = logging.DEBUG
)