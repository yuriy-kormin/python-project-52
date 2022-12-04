from django.test import SimpleTestCase


class SimpleTest(SimpleTestCase):
    # databases = '__all__'

    def test_open_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
