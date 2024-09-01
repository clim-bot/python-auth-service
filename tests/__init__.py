import unittest
from app import create_app, db
from app.models import User

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        # Create tables and add a test user
        with self.app.app_context():
            db.create_all()
            test_user = User(username='testuser')
            test_user.set_password('testpassword')
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

