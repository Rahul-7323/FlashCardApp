import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "database.sqlite3")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_USERNAME_ENABLE = True
    SECURITY_REDIRECT_BEHAVIOR = 'spa'
    WTF_CSRF_CHECK_DEFAULT = False
    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None
    UPLOAD_FOLDER = os.path.join(basedir, '../static/files')
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    # Read the below values from environment variables for production
    ###############################################################################################
    SECRET_KEY = "k'u8Sj>VmmG,$'X!tAA&{A,iDBt?9D8~J7!3O[yKW8XU|{dlZ:k|ZTZI},BCg"
    SECURITY_PASSWORD_SALT = "u@8(YLSt<UB6eNsn={SHbd9ZA*[]I}cI!*|X8]J#O:|.>RZ7DQe>9(mUw.a8d"
    ############################################################################################### 
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
    REDIS_URL = 'redis://127.0.0.1:6379'
