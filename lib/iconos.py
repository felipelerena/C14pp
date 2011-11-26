import Image
import ImageDraw
import ImageFont

from os import path
from datetime import datetime


def get_img_data(timestamp):
    ts_date = datetime.fromtimestamp(timestamp)
    now = datetime.now()
    diff = now - ts_date
    if diff.days >= 365:
        shape = "year"
        number = diff.days / 365.0
    elif diff.days >= 30:
        shape = "month"
        number = diff.days / 30.0
    elif diff.days >= 1:
        shape = "day"
        number = diff.days
    else:
        shape = "hour"
        number = diff.seconds / 3600.0
    
    return shape, str(int(number))

def draw_shape(draw, shape):
    fill = "black"
    #outline = "blue"
    
    if shape == "year":
        lines = [(5, 0), (25, 0), (31, 16), (25, 31), (5, 31), (0, 16)]
        draw.polygon(lines, fill=fill)
    elif shape == "month":
        draw.rectangle((0, 0, 31, 31), fill=fill)
    elif shape == "day":
        lines = [(15, 1), (31, 31), (1, 31)]
        draw.polygon(lines, fill=fill)
    elif shape == "hour":
        draw.ellipse((0, 0, 30, 30), fill=fill)
    
def draw_text(draw, number, shape):
    font_size = 18
    font = ImageFont.truetype('/var/lib/defoma/x-ttcidfont-conf.d/dirs/TrueType/Georgia.ttf', font_size)
    text_size = font.getsize(number)
    margin_top = (32 - text_size[1]) / 2  - 2
    if shape == "day":
        margin_top += 3    
    margin_left = (32 - text_size[0]) / 2
    draw.text((margin_left, margin_top), number, font=font, fill="white") #Draw text
    
    
def get_image(timestamp):
    shape, number = get_img_data(timestamp)
    file_name = "%s_%s.png" % (shape, number)
    if not path.exists(file_name):
        generate_image(timestamp, file_name, shape, number)
    
    return file_name
        
def generate_image(timestamp, file_name, shape, number):
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_shape(draw, shape)
    draw_text(draw, number, shape)
    img.save(file_name, "PNG")
    return file_name
    
if __name__ == "__main__":
    test_dates = [816870646, 1321792246, 1298205046, 1322302440, 1321202246, 1322335343]
    for date in test_dates:
        print get_image(date)
