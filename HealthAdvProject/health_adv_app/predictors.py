import pickle

def diabetes_predictor(input_list):
    diabetes_prediction_model = pickle.load(open('static/ml_models/model_diabetes.pkl', 'rb'))
    return(diabetes_prediction_model.predict([input_list]))
