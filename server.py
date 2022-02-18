from sanic import Sanic
from sanic_babel import Babel
from sanic_babel import gettext
from sanic.response import json

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
    langs = request.headers.get('accept-language')
    if langs:
        return langs.split(';')[0].split(',')[0].replace('-', '_')


@babel.timezoneselector
def get_timezone(request):
    if request['current_user'] is not None:
        return request['current_user'].timezone


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, auto_reload=True, debug=True)
