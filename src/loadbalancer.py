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


@loadbalancer.route('/google')
def google_router():
    response = requests.get(f'http://{random.choice(GOOGLE_BACKENDS)}')
    return response.content, response.status_code

@loadbalancer.route('/apple')
def apple_router():
    response = requests.get(f'http://{random.choice(APPLE_BACKENDS)}')
    return response.content, response.status_code

@loadbalancer.route('/notfound')
def no_router():
    return 'Not found!', 404
