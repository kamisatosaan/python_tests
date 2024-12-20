import exam_test.google_maps_end_points as gme
import exam_test.checker as checker


def test_google_maps():
    place_data = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Petty Friend",
        "phone_number": "(+996) 777 98 11 89",
        "address": "103, Toktogula street",
        "types": [
            "pets’ shop",
            "shop"
        ],
        "website": "http://google.com",
        "language": "English-EN"
    }
    response = gme.create_place(place_data)
    checker.check_status_code(response, 200)
    print(response.json())

    response_dict = response.json()
    place_id = response_dict.get('place_id')
    response = gme.get_place_by_id(place_id)
    checker.check_status_code(response, 200)
    print(response.json())

    deleted_place_id = {"place_id": "a1ef89c2d9b871c469fa03f8d6a53d52"}
    response = gme.delete_place(deleted_place_id)
    checker.check_status_code(response, 200)

    response = gme.get_place_by_id(deleted_place_id)
    checker.check_status_code(response, 404)
    checker.check_message(response, "msg", "doesn't exists")
