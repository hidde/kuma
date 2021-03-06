import mock
import pytest

from kuma.core.tests import assert_no_cache_header
from kuma.core.urlresolvers import reverse


@pytest.mark.django_db
@mock.patch('kuma.contributions.views.enabled')
def test_contribute_view(mock_enabled, client, settings):
    """If enabled, contribution page is returned."""
    mock_enabled.return_value = True
    response = client.get(reverse('contribute'))
    assert_no_cache_header(response)
    assert response.status_code == 200


@pytest.mark.django_db
@mock.patch('kuma.contributions.views.enabled')
def test_thanks_view(mock_enabled, client, settings):
    """If enabled, contribution thank you page is returned."""
    mock_enabled.return_value = True
    response = client.get(reverse('contribute_succeeded'))
    assert_no_cache_header(response)
    assert response.status_code == 200


@pytest.mark.django_db
@mock.patch('kuma.contributions.views.enabled')
def test_error_view(mock_enabled, client, settings):
    """If enabled, contribution error page is returned."""
    mock_enabled.return_value = True
    response = client.get(reverse('contribute_error'))
    assert_no_cache_header(response)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('view', ('contribute',
                                  'contribute_succeeded',
                                  'contribute_error'))
@mock.patch('kuma.contributions.views.enabled')
def test_views_404(mock_enabled, view, client, settings):
    """If disabled, contribution pages are 404."""
    mock_enabled.return_value = False
    response = client.get(reverse(view))
    assert response.status_code == 404
