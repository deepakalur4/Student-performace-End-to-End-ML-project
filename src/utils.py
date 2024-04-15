import pickle
from src.exception import Custom_exception
from src.logger import logging
import sys
import os
from sklearn.metrics import r2_score

def save_object(filepath,obj):
    try:
        with open(filepath,"wb") as file_obj:
            return pickle.dump(obj,file_obj)
        
    except Exception as e:
        raise Custom_exception(e,sys)
    
    
def evaluate_model(x_train,y_train,x_test,y_test,model):
    try:
        score=dict()
        for i in model.items():
            model=i[1]
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            score[i[0]]=r2_score(y_test,y_pred)

        return (score)
    except Exception as e:
        raise Custom_exception(e,sys)    


def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj_1:
            return pickle.load(file_obj_1)   

    except Exception as e:
        raise Custom_exception(e,sys)    
  


        
            



