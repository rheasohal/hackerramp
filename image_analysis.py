import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import io
import requests

# Load the pre-trained VGG16 model + higher level layers
model = VGG16(weights='imagenet', include_top=False)

def analyze_images(image_url):
    try:
        # Download image from URL
        img_data = requests.get(image_url).content

        # Load and preprocess image for VGG16
        img = image.load_img(io.BytesIO(img_data), target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        # Extract features using VGG16
        features = model.predict(img)

        # Flatten features and convert to list
        flattened_features = features.flatten().tolist()

        return flattened_features

    except Exception as e:
        print(f"Error analyzing image: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    # Example image URL
    image_url = 'https://example.com/image.jpg'
    embedding = analyze_images(image_url)
    if embedding:
        print(f"Embedding for image {image_url}: {embedding}")
    else:
        print(f"Failed to analyze image {image_url}")
