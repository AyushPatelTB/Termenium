import requests

API_URL = "https://tbuzzer.up.railway.app/api/v1/prediction/307ed76d-d323-4366-a431-1bf562da7a33"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})
