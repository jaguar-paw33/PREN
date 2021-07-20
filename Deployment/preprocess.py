import tensorflow as tf
from utils import *

def preprocess(path):

    image_string = tf.io.read_file(path)
    image = tf.image.decode_image(image_string, channels=1, dtype=tf.float32, expand_animations=False)
    image = tf.image.resize(image, [img_height, img_width])
    image = tf.image.grayscale_to_rgb(image)
    image = tf.expand_dims(image, axis=0)
    
    return image