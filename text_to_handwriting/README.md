# ✍️ Text to Handwriting Python Project

Convert your typed text into a handwriting-style image using Python and Pillow!  
This project supports multi-line text, dynamic image sizing, and custom handwriting fonts.

---

## ✨ Features

- 📝 Converts text to a handwriting-style image
- 📏 Automatically wraps text and adjusts image height
- 🖋️ Uses any handwriting-style `.ttf` font
- 🎨 Easy to customize font size, colors, and output file name
- 🚫 Handles long text gracefully

---

## 🛠 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)

Install Pillow with:

```
pip install pillow
```

---

## 🚀 Usage

1. **Download a handwriting-style `.ttf` font**

   - Example: [Dancing Script](https://fonts.google.com/specimen/Dancing+Script) or [Pacifico](https://fonts.google.com/specimen/Pacifico)
   - Save the font file as `handwriting.ttf` in your project folder

2. **Run the script:**

   ```
   python text_to_handwriting.py
   ```

3. **Enter your text when prompted.**

4. **Check your folder for `handwriting_output.png`.**

---

## ⚙️ Customization

- Change `font_size`, `img_width`, or colors in the script for different styles.
- Use any `.ttf` font by updating the `font_path`.

---

## 📜 License

This project is for educational and personal use.
