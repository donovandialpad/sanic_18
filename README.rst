Sanic Babel And Vue i18n
=====


Sanic is a Python 3.7+ web server and web framework that’s written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

sanic-babel is an extension to Sanic that adds i18n and l10n support to any Sanic application with the help of babel, pytz and speaklater. It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to gettext translations.


.. code-block:: python

   @app.get("/")
   async def index(request):
   response = gettext('Please translate me, I am a message!', request=request) + ' ' + gettext('My name is %(name)s.',
                                                                                                name='Donovan',
                                                                                         request=request)
sanic babel locale
----------

.. code-block:: python

   @babel.localeselector
   def get_locale(request):
    langs = request.headers.get('accept-language')
    if langs:
        return langs.split(';')[0].split(',')[0].replace('-', '_')

Installing
----------

.. code-block:: text

   $ pip install -i requirements.txt
   
.. code-block:: text

   $ sanic server.app

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

Vue and vue-i18n
----------
https://kazupon.github.io/vue-i18n/

Vue I18n is internationalization plugin of Vue.js. It easily integrates some localization features to your Vue.js Application.

.. code-block:: text

   $ cd vue-i18n

install npm packages

.. code-block:: text

   $ npm install

Run dev server

.. code-block:: text

   $ npm run dev

Go to http://localhost:3000 and vue will automatically redirect you to http://localhost:3000/en
can you change you language to Spanish