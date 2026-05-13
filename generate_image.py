import os
from openai import OpenAI
from pathlib import Path
import base64

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = (
    "A photorealistic glass squeeze bottle shaped like a classic ketchup bottle, "
    "filled with thick, glossy purple meat sauce. The bottle has no label, "
    "no logo, no text — completely blank glass. Soft studio lighting, "
    "white background, high detail, appetizing food photography style."
)

result = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="hd",
    n=1,
    response_format="b64_json",
)

image_b64 = result.data[0].b64_json
out = Path("purple_sauce_bottle.png")
out.write_bytes(base64.b64decode(image_b64))
print(f"Saved: {out.resolve()}")
