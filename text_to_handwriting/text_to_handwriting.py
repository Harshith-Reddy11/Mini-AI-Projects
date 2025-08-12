from PIL import Image, ImageDraw, ImageFont

text = input("📝 Enter the text you want to convert to handwriting: ")
output_file = "handwriting_output.png"

# Download a handwriting font (e.g., 'Dancing Script', 'Pacifico', or any .ttf file)
font_path = "handwriting.ttf"  # Place your .ttf font file in the same folder

font_size = 32
img = Image.new('RGB', (800, 200), color='white')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
draw.text((10, 50), text, font=font, fill='black')

img.save(output_file)
print(f"✅ Handwriting image saved as {output_file}")