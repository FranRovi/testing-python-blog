from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('My blog', 'Joe Black')

        self.assertEqual("My blog", b.title)
        self.assertEqual("Joe Black", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('My blog', 'Joe Black')
        b2 = Blog('My day', 'Rolf')

        self.assertEqual("My blog by Joe Black (0 posts)", b.__repr__())
        self.assertEqual("My day by Rolf (0 posts)", b2.__repr__())

    def test_repr_multiple(self):
        b = Blog('My blog', 'Joe Black')
        b.posts = [{'My day': "My day was great"}]

        b2 = Blog('Peter\'s blog', 'Peter Parker')
        b2.posts = [{'My day': "My day was great"},
                    {'My night': "My night was terrible"}]

        self.assertEqual("My blog by Joe Black (1 post)", b.__repr__())
        self.assertEqual("Peter's blog by Peter Parker (2 posts)",
                         b2.__repr__())



