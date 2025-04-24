import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--skip", action="store", default="", help="Comma-separated test numbers to skip"
    )

@pytest.fixture(scope="session")
def skip_list(request):
    return [x.strip() for x in request.config.getoption("--skip").split(",") if x.strip()]





