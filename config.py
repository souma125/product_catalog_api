
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "mysql+pymysql://user:password@localhost/product_catalog")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
