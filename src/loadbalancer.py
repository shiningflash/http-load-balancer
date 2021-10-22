import random

import requests
from flask import Flask, request

loadbalancer = Flask(__name__)

GOOGLE_BACKENDS = [
    'localhost:8081',
    'localhost:8082'
]
APPLE_BACKENDS = [
    'localhost:9081',
    'localhost:9082'
]


@loadbalancer.route('/')
def router():
    host_header = request.headers['Host']
    if host_header == 'www.google.com':
        response = requests.get(f'http://{random.choice(GOOGLE_BACKENDS)}')
        return response.content, response.status_code
    elif host_header == 'www.apple.com':
        response = requests.get(f'http://{random.choice(APPLE_BACKENDS)}')
        return response.content, response.status_code
    else:
        return 'Not found!', 404
