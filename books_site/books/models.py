from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    num_pages = models.IntegerField()
    date_published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title