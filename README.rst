Sanic Babel
=====


Sanic is a Python 3.7+ web server and web framework that’s written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

sanic-babel is an extension to Sanic that adds i18n and l10n support to any Sanic application with the help of babel, pytz and speaklater. It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to gettext translations.

.. code-block:: python
    @app.get("/")
    async def index(request):
    response = gettext('Please translate me, I am a message!', request=request) + ' ' + gettext('My name is %(name)s.',
                                                                                                name='Donovan',
                                                                                                request=request)

Installing
----------



Babel usage
----------
Run the pybabel command that comes with Babel to extract your strings:

.. code-block:: text
    $ pybabel extract -F babel.cfg -o messages.pot .

This will use the mapping from the babel.cfg file and store the generated template in messages.pot. Now we can create the first translation. For example to translate to German use this command:

.. code-block:: text
    $ pybabel init -i messages.pot -d translations -l de

To compile the translations for use, pybabel helps again:

.. code-block:: text
    $ pybabel compile -d translations