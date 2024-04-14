from src.exception import Custom_exception
from src.logger import logging
from sklearn.ensemble import (RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor)
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import sys
from dataclasses import dataclass
import os
from src.utils import evaluate_model
from src.utils import save_object
from sklearn.metrics import r2_score

@dataclass
class modeltrainerconfig:
    trained_model_file=os.path.join("artifacts","model.pkl")

class model_trainer:
    def __init__(self):
        self.model_trainer=modeltrainerconfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Model training has started")
            X_train,Y_train,X_test,Y_test=(train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])


            models= {
                "RandomForest": RandomForestRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "LinearRegression": LinearRegression(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "Gradientboostingregressor":GradientBoostingRegressor()
            }

            models_Score=evaluate_model(x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test,model=models)

            a=(max(models_Score.values()))
            b=[i[0] for i in models_Score.items() if i[1]==a]
            best_model=models[b[0]]

            save_object(filepath=self.model_trainer.trained_model_file,obj=best_model)

            y_pred=best_model.predict(X_test)
            
            r22_score=r2_score(Y_test,y_pred)

            return r22_score


        except Exception as e:
            raise Custom_exception(e,sys)


