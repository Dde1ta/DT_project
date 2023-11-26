from Model.preparingModels import Models
from sklearn.preprocessing import StandardScaler
import numpy as np
scaler = StandardScaler()
option_file = "Model/options.json"
model = Models(option_file).load_models()
sample = np.array([0,1,2,1,2,2,3,4,5,1]).reshape(1,-1)
print(model[2].predict(sample))