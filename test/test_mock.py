from src.database import Database
from src.metrics import Metrics

import pytest

def mocked_get_data():
    return ['mock data']

@pytest.fixture
def db(monkeypatch):
    db = Database("rtl.nl")
    # inject data
    monkeypatch.setattr(db, "get_data", mocked_get_data)
    return db

def test_database_data(db):
    assert len(db.get_data()) > 0

def mocked_metrics(self):
    self.predictions = [1, 7, 6]

def test_model_metric(monkeypatch):
    # model = Model(...)
    # metrics = Metrics(model, ["img1.png", "img2.png"])
    monkeypatch.setattr("src.metrics.Metrics.__init__", mocked_metrics)
    
    gts = [1, 2, 6]
    m = Metrics()
    acc = m.get_metric(gts, "accuracy")
    assert acc == 2./3