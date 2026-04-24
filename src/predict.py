import numpy as np

def predict(model, input_data):
    input_array = np.array(input_data).reshape(1, -1)
    result = model.predict(input_array)

    return "Addicted" if result[0] == 1 else "Not Addicted"
