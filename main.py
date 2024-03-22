import requests

# response = requests.get('https://restful-booker.herokuapp.com/booking')
#
# print(response.headers)
def create_booking():
    url = 'https://restful-booker.herokuapp.com/booking'
    data = {
        "firstname" : "Jimmmmmi",
        "lastname" : "Browwwwwwn",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"}

    response = requests.post(url=url, json=data)

    print(response.json())

create_booking()rgerge