"""I want a test that can cycle over each page of my Django website and confirm
the existance of each web page"""

from django.test import Client, TestCase
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


# # test that each page comes back correctly
# @pytest.mark.parametrize('test_urls', expected_page_urls)
# def test_page_success(client, test_urls):
#     print(client)
#     response = client.get(test_urls)
#
#     print(test_urls)
#
#     assert response.status_code == 200 or 302

# revised test (above) that uses Client()
@pytest.mark.parametrize('test_urls', expected_page_urls)
def test_page_success(test_urls):
    c = Client()
    response = c.get(test_urls)

    print(test_urls)

    assert response.status_code == 200 or response.status_code == 302
