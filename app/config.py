from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    jwt_algorithm: str
    debug: bool
    smtp_server: str
    smtp_port: int
    sender_email: str
    sender_password: str
    log_level: str
    environment: str
    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()
