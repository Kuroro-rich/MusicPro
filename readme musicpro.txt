framework flask 

instalaciones (todas dentro del env)

activar env ./env/Scripts/activate

python (compando de intalación de librerías varía dependiendo de version de python) 



flask
	pip install flask

librería para consumir WSDL en python 
	pip install zeep 


libreria BD 

pip install pymysql

otras librerías bd/autenticacion de login

pip install Flask-login
pip install Flask-MySqlbd
Flask-WTF
WTForms


para insertar fotos instalar 
pip install flask-uploads
(existe un bug con werkzeug)
{In flask_uploads.py

pip install transbank-sdk

Change

from werkzeug import secure_filename,FileStorage
to

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage}

otras librerias (la mayoria se instala junto con flask)

blinker      1.6.2
click        8.1.3
colorama     0.4.6
Flask        2.3.2
itsdangerous 2.1.2
Jinja2       3.1.2
MarkupSafe   2.1.3
pip          23.0.1
setuptools   65.5.0
Werkzeug     2.3.4



Desarrollo de templates:
	HTML
	CSS
	Bootstrap 5 
	JS




