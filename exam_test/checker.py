def check_status_code(response, expected_status_code):
    print(f'Status code: {response.status_code}')
    assert response.status_code == expected_status_code
    print('status: ok!')


def check_message(response, key, expected_message):
    response_dict = response.json()
    assert expected_message in response_dict.get(key)
    print(f'msg: {expected_message}')
