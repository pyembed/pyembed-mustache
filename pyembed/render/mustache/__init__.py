# The MIT License(MIT)

# Copyright (c) 2013-2014 Matt Thomson

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pyembed.core.render import PyEmbedRenderer

import os
from pkg_resources import resource_string
from pystache import Renderer


class MustacheRenderer(PyEmbedRenderer):

    """Renders OEmbed responses using Mustache templates."""

    def __init__(self, template_dir):
        self.template_dir = template_dir

    def render(self, content_url, response):
        """Generates an HTML representation of an OEmbed response.

        :param content_url: the content URL.
        :param response: the response to render.
        :returns: an HTML representation of the resource.
        """

        template = self.__load_template_from_file(response)
        return Renderer().render(template,
                                 response,
                                 {'content_url': content_url})

    def __load_template_from_file(self, response):
        file_name = '%s.mustache' % response.type
        template_path = os.path.join(self.template_dir, file_name)

        try:
            with open(template_path) as template_file:
                return template_file.read()
        except IOError:
            # Error reading file - use default template.
            return resource_string(__name__, 'templates/%s' % file_name)
