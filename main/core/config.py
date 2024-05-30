from pydantic_settings import BaseSettings
import os,dotenv

dotenv.load_dotenv()





class Settings(BaseSettings):
    database_hostname: str = os.getenv("database_hostname")
    database_port: str = os.getenv("database_port")
    database_password: str = os.getenv("database_password")
    database_name: str = os.getenv("database_name")
    database_username: str = os.getenv("database_username")
    secret_key: str = os.getenv("secret_key")
    algorithm: str = os.getenv("algorithm")
    access_token_expire_minutes: int = os.getenv("access_token_expire_minutes")

    class Config:
        env_file = ".env"


settings = Settings()