import json
import os

from flask import Flask

app = Flask('To Service')


def app_response(api_response):
    return app.response_class(response=api_response['body'], status=api_response['status_code'])


@app.route('/', methods=['GET'])
def list():
    return app_response({"body": json.dumps(os.listdir('files')), "status_code": "200"})
