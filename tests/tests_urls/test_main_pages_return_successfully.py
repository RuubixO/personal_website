"""I want a test that can cycle over each page of my Django website and confirm
the existance of each web page"""

# from django.test import Client, TestCase
import pytest


# check pages and return http status code
expected_page_urls = [
                    '/admin/',
                    '/home/',
                    '/BensBlog/',
                    '/aboutme/',
                    '/resume/',
                    '/contactme/',
                    '/dummy/'
                    ]


# test that each page comes back correctly; specifically pytest-django plugin
@pytest.mark.parametrize('test_urls', expected_page_urls)
def test_page_success(client, test_urls):

    response = client.get(test_urls)

    print(test_urls)

    assert response.status_code == 200 or response.status_code == 302
