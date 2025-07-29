from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql+pymysql://127.0.0.1:1234/db"
    secret_key: str ="your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()