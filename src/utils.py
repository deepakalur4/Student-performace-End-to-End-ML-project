import pickle
from src.exception import Custom_exception
from src.logger import logging
import sys
import os
from sklearn.metrics import r2_score

def save_object(filepath,obj):
    try:
        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
        raise Custom_exception(e,sys)
    
    
def evaluate_model(x_train,y_train,x_test,y_test,model):
    try:
        score=dict()
        for i in model.items():
            ML_model=i[1]
            ML_model.fit(x_train,y_train)
            y_pred=ML_model.predict(x_test)
            train_model_Score=r2_score(y_test,y_pred)
            score[i[0]]=train_model_Score

        return score
    except Exception as e:
        raise Custom_exception(e,sys)
    

        
            



