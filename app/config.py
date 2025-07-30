from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database and JWT
    database_url: str
    secret_key: str
    jwt_algorithm: str
    debug: bool

    # Email configuration
    smtp_server: str
    smtp_port: int
    sender_email: str
    sender_password: str

    # Logging and environment
    log_level: str
    environment: str

    # Load from .env file
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
