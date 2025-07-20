import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image

class_names = ['Front Breakage', 'Front Crushed', 'Front Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']


# Define the model architecture
class CarClassifierResNet(nn.Module):
    def __init__(self, num_classes=6):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')

        # Freeze all layers
        for param in self.model.parameters():
            param.requires_grad = False

        # Unfreeze the last block and FC
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        # Modify the final fully connected layer
        self.model.fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)


# Prediction function
def predict(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)

    # Load model
    model = CarClassifierResNet()
    model.load_state_dict(torch.load("saved_model.pth", map_location=torch.device("cpu")))
    model.eval()

    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
        return class_names[predicted.item()]
