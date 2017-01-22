"""
http://getblimp.github.io/django-rest-framework-jwt/


curl -X POST -d "username=taniguchi&password=77777" http://127.0.0.1:8000/api/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRhbmlndWNoaSIsImV4cCI6MTQ4NTExMTUzNywiZW1haWwiOiJqanpvb3c5NkBnbWFpbC5jb20iLCJ1c2VyX2lkIjoxfQ.ZQKmB4U0CaOmSu3Av8QWgy0ke4jd2E9Zjx9kv-58gBA

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Impqem9vdzk2QGdtYWlsLmNvbSIsImV4cCI6MTQ4NTExMjM1OCwidXNlcm5hbWUiOiJ0YW5pZ3VjaGkifQ.2YH2Z_Evw5BSFB4oGMV-pmhQqfdv2QKFEHBsmm4uekA" http://127.0.0.1:8000/api/comments/

curl http://127.0.0.1:8000/api/comments/


"""
