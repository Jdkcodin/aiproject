from PIL import Image, ImageDraw

# Load the certificate template
TEMPLATE_PATH = "static/WhatsApp Image 2025-04-11 at 21.25.01_e4b0b716.jpg"
OUTPUT_PATH = "static/grid_overlay.png"

img = Image.open(TEMPLATE_PATH)
draw = ImageDraw.Draw(img)

# Draw grid lines at every 100 pixels
for x in range(0, img.width, 100):
    draw.line([(x, 0), (x, img.height)], fill="red", width=2)
for y in range(0, img.height, 100):
    draw.line([(0, y), (img.width, y)], fill="red", width=2)

# Save the image with the grid overlay
img.save(OUTPUT_PATH)

print(f"Grid image saved at: {OUTPUT_PATH}")
