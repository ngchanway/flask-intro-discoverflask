import unittest
from tests.base import BaseTestCase

class FlaskTestCase(BaseTestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    # Ensure that the main page requires login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    # Ensure that welcome page loads
    def test_welcome_route_works_as_expected(self):
        response = self.client.get('/welcome', follow_redirects=True)
        self.assertIn(b'Welcome to Flask!', response.data)

    # Ensure that posts show up on the main page
    def test_post_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data={'username':'admin', 'password':'admin'},
            follow_redirects=True
        )
        self.assertIn(b'This is a test. Only a test.', response.data)

if __name__ == '__main__':
    unittest.main()
