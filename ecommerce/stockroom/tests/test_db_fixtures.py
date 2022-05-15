import pytest
from ecommerce.stockroom import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, 'fashion', 'fashion', 1),
        (13, 't-shirt', 't-shirt', 1),
        (24, 'jeans', 'jeans', 1)
    ]
)
def test_category_of_stockroom_dbfixture(
        db, fixture_db_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active



@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ('fashion', 'fashion', 1),
        ('t-shirt', 't-shirt', 1),
        ('jeans', 'jeans', 1)
    ]
)
def test_category_of_stockroom_insert_data(
        db, category_factory, name, slug, is_active
)
    '''
    Создаем модели для инсерта в бд и тестинга их
    '''