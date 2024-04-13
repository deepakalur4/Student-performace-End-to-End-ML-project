from src.logger import logging
from src.exception import Custom_exception
from dataclasses import  dataclass
import pandas as pd
import numpy as np
import sys
import os
from sklearn.model_selection import train_test_split
from data_transformation import * 


@dataclass
class dataingestionconfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")

class data_ingestion:
    def __init__(self):
        self.data_ingestion=dataingestionconfig()

    def initiate_dataingestion(self):
        try:
            logging.info("data ingestion part stared")

            df=pd.read_csv("src/notebooks/data/stud.csv")

            logging.info("read the csv data set as dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion.raw_data_path,header=True,index=False)

            logging.info("Starting a train and test split")

            train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)

            train_df.to_csv(self.data_ingestion.train_data_path,header=True,index=False)
            test_df.to_csv(self.data_ingestion.test_data_path,header=True,index=False)

            return(
                self.data_ingestion.train_data_path,self.data_ingestion.test_data_path
            )
        except Exception as e:
            raise Custom_exception(e,sys)
        
if __name__=="__main__":
    obj=data_ingestion()
    traindf,testdf=obj.initiate_dataingestion()
    obj2=data_transformation()
    obj2.initiaate_data_transformation(traindf,testdf)
    # print(traindf,testdf)



