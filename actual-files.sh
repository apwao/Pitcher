curl https://bootstrap.pypa.io/get-pip.py | python
git init
pip install flask
pip install flask-bootstrap
pip install flask-wtf 
mkdir app tests 
touch config.py .gitignore manage.py start.sh
cd app
mkdir main static templates 
cd main
touch __init__.py errors.py forms.py views.py
cd ..
touch __init__.py models.py requests.py email.py
cd ..
pip install flask-script
chmod a+x start.sh
python3.6 -m  pip install gunicorn

pip install flask-SQLAlchemy
pip install psycopg2
pip install flask-migrate
pip install flask-login
pip install flask-uploads
pip install flask-mail
pip install flask-simplemde markdown2

mkdir app/auth
cd app/auth
touch __init__.py views.py forms.py
cd ..
cd templates
mkdir auth
touch auth/register.htm auth/login.htm
mkdir profile
touch profile/profile.html
touch profile/update.html

cd ..
mkdir static/photos
