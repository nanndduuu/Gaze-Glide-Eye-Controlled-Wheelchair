import tensorflow as tf
import numpy as np
import cv2  # If using camera input

# Load the trained model
model = tf.keras.models.load_model(my_model.h5)

# Function to process input image
def preprocess_input(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Modify based on model requirements
    img = cv2.resize(img, (64, 64))  # Resize to match the model's input shape
    img = img.astype(float32)  255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Take an input image and predict output
def predict(image_path)
    input_data = preprocess_input(image_path)
    prediction = model.predict(input_data)
    return prediction

# Example usage
if __name__ == __main__
    image_path = test_image.jpg  # Replace with your test image
    result = predict(image_path)
    print(Model Output, result)
