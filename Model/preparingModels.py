import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import classification_report
import json as j
from joblib import load,dump

class Models:
    def __init__(self,json_file):
        json_file_r = open(json_file,'r')
        in_file = j.load(json_file_r)
        json_file_w = open(json_file,'w')
        if not in_file["Models"]:
            self.save_models()
            in_file["Models"] = True
            j.dump(in_file,json_file_w)
        else:
            j.dump(in_file, json_file_w)
            self.models = self.load_models()

    def load_data(self):
        dia_data = pd.read_csv("Data/diabetesDataset.csv")
        heart_data = pd.read_csv("Data/Heart_disease.csv")
        hep_data = pd.read_csv("Data/hepatitis_csv.csv")
        dia_data = dia_data.dropna()
        heart_data = heart_data.dropna()
        hep_data = hep_data.dropna()
        print("Loaded_data")
        return [dia_data,heart_data,hep_data]

    def into_train_test(self,data_list):
        l = []
        for data in data_list:
            train, test = np.split(df.sample(frac=1), [int(0.8 * len(data))])
            l.append([train,test])
        print("split_data")
        return l

    def create_models(self):
        dia,hea,hep = self.load_data()
        dia_x,dia_y = dia[dia.columns[1:-1]].values,dia[dia.columns[-1]].values
        hea_x,hea_y = hea[hea.columns[1:-1]].values,hea[hea.columns[-1]].values
        hep_x,hep_y = hep[hep.columns[1:-1]].values,hep[hep.columns[-1]].values
        scaler = StandardScaler()
        encoder = LabelEncoder()
        # dia_x = pd.DataFrame(scaler.fit_transform(dia_x))
        # hea_x = pd.DataFrame(scaler.fit_transform(hea_x))
        # hep_x = pd.DataFrame(scaler.fit_transform(hep_x))
        dia_m = LogisticRegression(max_iter=1000)
        hea_m = LogisticRegression(max_iter=1000)
        hep_m = LogisticRegression(max_iter=1000)
        dia_m.fit(dia_x,dia_y)
        print("trained")
        hea_m.fit(hea_x,hea_y)
        print("trained")
        hep_m.fit(hep_x,hep_y)
        print("trained")
        return [dia_m,hea_m,hep_m]

    def save_models(self):
        dic = open("models/models.joblib",'wb')
        dump(self.create_models(),dic)

    def load_models(self):
        return load("models\models.joblib")

if __name__ == "__main__":
    json_file = "options.json"
    models = Models(json_file)