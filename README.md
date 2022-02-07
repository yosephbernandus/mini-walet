# mini-walet

### Requirements
- python 3.6 or higher

### install and run:
- create directory a directory example (mini) using mkdir or anything else -> `mkdir mini`
- open directory using cd -> `cd mini`
- create python environment -> `python3 -m venv my_env`
- activate environment -> `source my_env/bin/activate`
- clone project `git clone https://github.com/yosephbernandus/mini-walet.git`
- open directory project -> `cd mini-walet`
- installing requirements -> `pip install -r requirements.txt`
- migrate local db -> `python manage.py migrate`
- create superuser to login django admin -> `python manage.py createsuperuser` and complete the form
- run -> `python manage.py runserver 0:8000` (not always port 8000)

### Setup data
- open django admin http://127.0.0.1:8000/admin, login with user that you created
- go to menu wallet ids and save, dont fill a token field. it will generated when user login
- go to menu wallet, create a wallet and fill `owned_by` field using wallets ids that created before, it must show a dropdown list after than save
- run api using postman/curl


## Postman
https://documenter.getpostman.com/view/1635245/UVeJKQRB
