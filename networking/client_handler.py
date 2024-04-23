import requests

def send_to_server(prompt):
    response = requests.post('http://localhost:5000/process', json={'prompt': prompt})
    return response.json()
