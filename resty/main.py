from flask import Flask, request
from kubernetes import client, config
import os
import yaml

app = Flask(__name__)

# Load the Kubernetes configuration from default location
config.load_kube_config()

@app.route('/connect', methods=['POST'])
def connect():
    ip = request.json.get('IP')
    port = request.json.get('PORT')
    username = request.json.get('USERNAME')
    password = request.json.get('PASSWORD')

    # Load the job YAML file
    with open('job.yaml', 'r') as f:
        job_manifest = yaml.safe_load(f)

    # Set the environment variables in the job manifest
    job_manifest['spec']['template']['spec']['containers'][0]['env'] = [
        {'name': 'IP', 'value': ip},
        {'name': 'PORT', 'value': port},
        {'name': 'USERNAME', 'value': username},
        {'name': 'PASSWORD', 'value': password},
    ]

    # Create a Kubernetes batch client
    batch_client = client.BatchV1Api()

    # Apply the job YAML file
    batch_client.create_namespaced_job(namespace='default', body=job_manifest)

    return 'Job triggered successfully', 200

@app.route('/', methods=['GET'])
def landing():
    return 'Usage: curl -X POST \
        http://<EXTERNAL_IP>/connect \
        -d \'ip=<REMOTE_HOST_IP>&port=<REMOTE_HOST_PORT>&username=<REMOTE_HOST_USERNAME>&password=<REMOTE_HOST_PASSWORD>\' \
        '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
