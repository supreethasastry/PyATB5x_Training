import pytest
import allure
import requests

base_url="https://restful-booker.herokuapp.com"
headers={
    "Content-Type" :"application/json"}

def create_token():
    base_path="/auth"
    full_url=base_url+base_path
    json={
        "username" : "admin",
        "password" : "password123"
    }
    responseData=requests.post(url=full_url,headers=headers, json=json)
    assert responseData.status_code==200
    responseData_json = responseData.json()
    token = responseData_json["token"]
    print(token)
    assert type(token)==str
    assert len(token)>0
    return token

def get_bookingid():
    base_path="/booking"
    full_url=base_url+base_path
    payload = {
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
    responseData = requests.post(url=full_url, headers=headers, json=payload)
    responseData_json=responseData.json()
    bookingid=responseData_json["bookingid"]
    return bookingid

def test_putrequest():
    token=create_token()
    bookingid=get_bookingid()
    print(token)
    print(bookingid)
    base_path="/booking/"+str(bookingid)
    full_url_path=base_url+base_path
    cookie="token="+token
    headers1 ={
        "Content-Type": "application/json",
        "Cookie" : cookie
    }
    json_payload= {
        "firstname": "Sup",
        "lastname": "Smart",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.put(url=full_url_path,headers=headers1,json=json_payload)
    assert response.status_code==200
    assert response.json()["lastname"]=="Smart"
    print(response.json()["lastname"])


def test_delete():
    URL="https://restful-booker.herokuapp.com/booking/"
    booking_id=get_bookingid()
    Delete_url=URL + str(booking_id)
    cookie_value="token=" + create_token()
    headers1 = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response=requests.delete(url=Delete_url, headers=headers1)
    assert response.status_code==201


