#!/usr/bin/python
# -*- coding: utf-8 -*-
"""CherryPy root object class."""
import cherrypy
from pacifica.user_mgmt.view.render import render
from pacifica.user_mgmt.controller.test import HelloWorld

def error_page_default(**kwargs):
    return render('error')

class Root(object):
    """ CherryPy root object class. """
    def index(self):
        return render('hello_world', foo='bar')

    index.exposed = True

    test = HelloWorld()
