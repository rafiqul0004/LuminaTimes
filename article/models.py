from django.db import models
from user.models import Viewer,Editor
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
STAR_CHOICES=[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
]

class Article(models.Model):
    editor=models.ForeignKey(Editor,on_delete=models.CASCADE)
    headline=models.CharField(max_length=100)
    category=models.ManyToManyField(Category)
    body=models.TextField()
    image=models.ImageField(upload_to='article/images/')
    publishing_date=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.headline

class Review(models.Model):
    reviewer = models.ForeignKey(Viewer,on_delete=models.CASCADE)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10,choices=STAR_CHOICES)

    def __str__(self) -> str:
        return f'Patient : {self.reviewer.User.first_name} : {self.article.headline}'