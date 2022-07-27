import tensorflow as tf
from keras_preprocessing.sequence import pad_sequences
import pickle



def decode_sentiment(score):
    if score < 0.5:
        label = "NEGATIVE"

        return label
    else:
        label = "POSITIVE"

        return label
    
def predict(text):
    model = tf.keras.models.load_model('GLOVE_LSTM_traite')
    tokenizer = pickle.load(open('tokenizer_GLOVE_LSTM_traite.pkl', "rb"))
    
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]),
                           maxlen=30)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score)
    label = text + ': ' + label
    return label