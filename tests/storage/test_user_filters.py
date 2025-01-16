import pytest

from publisher.storage import get_user_filters, update_user_filter


def test_get_user_filters_not_found(fixture_empty_storage):
    response = get_user_filters(1)

    assert response.user_id == 1
    assert response.is_enabled is False
    assert response.enabled is False
    assert response.category is None
    assert response.max_cost is None


def test_get_user_filters_happy_path(fixture_empty_storage):
    update_user_filter(1, category='sale')

    response = get_user_filters(1)

    assert response.user_id == 1
    assert response.is_enabled is False
    assert response.enabled is False
    assert response.category == 'sale'
    assert response.max_cost is None


@pytest.mark.parametrize('payload, expected', [
    ('test', 'test'),
    (None, None),
])
def test_update_user_filter_category(fixture_empty_storage, payload, expected):
    update_user_filter(1, category=payload)

    response = get_user_filters(1)
    assert getattr(response, 'category') == expected


@pytest.mark.parametrize('payload, expected', [
    (100500, 100500),
    (0, 0),
    (None, None),
])
def test_update_user_filter_max_cost(fixture_empty_storage, payload, expected):
    update_user_filter(1, max_cost=payload)

    response = get_user_filters(1)
    assert getattr(response, 'max_cost') == expected


@pytest.mark.parametrize('payload, expected', [
    (True, True),
    (False, False),
    (None, False),
])
def test_update_user_filter_enabled(fixture_empty_storage, payload, expected):
    update_user_filter(1, enabled=payload)

    response = get_user_filters(1)
    assert getattr(response, 'enabled') == expected
