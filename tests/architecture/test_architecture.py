from decouple import config


def test_smoke_test():
    assert config('DB_URL') == "postgresql+psycopg2://database/main?user=admin&password=password"
