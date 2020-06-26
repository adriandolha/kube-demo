import datetime
import json
import subprocess

import requests
from flask import Flask

app = Flask('Connector Job')
SOURCE_DIR = '/home/demo/files'
TARGET_DIR = '/home/demo/files'


def app_response(api_response):
    return app.response_class(response=api_response['body'], status=api_response['status_code'])


@app.route('/<file_name>', methods=['GET'])
def copy(file_name):
    start = datetime.datetime.now()
    result = requests.get('http://to-service:8000/notfound')
    end = datetime.datetime.now()
    copy_file(f'{SOURCE_DIR}/{file_name}')
    return app_response({"body": json.dumps({
        'status_code': result.status_code,
        'start': str(start.isoformat()),
        'end': str(end.isoformat())}), "status_code": "200"})


from kubernetes import client, config


def copy_file(file):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if str(i.metadata.name).startswith("to-service"):
            print("%s\t%s\t%s\t%s" % (i.status.phase, i.status.pod_ip, i.metadata.namespace, i.metadata.name))
            _copy_file_to_pod(file, i.metadata.name, 'demo')


def _copy_file_to_pod(file, name, namespace):
    result = subprocess.run(
        f'kubectl cp {file} {namespace}/{name}:{TARGET_DIR}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    print(result.stdout)
    print(result.stderr)
    print(result)
    if result.returncode != 0:
        raise Exception(f'{result.stderr}')


@app.route('/health', methods=['GET'])
def health():
    return app_response({"body": json.dumps("all good"), "status_code": "200"})


@app.route('/version', methods=['GET'])
def version():
    return app_response({"body": json.dumps("1.0.0"), "status_code": "200"})
