from os import getenv

SECRET_KEY = getenv("SECRET_KEY")

DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")

CLOUDINARY_CLOUD_NAME=getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY=getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET=getenv("CLOUDINARY_API_SECRET")