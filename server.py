from sanic import Sanic
from sanic_babel import Babel
from sanic_babel import gettext
from sanic.response import json
from cors import add_cors_headers
from options import setup_options


app = Sanic("App")
babel = Babel(app, configure_jinja=False)


@app.get("/")
async def index(request):
    response = gettext('Please translate me, I am a message!', request=request) + ' ' + gettext('My name is %(name)s.',
                                                                                                name='Donovan',
                                                                                                request=request)
    return json({'message': response})

@babel.localeselector
def get_locale(request):
    return 'it'
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
