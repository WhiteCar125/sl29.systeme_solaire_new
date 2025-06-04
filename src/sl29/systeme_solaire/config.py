import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = os.path.join('static', 'img')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # max 2MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
