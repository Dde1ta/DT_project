import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import classification_report


hea_m = LogisticRegression(max_iter=1000)
df = pd.read_csv("Model/Data/diabetesDataset.csv")
df.dropna(inplace=True)
train, test = np.split(df.sample(frac=1), [int(0.8 * len(df))])
train_x ,train_y = train[train.columns[1:-1]].values,train[train.columns[-1]].values
test_x,test_y = test[test.columns[1:-1]].values,test[test.columns[-1]].values
hea_m.fit(train_x,train_y)
p = hea_m.predict(test_x)
print(classification_report(test_y,p))