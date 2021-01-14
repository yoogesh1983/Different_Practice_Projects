from django.test import TestCase
from twmblog.models import EmailForm, Comment, Post


class PostTestCase(TestCase):

    # Overide
    def setUp(self):
        print('init() method called......')
        # Post.objects.create(title='test1', slug='test', author=1)

    def test_PostInfo(self):
        print('PostInfo() method called......')
        qs = Post.objects.all()
        self.assertEqual(qs.count(), 0)
        # p1 = Post.objects.get(title='test1')
        # self.assertEqual(p1.slug == 'test')

    def tearDown(self):
        print('Destroy() method called.....')
