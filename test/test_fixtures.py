from src.person import Person
import pytest

# @pytest.fixture(scope="function") default scope can be omitted
@pytest.fixture
def ivan():
    return Person("Ivan")

# all scopes are
# function: the default scope, the fixture is destroyed at the end of the test.
# class: the fixture is destroyed during teardown of the last test in the class.
# module: the fixture is destroyed during teardown of the last test in the module.
# package: the fixture is destroyed during teardown of the last test in the package.
# session: the fixture is destroyed at the end of the test session.
@pytest.fixture(scope="module")
def george():
    return Person("George")

@pytest.fixture
def people(ivan, george):
    return [ivan, george]

@pytest.fixture
def employee_list():
    employees = [Person("Maria"), Person("Mathew"), Person("Oscar")]
    print([f"{e.name}:{e.is_data_scientist}" for e in employees])
    
    yield employees

    [e.fire() for e in employees]
    print([f"{e.name}:{e.is_data_scientist}" for e in employees])

@pytest.fixture(params=[Person("Synthia"), Person("David")], ids=["synthia", "david"])
def employee(request):
    return request.param    

def test_ivan_data_scientist(ivan):
    assert ivan.is_data_scientist
    ivan.fire()
    assert not ivan.is_data_scientist

def test_ivan_data_scientist2(ivan):
    assert ivan.is_data_scientist
    ivan.fire()
    assert not ivan.is_data_scientist

def test_george_data_scientist(george):
    assert george.is_data_scientist
    george.fire()
    assert not george.is_data_scientist

def test_george_data_scientist2(george):
    assert george.is_data_scientist
    george.fire()
    assert not george.is_data_scientist

def test_any_data_scientists(people):
    assert any(p.is_data_scientist for p in people)

def test_all_data_scientists(employee_list):
    assert all(p.is_data_scientist for p in employee_list)

def test_parametrized_fixture(employee):
    assert employee.is_data_scientist