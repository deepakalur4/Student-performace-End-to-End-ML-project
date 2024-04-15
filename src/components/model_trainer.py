from src.logger import logging
from src.exception import Custom_exception
from dataclasses import dataclass
import os
from src.utils import evaluate_model
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
import sys
from src.utils import save_object

@dataclass
class model_trainer_config:
    model_pickle_file=os.path.join("artifacts","model.pkl")

class model_trainer:
    def __init__(self):
        self.model_trainer=model_trainer_config()
    
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("Model_training_started")
            X_train,Y_train,X_test,Y_test=(train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "greadient bossting":GradientBoostingRegressor()
            }

            model_score=evaluate_model(x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test,model=models)
            max_score=(max(model_score.values()))
            best_model=([i[0] for i  in model_score.items() if i[1]==max_score])

            model_1=models[best_model[0]]

            y_pred=model_1.predict(X_test)

            save_object(filepath=self.model_trainer.model_pickle_file,obj=model_1)
            

            return r2_score(Y_test,y_pred)


        except Exception as e:
            raise Custom_exception(e,sys)