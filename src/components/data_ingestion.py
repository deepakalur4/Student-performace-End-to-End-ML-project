from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
import os
import sys
from dataclasses import dataclass
import pandas as pd


@dataclass
class dataingestionconfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")


class dataingestion:
    def __init__(self):
        self.dataingestion=dataingestionconfig()

    def initiate_dataingestion(self):
        logging.info("Entered the method of data ingestion block")
        try:
            df=pd.read_csv("notebooks/stud.csv")
            logging.info("Loaded the csv file as a dataframe")
            
            os.makedirs(os.path.dirname(self.dataingestion.train_data_path),exist_ok=True)

            df.to_csv(self.dataingestion.raw_data_path,header=True,index=False)

            logging.info("Starting a train and test split")

            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.dataingestion.train_data_path,header=True,index=False)

            test_data.to_csv(self.dataingestion.test_data_path,header=True,index=False)

            logging.info("Train_test split done")

            return (
                    self.dataingestion.train_data_path,
                    self.dataingestion.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=dataingestion()
    train_arr,test_arr=obj.initiate_dataingestion()