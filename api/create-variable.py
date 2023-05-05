import requests

payload_json = {
  "description": "string",
  "key": "plumbers",
  "value": "data"
}

response = requests.post(
    url='http://localhost:8080/api/v1/variables'
    , json=payload_json
    , auth = ('admin','admin')
    )

response.json()