## How to run localy using Docker
1. Run following command
```commandline
$ docker build -t visionary_img .
$ docker run --rm -d --name visionary_ctn -p 8000:8000 visionary_img

```
## Setup local dev environment
1. Create virtualenv and activate virtualenv
```commandline
$ python -m venv .venv
$ source .venv/bin/activate (for linux)
$ .\.venv\Scripts\activate (for windows)
```
2. Install and run project
```commandline
$ pip install -r requirements.txt
$ python manage.py runserver
```
#### You can access into the follwing url: http://127.0.0.1:8000
Login info: admin@gmail.com / Mamun@123
