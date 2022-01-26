import os
import json

if os.environ.get('COMPUTERNAME')=='CAPTAIN2020':
    with open(r"D:\OneDrive\Documents\projects\config_files\config_km_dashboard.json") as config_file:
        config = json.load(config_file)
elif os.environ.get('USER')=='sanjose':
    with open('/home/sanjose/Documents/environments/config.json') as config_file:
        config = json.load(config_file)
else:
    with open('/home/ubuntu/environments/config.json') as config_file:
        config = json.load(config_file)



class Config:
    SECRET_KEY = config.get('SECRET_KEY_DMR')
    SQLALCHEMY_DATABASE_URI = config.get('SQL_URI_UPLOADERAPP')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_PASSWORD = config.get('MAIL_PASSWORD_KM')
    MAIL_USERNAME = config.get('MAIL_USERNAME_KM')
    DEBUG = True
    UPLOADED_FILES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/files')
    UTILITY_FILES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/files_utility')
    QUERIES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/queries')
    FILES_DATABASE = os.path.join(os.path.dirname(__file__), 'static/files_database')
    UPLOAD_KIA = os.path.join(os.path.dirname(__file__), 'static/upload_kia')
    