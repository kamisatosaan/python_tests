def check_status_code(response, expected_status_code):
    print(f'Status code: {response.status_code}')
    assert response.status_code == expected_status_code
    print(f'Status code верный!')


def check_data_type(response, expected_data_type):
    assert expected_data_type == type(response.json())
    print(f'Тип данных верный!')
