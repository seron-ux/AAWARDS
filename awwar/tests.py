from django.test import TestCase
from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class TestPostModel(TestCase):
    def setUp(self):
        self.user = User(username="testuser",password="adminpass")
        self.user.save()
        self.post = Post(
            image= SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg'),
            title="post title",
            desc="post desc",
            link="http://test.link.com",
            user=self.user,
            post_date=datetime.now(),
            technologies='lorem, ipsum, dolor, sit, amet'
        )
