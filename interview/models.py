from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.id)


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.id)


class Question(models.Model):
    title = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    is_checking = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format('Question', self.id)
