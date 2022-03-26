import os
###########################DEVELOPMENT CONFIG########################################
class DevelopmentConfig:
    # RESTX_VALIDATE = True
    PROPAGATE_EXCEPTIONS = False
    SECRET_KEY = os.urandom(20)
    JWT_SECRET_KEY = os.urandom(20)
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:morgan@127.0.0.1:5432/restx"
    SQLALCHEMY_DATABASE_URI = "sqlite:///restx.db"
    



###########################TESTING CONFIG########################################
class TestingConfig:

   SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.db"
