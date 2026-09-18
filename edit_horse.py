from PIL import Image, ImageEnhance, ImageFilter
import sys

# Get filename from command line or use default
if len(sys.argv) > 1:
    img_path = sys.argv[1]
else:
    img_path = "ec64d958-a8f4-4213-bb5d-a17e94606b99.jpeg"

try:
    img = Image.open(img_path).convert("L")  # Open as Grayscale
except FileNotFoundError:
    print(f"Error: File '{img_path}' not found.")
    print("Make sure the file is in the same folder as this script.")
    sys.exit(1)

# --- 1. ENHANCE LINES (Darken + Sharpen) ---
# Increase contrast first
enhancer = ImageEnhance.Contrast(img)
enhanced = enhancer.enhance(3.0)  # Boost contrast by 3x

# Sharpen the image
sharpened = enhanced.filter(ImageFilter.SHARPEN)

# Darken the lines further by adjusting brightness
enhancer2 = ImageEnhance.Brightness(sharpened)
final = enhancer2.enhance(0.8)  # Make it slightly darker

# --- 2. CROP EXTRA EDGES ---
# Find the bounding box of non-white pixels
# Convert to binary: 0 for white, 1 for dark
binary = final.point(lambda x: 255 if x > 20 else 0)

# Get all pixel coordinates where pixel is not white (255)
width, height = binary.size
non_white = []
for y in range(height):
    for x in range(width):
        if binary.getpixel((x, y)) != 255:
            non_white.append((x, y))

if not non_white:
    print("No content found in image.")
    sys.exit(1)

# Calculate bounding box
min_x = min(p[0] for p in non_white)
min_y = min(p[1] for p in non_white)
max_x = max(p[0] for p in non_white)
max_y = max(p[1] for p in non_white)

# Add a small margin (10 pixels)
margin = 10
min_x = max(0, min_x - margin)
min_y = max(0, min_y - margin)
max_x = min(width, max_x + margin)
max_y = min(height, max_y + margin)

# Crop
cropped = final.crop((min_x, min_y, max_x, max_y))

# Save with your desired name
cropped.save("knabstrupper_horse.jpeg")
print("✅ Done! Saved as 'knabstrupper_horse.jpeg'")
