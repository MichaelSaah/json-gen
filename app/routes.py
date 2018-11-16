from flask import Flask, request, Response
from app.views import api_view

from app import app


@app.route('/')
def index():
    return 'index'

@app.route('/api/', methods=['POST'])
def api():
    return api_view(request)

