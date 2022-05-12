import pytest
from ecommerce.stockroom import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active"
)