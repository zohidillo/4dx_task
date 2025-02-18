# Dasturni docker oqali yurguzish

```bash
docker compose up -d --build
```

# Dasturni dockersiz oqali yurguzish
```bash
pip install -r requirements.txt
python3 manage.py migrate
```
#### Hamma default datalarni o'rnatish (bu muhim test uchun)
```bash
python3 manage.py install
```
#### Default superuser
```text
username: admin
password: admin
```
#### Yurguzish
```bash
python3 manage.py runserver
```

# Swagger URL

[http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)