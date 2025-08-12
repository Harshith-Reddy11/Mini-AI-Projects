from PIL import Image, ImageDraw, ImageFont


def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and font.getlength(line + words[0] + ' ') <= max_width:
            line += words.pop(0) + ' '
        lines.append(line.strip())
    return lines


text = input("📝 Enter the text you want to convert to handwriting: ")
output_file = "handwriting_output.png"
font_path = "handwriting.ttf"  # Place your .ttf font file in the same folder
font_size = 32
img_width = 800
margin = 10

font = ImageFont.truetype(font_path, font_size)
lines = wrap_text(text, font, img_width - 2 * margin)
line_height = font_size + 10
img_height = line_height * len(lines) + 2 * margin

img = Image.new('RGB', (img_width, img_height), color='white')
draw = ImageDraw.Draw(img)

y = margin
for line in lines:
    draw.text((margin, y), line, font=font, fill='black')
    y += line_height

img.save(output_file)
print(f"✅ Handwriting image saved as {output_file}")
