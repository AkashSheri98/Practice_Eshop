from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    #foriegn key purpose return string
    def __str__(self):
        return self.name
