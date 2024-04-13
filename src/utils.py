import pickle
from src.exception import Custom_exception
from src.logger import logging
import sys
import os

def save_object(filepath,obj):
    try:
        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
        raise Custom_exception(e,sys)