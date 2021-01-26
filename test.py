import requests
import json

BASE_URL="http://127.0.0.1:5000/"


def valid_payments_with_different_amount():
    data=[]
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':80.8}, 200))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':800.8}, 200))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':8.8}, 200))

    for elem_data, code in data:
        response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
        assert response.status_code == code

def payments_with_Valid_Invalid_Card_Numbers():
    # Card Number should be valid & Must be 16 digit Card Number  
    data=[]
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':80.8}, 200))
    data.append(({'CCN':'4649510306051947', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':800.8}, 400))
    data.append(({'CCN':'46495103060519447', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':8.8}, 400))

    for elem_data, code in data:
        response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
        assert response.status_code == code

def payments_with_Expired_Unexpired_Cards():
    # Card Expiry Date should be in MM/YYYY Format like real Cards
    # Card have Expiry Date of Current Month of the present Year are invalid
    data=[]
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2024', 'AMT':80.8}, 200))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2019', 'AMT':80.8}, 400))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'01/2021', 'AMT':80.8}, 400))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'2021/01', 'AMT':80.8}, 400))
    
    for elem_data, code in data:
        response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
        assert response.status_code == code

def payments_with_Invalid_Security_Number():
    # Security Card must be a String of length 3
    data=[]
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2024', 'AMT':80.8}, 200))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'3656', 'ED':'02/2024', 'AMT':80.8}, 400))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'36', 'ED':'01/2024', 'AMT':80.8}, 400))
    data.append(({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':354, 'ED':'01/2024', 'AMT':80.8}, 400))
    
    for elem_data, code in data:
        response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
        assert response.status_code == code

def payments_No_Empty_Incomplete_Data():
    # Security Card must be a String of length 3
    data=[]
    data.append(({'CCN':'4649510306051944', 'SC':'365', 'ED':'02/2024'}, 400))
    data.append(({}, 400))

    response = requests.get(f"{BASE_URL}/ProcessPayment")
    assert response.status_code == 400
    for elem_data, code in data:
        response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
        assert response.status_code == code

if __name__ == '__main__':
    valid_payments_with_different_amount()
    payments_with_Valid_Invalid_Card_Numbers()
    payments_with_Expired_Unexpired_Cards()
    payments_with_Invalid_Security_Number()
    payments_No_Empty_Incomplete_Data()
    print("Test Completed ..")
