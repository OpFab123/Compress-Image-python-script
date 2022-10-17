import PIL
from PIL import Image, ImageFont, ImageDraw

# original: https://github.com/TheMorpheus407/Python-Lets-Code/blob/master/CompressImageAndWatermark.py
# https://www.youtube.com/watch?v=wI9yE7ZIbMg

def save_compressed(img):
    img.save(img_path_formatted, "JPEG", optimize=True, quality=85) # change quality to change the image size

if __name__ == "__main__":
    abfrage = input("Is the path to the image in quotation marks?  yes = 1; no = 2\n")
    if abfrage == "1":
        img_path = input("Enter path to image in qutation marks:\n")
        img_path_formatted = img_path.split("\"")[1]
        img = Image.open(img_path_formatted)
        rgb_img = img.convert('RGB')
        save_compressed(rgb_img)
    elif abfrage == "2":
        img_path_formatted = input("Enter path to image without qutation marks:\n")
        img = Image.open(img_path_formatted)
        rgb_img = img.convert('RGB')
        save_compressed(rgb_img)