import numpy
from PIL import Image
import curses
import requests
from io import BytesIO


def generate_image(url, height):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.convert('RGB')
    width = int((img.width / img.height) * height)
    img = img.resize((width, height), Image.ANTIALIAS)
    img_arr = numpy.asarray(img)
    height, width, _ = img_arr.shape

    return height, width, img_arr


def show_image(height, width, img_arr, y_start, window):
    for y in range(height):
        for x in range(width):
            pix = img_arr[y][x]
            color = int((pix[0]*6/256)*36 + (pix[1]*6/256)*6 + (pix[2]*6/256) - 1)
            curses.init_color(color, pix[0], pix[1], pix[2])
            curses.init_pair(color, color, color)
            window.addstr(y_start+y, x+1, "#", curses.color_pair(color))


def generate_and_show_image(url, height, y_start, window):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.convert('RGB')
    width = int((img.width / img.height) * height)
    img = img.resize((width, height), Image.ANTIALIAS)
    img_arr = numpy.asarray(img)
    height, width, _ = img_arr.shape
    for y in range(height):
        for x in range(width):
            pix = img_arr[y][x]
            color = int((pix[0]*6/256)*36 + (pix[1]*6/256)*6 + (pix[2]*6/256) - 1)
            curses.init_color(color, pix[0], pix[1], pix[2])
            curses.init_pair(color, color, color)
            window.addstr(y_start+y, x+1, "#", curses.color_pair(color))
