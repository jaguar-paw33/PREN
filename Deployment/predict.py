import tensorflow as tf
from tensorflow.python.framework.tensor_conversion_registry import get
from tensorflow.python.keras.saving.save import load_model
from model import model
from preprocess import *
from label_handler import *

def predict_label(path):

    image = preprocess(path)

    label = tf.argmax(model.get_prediction(image), axis=2)
    
    prediction = label_handler.decode(label)[0]

    return prediction