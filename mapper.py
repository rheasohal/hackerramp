import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import torch.nn.functional as F

# Load the pre-trained ResNet50 model
model = models.resnet50(pretrained=True)

# Remove the final classification layer to get feature vectors
model = nn.Sequential(*list(model.children())[:-1])

# Set the model to evaluation mode
model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

#Transformer model

def get_image_embedding(img_path):
    # Load and preprocess the image
    img = Image.open(img_path).convert('RGB')
    img_tensor = preprocess(img)
    img_tensor = img_tensor.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        embedding = model(img_tensor)

    # Flatten the embedding to a 1D tensor
    embedding = embedding.flatten().numpy()
    return embedding

#cosine

def cosine_similarity(embedding1, embedding2):
    embedding1 = torch.tensor(embedding1, dtype=torch.float32)
    embedding2 = torch.tensor(embedding2, dtype=torch.float32)
    return F.cosine_similarity(embedding1, embedding2, dim=0).item()
