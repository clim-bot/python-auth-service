import unittest
from app import create_app

class AuthServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_register_user(self):
        response = self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        # Register user first
        self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.post('/api/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

if __name__ == '__main__':
    unittest.main()
