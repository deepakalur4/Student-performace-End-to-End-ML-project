from src.exception import Custom_exception
from src.logger import logging
import pandas as pd
import os,sys
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import numpy as np
from src.utils import save_object

@dataclass
class datatransformationconfig:
    pickle_file_path=os.path.join("artifacts","preprocessor.pkl")

class data_transformation:
    def __init__(self):
        self.data_transformation=datatransformationconfig()

    def get_transformation_object(self):
        try:
            logging.info("Getting into get_transformation_object")
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline=Pipeline([(
                "Imputer",SimpleImputer(strategy="median")),("scaling",StandardScaler())])
            
            cat_pipeline=Pipeline([(
                "imputer",SimpleImputer(strategy="most_frequent")),("encoder",OneHotEncoder()),("scaling",StandardScaler(with_mean=False))])
            
            preprocessor_obj=ColumnTransformer([("num_features",num_pipeline,numerical_columns),("cat_features",cat_pipeline,categorical_columns)])

            return preprocessor_obj
        
        except Exception as e:
            raise Custom_exception(e,sys)
        
    def initiaate_data_transformation(self,train_ph,test_ph):
        try:
            logging.info("Initaiting data transformation")
            train_df=pd.read_csv(train_ph)
            test_df=pd.read_csv(test_ph)


            prprocsser_obj=self.get_transformation_object()

            target_column_name="math_score"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            input_feature_train_df_pre=prprocsser_obj.fit_transform(input_feature_train_df)
            input_feature_test_df_pre=prprocsser_obj.transform(input_feature_test_df)

            
            

            input_feature_train_df_arr=np.c_[input_feature_train_df_pre,np.array(target_feature_train_df)]
            input_feature_test_df_arr=np.c_[input_feature_test_df_pre,np.array(target_feature_test_df)]


            save_object(self.data_transformation.pickle_file_path,prprocsser_obj)


            return (input_feature_train_df_arr,input_feature_test_df_arr,self.data_transformation.pickle_file_path)
        
        except Exception as e:
            raise Custom_exception(e,sys)

        

