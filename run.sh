#!/bin/bash
cd app
gunicorn app.wsgi
