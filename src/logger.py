import logging
from datetime import datetime
import os

log_file_path=f"{datetime.now().strftime("%m_%d_%y_%H_%M_%S")}.log"
make_log_dir=os.path.join(os.getcwd(),"logs",log_file_path)

os.makedirs(make_log_dir,exist_ok=True)

log_path=os.path.join(make_log_dir,log_file_path)


logging.basicConfig(filename=log_path,level=logging.INFO)

