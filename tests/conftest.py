import pytest
from playhouse.sqlite_ext import SqliteExtDatabase
from desktop_app import models

@pytest.fixture(scope="function")
def test_db(monkeypatch):
    models.db.close()
    memory_db = SqliteExtDatabase(":memory:")
    monkeypatch.setattr(models, "db", memory_db)
    memory_db.bind([models.Contact])
    memory_db.connect()
    memory_db.create_tables([models.Contact])
    yield memory_db
    memory_db.close()