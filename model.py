from diffusers import StableDiffusionPipeline
from transformers import CLIPTextModel, CLIPTokenizer
from datasets import load_dataset
import torch, os
from torch import autocast
from tqdm import tqdm

# Define the path to your dataset and the prompts for each shape
data_path = "/Users/manvi11/Downloads/Dataset"
prompts = {
    "PS": "A pear-shaped engagement ring with a unique and elegant look",
    "CC": "A cushion cut engagement ring with a romantic and timeless design",
    "PR": "A princess cut engagement ring with a sophisticated design",
    "OV": "An oval cut engagement ring with a delicate band",
    "MQ": "A marquise cut engagement ring with a luxurious setting",
    "EM": "An emerald cut engagement ring with a vintage style",
    "RD": "A round engagement ring with a classic design",
    "RA": "A radiant cut engagement ring with a modern touch",
}

# Define hyperparameters
batch_size = 1
num_epochs = 1
learning_rate = 1e-4

# Load pre-trained Stable Diffusion model and tokenizer
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe
text_encoder = CLIPTextModel.from_pretrained(model_id, subfolder="text_encoder")
tokenizer = CLIPTokenizer.from_pretrained(model_id, subfolder="tokenizer")

# Define a function to prepare the dataset
def prepare_dataset():
    images = []
    captions = []
    for shape, prompt in prompts.items():
        image_folder = f"{data_path}/{shape}"
        for image_file in os.listdir(image_folder):
            image_path = os.path.join(image_folder, image_file)
            images.append(image_path)
            captions.append(prompt)
    return images, captions

# Get the images and captions
image_paths, captions = prepare_dataset()

# Tokenize the captions
inputs = tokenizer(captions, padding="max_length", max_length=tokenizer.model_max_length, truncation=True, return_tensors="pt")
input_ids = inputs.input_ids

# Fine-tune the model
text_encoder.train()
optimizer = torch.optim.AdamW(text_encoder.parameters(), lr=learning_rate)
for epoch in range(num_epochs):
    for i in tqdm(range(0, len(image_paths), batch_size)):
        batch_input_ids = input_ids[i:i+batch_size]
        with torch.no_grad():  # No need for autocast since we don't use CUDA
            text_embeddings = text_encoder(batch_input_ids)[0]
            # Additional training code to update the model using the text_embeddings and the images

        # Update model parameters
        optimizer.zero_grad()
        # loss.backward()
        optimizer.step()

# Save the fine-tuned model
pipe.save_pretrained("/Users/manvi11/Downloads/Dataset/fineTuned")
