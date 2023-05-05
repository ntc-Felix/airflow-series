curl -X 'POST' \
  'http://localhost:8080/api/v1/connections' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  --user "admin":"admin" \
  -d '{
  "conn_type": "teste",
  "connection_id": "plumbers",
  "description": "teste",
  "host": "teste",
  "login": "teste",
  "port": 0,
  "schema": "teste",
  "extra": "teste",
  "password": "teste"
}'