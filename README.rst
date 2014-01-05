PyEmbed-Mustache
===============

.. image:: https://secure.travis-ci.org/pyembed/pyembed-mustache.png?branch=master
    :target: http://travis-ci.org/pyembed/pyembed-mustache
.. image:: https://coveralls.io/repos/pyembed/pyembed-mustache/badge.png
    :target: https://coveralls.io/r/pyembed/pyembed-mustache
.. image:: https://pypip.in/v/pyembed-mustache/badge.png
    :target: https://crate.io/packages/pyembed-mustache/
.. image:: https://pypip.in/d/pyembed-mustache/badge.png
    :target: https://crate.io/packages/pyembed-mustache/

PyEmbed plugin for rendering embeddings using Mustache templates.

Usage
-----

Initialize the plugin like this:

::

    renderer = MustacheRenderer(path)

where `path` is the path to a directory containing Mustache templates:

- `link.mustache`
- `photo.mustache`
- `rich.mustache`
- `video.mustache`

If you don't supply one of these files, a default embedding will be used
instead.

Compatibility
-------------

PyEmbed-Mustache has been tested with Python 2.7 and 3.3.

Installation
------------

PyEmbed-Mustache can be installed using pip:

::

    pip install pyembed-mustache

Contributing
------------

To report an issue, request an enhancement, or contribute a patch, go to
the PyEmbed-Mustache `GitHub`_ page.

License
-------

PyEmbed-Mustache is distributed under the MIT license.

    Copyright (c) 2013 Matt Thomson

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. _GitHub: https://github.com/pyembed/pyembed-mustache