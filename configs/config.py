import toml


class Configs:

    def __init__(self):
        pass

    @staticmethod
    def get_database_configs(config_path: str) -> dict:

        config = toml.load(config_path)
        db_config: dict = config['DATABASE']
        return db_config
    
    @staticmethod
    def get_rabbit_configs(config_path: str) -> dict:

        config = toml.load(config_path)
        rabbbit_config = config['RABBITMQ_CONFIG']
        return rabbbit_config
    
    def url_string_conn(configs: dict) -> str:

        username = configs['DB_USERNAME']
        password = configs['DB_PASSWORD']
        dbname = configs['DB_DATABASE']
        host = configs['DB_ADRESS']
        port = configs['DB_PORT']
        db_type = configs['DB_TYPE']

        url = f"{db_type}://{username}:{password}@{host}:{port}/{dbname}"
        return url