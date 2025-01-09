# App-wide settings (DB URLs, secrets, environment configs)
import os

DB_URL = os.getenv("DB_URL", "postgresql://user:password@db:5432/integration_db")
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
