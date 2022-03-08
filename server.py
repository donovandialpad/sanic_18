import os
import json
from sanic import Sanic
from sanic_babel import Babel
from sanic_babel import gettext
from sanic.response import json as sanic_json
from cors import add_cors_headers
from options import setup_options


app = Sanic("App")
babel = Babel(app, configure_jinja=False)


def get_data_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "./static", "data.json")
    return json.load(open(json_url))


@app.get("/")
async def index(request):
    response = gettext('Please translate me, I am a message!', request=request) + ' ' + gettext('My name is %(name)s.',
                                                                                                name='Donovan',
                                                                                                request=request)
    return sanic_json({'message': response})


@app.get("/get_data")
async def get_data(request):
    return sanic_json(get_data_json())

@babel.localeselector
def get_locale(request):
    return 'es'
    langs = request.headers.get('accept-language')
    if langs:
        return langs.split(';')[0].split(',')[0].replace('-', '_')


@babel.timezoneselector
def get_timezone(request):
    if request['current_user'] is not None:
        return request['current_user'].timezone


# Add OPTIONS handlers to any route that is missing it
app.register_listener(setup_options, "before_server_start")

# Fill in CORS headers
app.register_middleware(add_cors_headers, "response")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, auto_reload=True, debug=True)
