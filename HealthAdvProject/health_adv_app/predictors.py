import pickle
import sklearn

def diabetes_predictor(input_list):
    diabetes_prediction_model = pickle.load(open('static/ml_models/model_diabetes.pkl', 'rb'))
    return(diabetes_prediction_model.predict([input_list]))


def stroke_predictor(input_list):
    stroke_prediction_model = pickle.load(open('static/ml_models/model_stroke.pkl', 'rb'))
    return(stroke_prediction_model.predict([input_list]))
