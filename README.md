# Alexandria
Un template para bots de Telegram enfocados a guardar recursos de aprendizaje.

## Requirements.txt
El bot está escrito en Python3, así que:
pip3 install -r requirements.txt


# Mysql
El bot utiliza mysql como base de datos.
pymysql es la librería que utilizaremos para la comunicación.


# config.cfg
El fichero de configuración tendrá el formato siguiente:
 [BOT]
 token: tokentext

 [DATABASE]
 host: localhost
 user: database_user
 pass: database_password
 db:   database_name
