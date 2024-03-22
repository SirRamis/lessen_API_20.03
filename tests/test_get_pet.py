import requests

base_url = "https://petstore.swagger.io/v2/"
get_pet_by_iu_url = "/pet/5"
create_pet = "/pet"


# def test_get_pet_by_id():
#     full_url = base_url + get_pet_by_iu_url
#     response = requests.get(full_url)
#     status_code = response.status_code
#     body = response.json()
#     print()
#     print(status_code)
#     print(body)

def test_create_pet():
    full_url = base_url + create_pet
    data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(full_url, json=data)
    status_code = response.status_code
    print()
    print(status_code)
    body = response.json()
    print(body)

