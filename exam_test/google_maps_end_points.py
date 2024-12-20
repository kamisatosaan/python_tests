import requests

base_url = 'https://rahulshettyacademy.com'
api_key = 'qaclick123'


def create_place(place_data):
    url = base_url + f'/maps/api/place/add/json?key={api_key}'
    response = requests.post(url, json=place_data)
    return response


def get_place_by_id(place_id):
    url = base_url + f'/maps/api/place/get/json?key={api_key}&place_id={place_id}'
    response = requests.get(url)
    return response


def delete_place(place_id):
    url = base_url + f'/maps/api/place/delete/json?key={api_key}&place_id={place_id}'
    response = requests.delete(url)
    return response
