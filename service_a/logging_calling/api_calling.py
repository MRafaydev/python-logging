import time
import requests
import os 

def call_service_b(logger):
    SERVICE_B_URL = os.environ.get("SERVICE_B_URL")
    print(SERVICE_B_URL)

    try:
        # Send a request to service_b and log the response
        response_start_time = time.time()
        response = requests.get(SERVICE_B_URL)
        print(response)
        response_end_time = time.time()

        # Log the response time and status code from service_b
        response_time = response_end_time - response_start_time
        logger.info(f'Sending request to {SERVICE_B_URL} - '
                    f'Status Code: {response.status_code} - Response Time: {response_time:.4f} seconds')
        logger.info(f'Received response from service_b: {response.text} ')
        
        # Perform some operations on the response data from service_b
        response_data = response.json()
        modified_response_data = {}
        for key, value in response_data.items():
            modified_response_data[key] = value.upper()

        # Log the modified response data
        logger.info(f'Modified response data from service_b: {modified_response_data}')

        return modified_response_data

    except requests.exceptions.RequestException as e:
        # Handle errors from failed requests to service_b
        logger.error(f'Failed to get response from service_b: {e}')
        logger.info(f'Service_b is currently down')

        return None
