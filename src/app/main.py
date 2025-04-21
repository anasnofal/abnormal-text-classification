from fastapi import FastAPI
from app.Schema import Request
import ktrain
import pickle

# loading preprocess and model file
app = FastAPI()

pickle_in = open('models/englishpipeline.pickle', 'rb')
classifier_en = pickle.load(pickle_in)
predictor = ktrain.load_predictor('models/arabic model')


@app.post('/predict')
def classify(data: Request):
    text = data.post_body
    lan = data.post_languages
    if lan == 'en':
        prediction = classifier_en.predict([text])
        if prediction[0] == 0:
            prediction = "normal"
        elif prediction[0] == 1:
            prediction = "offensive"
        elif prediction[0] == 2:
            prediction = 'spam'
        elif prediction[0] == 3:
            prediction = 'profane'
    else:
        prediction = predictor.predict([text])
        if prediction[0] == 0:
            prediction = "normal"
        elif prediction[0] == 1:
            prediction = "offensive"
        elif prediction[0] == 2:
            prediction = 'spam'
        elif prediction[0] == 3:
            prediction = 'profane'

    return {
        'prediction': prediction
    }
