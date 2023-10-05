class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_json(self):
        return {
            "title": self.title,
            "content" : self.content
        }

    def __str__(self):
        return "The title of this post is " + self.title + " and the content" \
            " is: " + self.content
