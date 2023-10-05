from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test_title", "Test_content")

        self.assertEqual('Test_title', p.title)
        self.assertEqual('Test_content', p.content)

    def test_toJson(self):
        p = Post("Test_title", "Test_content")
        expected = {'title': 'Test_title', 'content': 'Test_content'}

        self.assertDictEqual(expected, p.to_json())

    def test_str(self):
        p = Post("Argentina Campeon", "Argentina gano su tercera estrella "
                                      "luego de vencer a Francia")

        expected = "The title of this post is Argentina Campeon and the " \
                   "content is: Argentina gano su tercera estrella luego de " \
                   "vencer a Francia"

        self.assertEqual(expected, p.__str__())