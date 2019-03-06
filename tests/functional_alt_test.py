from selenium import webdriver
import unittest
import pytest



    @pytest.fixture
    visit_func():
        browser = webdriver.Firefox()
        yield browser

        browser.quit()

"""class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()"""

    def test_can_start_a_list_and_retrieve_it_later(visit_func):
        # Tamara heard about an awesome new to-do app. They check out its
        # homepage.
        visit_func.get('http://localhost:8000')

        # They notice the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # They are invited to enter a to-do item striaght away.

    """They type "Buy peacock feathers" into a text box.(Edith's hobby is tying
    fly-fishing lures).


    When they hit enter, the page updates, and now the page lists
    "1: Buy peacock feathers" as an item in a to-do list.


    There is still a text box inviting her to add another item. They enter
    "Use peacock feathers to make a fly" (Edit is very methodical).


    The page updates again, and now shows both items on their list.


    Edith wonders whether the site will remember their list. Then she sees that
    the site has generated a unique URL for her -- there is some explanatory
    text to that effect.

    They visit that URL - her to-do list is still there.
    Satisfied, she goes back to sleep.
    """

if __name__ == '__main__':
    unittest.main(warnings='ignore')
