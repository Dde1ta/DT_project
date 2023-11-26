from preparingModels import Models
from sklearn.preprocessing import StandardScaler,LabelEncoder
import numpy as np
scaler = StandardScaler()
option_file = "options.json"
model = Models(option_file).load_models()
sample = np.array([]).reshape(1,-1)
print(model[0].predict(sample))