DEBUG = False

# MYSQL
USERNAME = "root"
PASSWORD = "123456qa!"
IP = "127.0.0.1"
PORT = 3306
DB = "flaskdb"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{ip}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    ip=IP,
    port=PORT,
    db=DB)
SQLALCHEMY_TRACK_MODIFICATIONS = True
