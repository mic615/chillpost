from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class  ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@gmail.com', password='top_secret')
        self.body = 'my example post'
        self.post = Post(body = self.body, owner = self.user)

    def test_model_user_can_create_a_post(self):
        """Test the single model can create a transaction."""
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
