import pickle

def diabetes_predictor(input_list):
    diabetes_prediction_model = pickle.load(open('static/ml_models/model_diabetes.pkl', 'rb'))
    return(diabetes_prediction_model.predict([input_list]))


def stroke_predictor(input_list):
    stroke_prediction_model = pickle.load(open('static/ml_models/model_stroke.pkl', 'rb'))
    return(stroke_prediction_model.predict([input_list]))


def heart_disease_predictor(input_list):
    #make input list feasible for the model
    #input format = [age,sex,trestbps,chol,fbs,exang,cp,restecg]
    main_list = input_list[:6]
    for i in range(4):
        if input_list[6] == i:
            main_list.append(1)
        else:
            main_list.append(0)
    for i in range(3):
        if input_list[7] == i:
            main_list.append(1)
        else:
            main_list.append(0)
    heart_disease_prediction_model = pickle.load(open('static/ml_models/model_heart_disease.pkl', 'rb'))
    return(heart_disease_prediction_model.predict([main_list]))
