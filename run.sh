#!/bin/bash
cd app
gunicorn src.wsgi
