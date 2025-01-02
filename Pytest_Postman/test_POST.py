import pytest
import allure
import requests


@allure.title("TC1-Create Booking CRUD positive")
@allure.description("Verify the create booking!!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url=base_url+base_path
    headers={
        "Content-Type" : "application/json"
    }
    payload={
        "firstname": "Sup",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    responseData=requests.post(url=full_url,headers=headers,json=payload)
    print(responseData.text)
    assert responseData.status_code==200
    responseData_json = responseData.json()
    bookingid=responseData_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid>0
    assert type(bookingid)==int
    firstname=responseData_json["booking"]["firstname"]
    assert firstname=="Sup"
    assert type(firstname) == str
    lastname=responseData_json["booking"]["lastname"]
    assert lastname=="Brown"
    assert type(lastname) == str
    totalprice=responseData_json["booking"]["totalprice"]
    assert totalprice==111
    assert type(totalprice) == int
    depositpaid=responseData_json["booking"]["depositpaid"]
    assert depositpaid==True
    assert type(depositpaid) == bool
    checkin=responseData_json["booking"]["bookingdates"]["checkin"]
    assert checkin=="2018-01-01"
    assert type(checkin) == str
    checkout=responseData_json["booking"]["bookingdates"]["checkout"]
    assert checkout=="2019-01-01"
    assert type(checkout) == str

    time=responseData.elapsed.total_seconds()
    assert time<3


@allure.title("TC2-Create Booking CRUD negative")
@allure.description("Verify the booking is not created without request payload!!")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url=base_url+base_path
    headers={
        "Content-Type" : "application/json"
    }
    json_payload={ }
    responseData=requests.post(url=full_url,headers=headers, json=json_payload)
    assert responseData.status_code==500
    print(responseData.text)
    assert responseData.text=="Internal Server Error"


