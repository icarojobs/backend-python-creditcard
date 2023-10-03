from decouple import config


def test_smoke_test():
    database_name = config('POSTGRES_DB')
    assert config('DB_URL') == f"postgresql+psycopg2://database/{database_name}?user=admin&password=password"
