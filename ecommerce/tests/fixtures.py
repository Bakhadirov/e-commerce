import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

# @pytest.fixture()
# def create_admin(django_user_model):
#
#     return django_user_model.objects.create_superuser('admin', '', '1') # создаем при помощи пайтест джанго нового админа


@pytest.fixture(scope="session")
def fixture_db_setup(
    django_db_setup, django_db_blocker
):  # доступ к базе данных в фикстуре с привязкой к sessions/module,
    """
    load db data fixtures
    загрузка фикстуры базы данных
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixtures.json")
