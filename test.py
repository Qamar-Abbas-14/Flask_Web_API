import requests
import json

BASE_URL="http://127.0.0.1:5000/"


data=[]
data.append({})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'345'})
data.append({'CCN':'46495103060519445', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':'80.8'})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2020', 'AMT':80.8})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'3655', 'ED':'02/2021', 'AMT':80.8})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':-80.8})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':80})

#Valid Payments with Different Amount
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':80.8})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':800.8})
data.append({'CCN':'4649510306051944', 'CH':'Qamar Abbas', 'SC':'365', 'ED':'02/2021', 'AMT':8.8})
# data = {'CCN':'4649510306051944', 'SC':'345', 'ED':'03/2024', 'AMT':'80.8'}


for elem_data in data:
    response = requests.get(f"{BASE_URL}/ProcessPayment", data=json.dumps(elem_data))
    print(response.text)
    print(response.status_code)
    print(response.json)


