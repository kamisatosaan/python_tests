import api_tests.employees_api_end_points as employees_api
import api_tests.checker as checker


def test_employees_api():
    # Проверить получение списка сотрудников. Убедиться, что статус-код равен 200.
    response = employees_api.get_all_employees()
    checker.check_status_code(response, 200)
    # Убедиться, что возвращаемый тип данных — список
    checker.check_data_type(response, list)

    # Статус-код равен 200 при успешном создании.
    valid_employee_data = {"name": "Ivan", "surname": "Ivanov", "salary": 1000, "department": "HR"}
    response = employees_api.create_employee(valid_employee_data)
    checker.check_status_code(response, 200)

    # Убедиться, что статус-код равен 200, если сотрудник существует
    response_dict = response.json()
    employee_id = response_dict.get('id')
    response = employees_api.get_employee_by_id(employee_id)
    checker.check_status_code(response, 200)

    # Убедиться, что статус-код равен 404, если сотрудник с указанным ID отсутствует
    non_existent_employee_id = 999999
    response = employees_api.get_employee_by_id(non_existent_employee_id)
    checker.check_status_code(response, 404)

    # Проверить, что статус-код равен 400, если переданы некорректные данные
    invalid_employee_data = {"name": "", "surname": "Ivanov", "salary": -500, "department": ""}
    response = employees_api.create_employee(invalid_employee_data)
    checker.check_status_code(response, 400)

    # Статус-код равен 200 при успешном обновлении.
    correct_updated_employee_data = {"id": 4254, "name": "Ivan", "surname": "Ivanov", "salary": 3100,
                                     "department": "Sales"}
    response = employees_api.update_employee(correct_updated_employee_data)
    checker.check_status_code(response, 200)

    # Статус-код равен 403, если пытаются обновить сотрудника с id <= 100.
    update_employee_data = {"id": 85, "name": "Ivan", "surname": "Ivanov", "salary": 3100, "department": "Sales"}
    response = employees_api.update_employee(update_employee_data)
    checker.check_status_code(response, 403)

    # Статус-код равен 400, если переданы некорректные данные.
    incorrect_updated_employee_data = {"id": 415, "name": "", "surname": "Ivanov", "salary": -500, "department": ""}
    response = employees_api.update_employee(incorrect_updated_employee_data)
    checker.check_status_code(response, 400)

    # Убедиться, что статус-код равен 200 при успешном удалении
    response = employees_api.delete_employee(employee_id)
    checker.check_status_code(response, 200)

    # Убедиться, что повторный запрос на удаление возвращает статус-код 404.
    response = employees_api.delete_employee(employee_id)
    checker.check_status_code(response, 404)

    # Статус-код равен 403, если пытаются удалить сотрудника с id <= 100.
    low_employee_id = 85
    response = employees_api.delete_employee(low_employee_id)
    checker.check_status_code(response, 403)

    # Статус-код равен 404, если сотрудник с указанным ID отсутствует.
    response = employees_api.delete_employee(employee_id)
    checker.check_status_code(response, 404)
