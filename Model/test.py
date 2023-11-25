from preparingModels import Models
from sklearn.preprocessing import StandardScaler,LabelEncoder
import numpy as np
scaler = StandardScaler()
option_file = "options.json"
model = Models(option_file).load_models()
sample = np.array([30,1,4,30,152,0,2,109,0,2.4,2,3,3]).reshape(1,-1)
print(model[1].predict(sample))