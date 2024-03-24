import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'mysql')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'sakila')
DATABASE_PORT = os.getenv('DATABASE_PORT', '3306')