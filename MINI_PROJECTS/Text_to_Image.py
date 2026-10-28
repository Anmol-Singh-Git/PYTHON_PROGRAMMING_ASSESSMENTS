import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompt = "A beautiful house surrounded by green trees"

image = pipe(prompt).images[0]

image.save("generated_image.png")

print("Image generated successfully!")
