import pytest
from playhouse.sqlite_ext import SqliteExtDatabase

def test_db(monkeypatch):
    from desktop_app import models
    models.db.close()
    memory_db = SqliteExtDatabase(':memory:')
    monkeypatch.setattr(models, 'db', memory_db)
    models.db.bind([models.Contact])
    yield memory_db
    models.db.close()

