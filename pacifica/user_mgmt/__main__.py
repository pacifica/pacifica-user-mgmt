#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Metadata Module."""
import cherrypy
from pacifica.user_mgmt.controller.root import Root
from pacifica.user_mgmt.controller.root import error_page_default

def main():
    """Main method to start the httpd server."""
    cherrypy.config.update({ 'error_page.default': error_page_default })
    cherrypy.quickstart(Root())


if __name__ == '__main__':
    main()
