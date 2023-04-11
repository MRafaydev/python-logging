import time
from flask import Flask, jsonify, request
from utils.customlogger import setup_logger
from api.api_calling import call_service_b
import os

app = Flask(__name__)
PORT = 5001

# Set up the custom logger for the microservice
logger = setup_logger('microservice', 'microservice.log')


@app.route('/')
def hello_world():
    # Log the start of the API request
    logger.info(f'{request.method} {request.path} - IP: {request.remote_addr} - PORT: {PORT}')

    # Call service_b and get its response
    response_data = call_service_b(logger)

    if response_data:
        return jsonify(response_data)
    else:
        return f'Unable to establish communication with service_b', 500


if __name__ == '__main__':
    app.run(port=5000)
