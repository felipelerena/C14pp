import bottle

from bottle import route, run, static_file
from iconos import get_image

@route('/')
def home():
    return "hola"

@route("/img/:ts")
def img(ts=1234):
    file_name = get_image(float(ts))
    return static_file(file_name, root='/home/felipe/devel/C14pp/lib/', 
                       mimetype='image/png')

bottle.debug(True)
run(host='localhost', port=8080)

