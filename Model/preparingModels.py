import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import json as j

class Models:
    def __init__(self,json_file):
        if not j.load(json_file)["Models"]:
            self.create_models()
        else:
            self.load_models()

    def load_data(self):
        dia_data = pd.read_csv("/Data/diabetesDataset.csv")
        heart_data = pd.read_csv("/Data/Heart_disease.csv")
        hep_data = pd.read_csv("/Data/hepatitis_csv.csv")
        return into_train_test([dia_data,heart_data,hep_data])

    def into_train_test(self,data_list):
        l = []
        for data in data_list:
            train, test = np.split(df.sample(frac=1), [int(0.8 * len(data))])
            l.append([train,test])
        return l

    def create_models(self):
        dia,hea,hep = self.load_models()
        dia_x,dia_y = dia[:-1].values,dia[-1].values
        hea_x,hea_y = hea[:-1].values,hea[-1].values
        hep_x,hep_y = hep[1:].values,hep[0].values

    def load_models(self):
        print("loading")

if __name__ == "__main__":
    json_file = open("options.json",'r+')
    models = Models(json_file)