from rest_framework.test import APITestCase
from twmblog.models import EmailForm, Comment, Post

class PostAPITestCase(APITestCase):
    def setUp(self):
        print('init() API method called.....')

    def test_getPosts(self):
        print('API test Service() method called.....')
        url='http://127.0.0.1:8000/api/drf/apiviews/core/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = Post.objects.filter(slug= 'totalwine')
        self.assertEqual(qs.count(), 0)

    def tearDown(self):
        print('destroy() API method called...')


