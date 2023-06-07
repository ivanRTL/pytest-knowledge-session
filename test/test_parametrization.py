import pytest
from src.functions import add_one
from src.person import Person

@pytest.mark.parametrize("input_val, expected_val", [(5, 6), (6, 7), (13, 14)])
def test_parametrization1(input_val, expected_val):
    assert add_one(input_val) == expected_val

@pytest.mark.parametrize("input_val, expected_val, name", [(5, 6, "ivan"), (6, 7, "george"), (13, 14, "david")])
def test_parametrization2(input_val, expected_val, name):
    p = Person(name)

    assert p.name == name

    assert add_one(input_val) == expected_val

@pytest.mark.parametrize("name", [("ivan"), ("george"), ("david")])
@pytest.mark.parametrize("input_val, expected_val", [(5, 6), (6, 7), (13, 14)])
def test_parametrization_stacked(input_val, expected_val, name):
    p = Person(name)

    assert p.name == name

    assert add_one(input_val) == expected_val

@pytest.fixture
def ivan_fixture():
    return Person("Ivan")

@pytest.fixture
def george_fixture():
    return Person("George")

@pytest.fixture
def david_fixture():
    return Person("David")

@pytest.mark.parametrize("fixture_name", [("ivan_fixture"), ("george_fixture"), ("david_fixture")])
@pytest.mark.parametrize("input_val, expected_val", [(5, 6), (6, 7), (13, 14)])
def test_parametrization_with_fixtures(input_val, expected_val, fixture_name, request):
    
    assert request.getfixturevalue(fixture_name).is_data_scientist

    assert add_one(input_val) == expected_val


