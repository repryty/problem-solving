import random
from PIL import Image

def generate_random_noise():
    # Initialize the seed with a random value
    seed = random.random()
    random.seed(seed)

    # Generate random black and white noise
    noise = []
    for _ in range(250):
        row = []
        for _ in range(250):
            # Get the previous pixel's result as the new seed
            seed = random.random()
            random.seed(seed)

            pixel = random.choice([0, 255])
            row.append(pixel)
        noise.append(row)

    return noise

# Example usage
random_noise = generate_random_noise()

# Create a PIL image from the noise data
image = Image.new("L", (255, 255))
image.putdata([pixel for row in random_noise for pixel in row])

# Display the image
image.show()