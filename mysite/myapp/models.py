from os import name
from django.db import models
from django.contrib.auth.models import User
import pytz


# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100) 
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads') #upload folder will automatic create
    

    def __str__(self): #method to display name of product inside db
        return self.name
    def rating(self):
        comments = self.comments.all()
        if comments:
            total_rating = sum(comment.rating for comment in comments)
            average_rating = total_rating / len(comments)
            return round(average_rating, 1)
        return 0.0

    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="comments")
    dated = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    #     self.dated = timezone.localtime(timezone.now(), vietnam_tz)
    #     super().save(*args, **kwargs)


    def __str__(self):
        return '%s - %s' % (self.post.name, self.user)
    
    def get_rating_range(self):
        return range(self.rating)

    def get_empty_star_range(self):
        return range(5 - self.rating)
    
    