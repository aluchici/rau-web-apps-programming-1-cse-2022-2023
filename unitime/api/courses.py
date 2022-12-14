from base import BaseDTO

class Course(BaseDTO):
    def __init__(self, name, url, path_to_image):
        self.name = name 
        self.url = url 
        self.path_to_image = path_to_image

    def to_dict(self):
        course = {
            "name": self.name,
            "url": self.url,
            "image": self.path_to_image
        }
        return course 
