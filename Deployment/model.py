import tensorflow as tf
tf.get_logger().setLevel('INFO')

class model:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path, compile=False)

    def get_prediction(self, image):
        return self.model.predict(image)

model = model('final_model')