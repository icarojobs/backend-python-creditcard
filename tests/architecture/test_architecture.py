from decouple import config


def test_smoke_test():
    DB_NAME = config('POSTGRES_DB')
    assert config('DB_URL') == f"postgresql+psycopg2://database/{DB_NAME}?user=admin&password=password"
