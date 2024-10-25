import requests

url = 'http://localhost:4000/api/models'

failures = 0
success = 0

def add(models):
    global success
    global failures
    print('Models To Add: ', len(models))

    for model in models:
        response = requests.post(url, json=model)    

        if response.status_code == 200:
            success = success + 1
            print("Request was successful")
        else:
            failures = failures + 1
            print("Request failed with status:", response.status_code, response.text)

    
    print('Finished Saving Models')
    print(f'Successes: {len(models)}/{success}')
    print(f'Failures: {len(models)}/{failures}')
    success = 0
    failures = 0