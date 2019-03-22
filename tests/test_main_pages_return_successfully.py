"""I want a test that can cycle over each page of my Django website and confirm
the existance of each web page"""

from django.test import Client, TestCase


# check pages and return http status code
expected_page_urls = [
                    '/admin/',
                    '/home/',
                    '/BensBlog/',
                    '/aboutme/',
                    '/resume/',
                    '/contactme/'
                    ]


# test that each page comes back correctly
def test_page_success():
    for pageurl in expected_page_urls:
        c = Client()
        response = c.get(pageurl)

        print(pageurl)

        assert response.status_code == 200


# test to dig deeper into redirect issues with '/admin/'
def test_admin_redirects_page():
    c = Client()
    response = c.get('/admin/')

    assert response.status_code == 302
