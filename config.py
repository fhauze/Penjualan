import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://muhammadhaviz:asalada@localhost/barang')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
