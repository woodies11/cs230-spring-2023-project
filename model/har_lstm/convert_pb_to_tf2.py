import os
import tensorflow as tf

# Get the path to the frozen model
script_dir = os.path.dirname(os.path.abspath(__file__))
frozen_graph_path = os.path.join(script_dir, 'frozen_model.pb')

# Load the frozen graph
loaded_model = tf.saved_model.load(frozen_graph_path)

# Convert the loaded model to a TensorFlow 2.x model
model = tf.keras.models.Sequential()
model.add(loaded_model.signatures['serving_default'])

# Optional: Print the model summary
model.summary()
