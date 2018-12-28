from fixture.application import Application
import pytest
fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.tear_down()
    request.addfinalizer(fin)
    return fixture
