#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def generate_image(avatar_path, text, output_path):
    """
    generates a new image from an original avatar, with text on top-right corner.
    args: 
    - avatar_path: path of the original avatar image
    - text: text to display on the image (4 chars at most)
    - output_path: path of the generated image
    """
    img_avatar = Image.open(avatar_path).convert("RGBA").resize((200,200))

    img_txt = Image.new("RGBA", img_avatar.size, (255,0,0,0))
    fnt = ImageFont.truetype("Courier New.ttf", 60) # monospaced font is preferred
    draw = ImageDraw.Draw(img_txt)
    draw.text((50,10), "%4s" % text, font=fnt, fill=(255,0,0,255))

    out = Image.alpha_composite(img_avatar, img_txt)
    # out.show() # test
    out.save(output_path, "JPEG")


if __name__ == "__main__":
    generate_image("./avatar.png", "7", "./out1.jpg")
    generate_image("./avatar.png", "9999", "./out2.jpg")