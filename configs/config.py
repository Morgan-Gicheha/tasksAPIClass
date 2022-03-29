import os
###########################DEVELOPMENT CONFIG########################################
class DevelopmentConfig:
    # RESTX_VALIDATE = True
    PROPAGATE_EXCEPTIONS = False
    SECRET_KEY = os.urandom(20)
    JWT_SECRET_KEY = os.urandom(20)
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:morgan@127.0.0.1:5432/restx"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///restx.db"
    SQLALCHEMY_DATABASE_URI = "postgres://kbmithtlwhakxe:024ee18efebbd5e0d391714a28046b216c933f2750974f46e1b89e1f8f160ab5@ec2-34-235-33-44.compute-1.amazonaws.com:5432/d2r68bip0nkt1c"
    
    



###########################TESTING CONFIG########################################
class TestingConfig:

   SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.db"
