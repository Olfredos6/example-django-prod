from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Publisher: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"<Category: {self.name}>"


class Book(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()
    authors = models.CharField(max_length=300)
    image = models.URLField(null=False, max_length=500)
    preview_link = models.URLField(null=True, max_length=500)
    date_published = models.DateField(null=False)
    info_link = models.URLField(null=True, max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category)

    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f"<Book: {self.title} - {self.authors}>"

    def multiplie_prix_par_10(self):
        self.price = self.price * 10
        self.save()

    def increment_view_count(self):
        self.view_count = self.view_count + 1
        self.save()
