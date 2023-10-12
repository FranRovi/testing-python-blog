from unittest import TestCase
from blog import Blog


class  BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('My blog', 'Joe Black')

        b.create_post('Test Post', 'Test Content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual("Test Post", b.posts[0].title)
        self.assertEqual("Test Content", b.posts[0].content)

    def test_to_json_in_blog(self):
        b = Blog('My blog', 'Joe Black')

        b.create_post('Test Title', 'Test Content')

        expected = {
            'title': 'My blog',
            'author': 'Joe Black',
            'posts': [{
                'title': 'Test Title',
                'content': 'Test Content'
            }]
        }

    def test_to_json__blog_no_posts(self):
        b = Blog('My blog', 'Joe Black')

        expected = {
            'title': 'My blog',
            'author': 'Joe Black',
            'posts': []
        }

        self.assertDictEqual(expected, b.to_json())
