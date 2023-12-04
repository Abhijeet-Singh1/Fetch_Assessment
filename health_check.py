import yaml
import requests
import time
import os

def load_endpoints(file_path):
    with open(file_path, 'r') as file:
        endpoints = yaml.safe_load(file)
    return endpoints

def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', '')
        )
        response_latency = response.elapsed.total_seconds() * 1000
        if 200 <= response.status_code < 300 and response_latency < 500:
            return 'UP'
        else:
            return 'DOWN'

    except requests.exceptions.RequestException as e:
        return 'DOWN'

def calculate_availability(availability_list):
    total_tests = len(availability_list)
    successful_tests = availability_list.count('UP')
    availability_percentage = round((successful_tests / total_tests) * 100) if total_tests > 0 else 0
    return availability_percentage

def print_availability(domain_availability):
    for domain, data in domain_availability.items():
        print(f"{domain} has {data['availability']}% availability percentage")

def main(event, context):
    file_path = os.path.abspath('endpoints.yaml')
    endpoints = load_endpoints(file_path)
    domain_availability = {domain['url'].split('/')[2]: {'history': [], 'availability': 0} for domain in endpoints}

    try:
        while True:
            for endpoint in endpoints:
                status = check_health(endpoint)
                domain = endpoint['url'].split('/')[2]
                domain_availability[domain]['history'].append(status)

            for domain, data in domain_availability.items():
                data['availability'] = calculate_availability(data['history'])

            print_availability(domain_availability)
            time.sleep(15)

    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main(None, None)
