import Image, ImageDraw, ImageFont

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
    fill = "white"
    outline = "blue"
    
    if shape == "year":
        lines = [(5, 0), (25, 0), (31, 16), (25, 31), (5, 31), (0, 16)]
        draw.polygon(lines, fill=fill)
    elif shape == "month":
        draw.rectangle((1, 1, 30, 30), fill=fill, outline=outline)
    elif shape == "day":
        lines = [(15, 1), (31, 31), (1, 31)]
        draw.polygon(lines, fill=fill)
    elif shape == "hour":
        draw.ellipse((0, 0, 30, 30), fill=(255, 255, 255))
    
def draw_text(draw, number, shape):
    font_size = 18
    font = ImageFont.truetype('/var/lib/defoma/x-ttcidfont-conf.d/dirs/TrueType/Georgia.ttf', font_size)
    text_size = font.getsize(number)
    margin_top = (32 - text_size[1]) / 2 
    if shape == "day":
        margin_top += 3    
    margin_left = (32 - text_size[0]) / 2
    draw.text((margin_left, margin_top), number, font=font, fill="black") #Draw text
    
    
def get_image(timestamp):
    shape, number = get_img_data(timestamp)
    print shape, number
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_shape(draw, shape)
    draw_text(draw, number, shape)
    
    img.save("icono.jpg", "JPEG")
    
    
    
if __name__ == "__main__":
    timestamp = 816870646
     
    get_image(timestamp)
