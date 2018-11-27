.. _twill_runner:

Twill Runner
============

Integrates the twill web browsing scripting language with Django.

Introducation
--------------

Provides two main functions, ``setup()`` and ``teardown``, that hook
(and unhook) a certain host name to the WSGI interface of your Django
app, making it possible to test your site using twill without actually
going through TCP/IP.

It also changes the twill browsing behaviour, so that relative urls
per default point to the intercept (e.g. your Django app), so long
as you don't browse away from that host. Further, you are allowed to
specify the target url as arguments to Django's ``reverse()``.

Usage::

    twill3.setup()
    try:
        twill3.go('/')                     # --> Django WSGI
        twill3.code(200)

        twill3.go('http://google.com')
        twill3.go('/services')             # --> http://google.com/services

        twill3.go('/list', default=True)   # --> back to Django WSGI

        twill3.go('proj.app.views.func',
                 args=[1,2,3])
    finally:
        twill3.teardown()

For more information about twill3
