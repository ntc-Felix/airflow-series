curl -X 'POST' \
  'http://localhost:8080/api/v1/variables' \
  -H 'Content-Type: application/json' \
  --user 'admin':'admin'\
  -d '{
    "conn_id": "minio",
    "conn_type": "s3",
    "extra": {
        "aws_access_key_id": "myaccesskey",
        "aws_secret_access_key": "mysecretkey",
        "host": "http://10.109.85.83:9000"
    }
}'

