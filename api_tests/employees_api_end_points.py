import requests

base_url = 'https://emps.alatoo.edu.kg'


def get_all_employees():
    url = base_url + '/api/employees'
    print('\nGET')
    print('URL: ', url)
    response = requests.get(url)
    elements_list = response.json()
    for i in range(5):
        print(elements_list[i])
        if i == len(elements_list) - 1:
            break
    return response


def get_employee_by_id(employee_id):
    url = base_url + '/api/employees' + '/' + str(employee_id)
    print('\nGET BY ID')
    print('URL: ', url)
    response = requests.get(url)
    return response


def create_employee(employee_data):
    url = base_url + '/api/employees'
    print('\nPOST')
    print('URL: ', url)
    response = requests.post(url, json=employee_data)
    print(response.text)
    return response


def update_employee(updated_data):
    url = base_url + '/api/employees'
    print('\nPUT')
    print('URL: ', url)
    response = requests.put(url, json=updated_data)
    print(response.text)
    return response


def delete_employee(employee_id):
    url = base_url + '/api/employees' + '/' + str(employee_id)
    print('\nDELETE')
    print('URL: ', url)
    response = requests.delete(url)
    return response
