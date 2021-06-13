import os

import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = NnUdYr28vxncCAuYyppNp33H
ALLOWED_HOSTS = ["*"]
DJANGO_SETTINGS_MODULE = mysite.heroku

MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,
)
