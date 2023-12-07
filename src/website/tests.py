import datetime

import factory
from django.test import TestCase

from . import models


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Publisher


class NoCategoryBookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    publisher = factory.SubFactory(PublisherFactory)
    date_published = factory.Faker("date_time")
    price = factory.Faker("pydecimal", left_digits=1, right_digits=2, positive=True)
    rating = factory.Faker("pydecimal", left_digits=1, right_digits=2, positive=True)


class PublisherModelTestCase(TestCase):
    def test_can_create_publisher(self):
        publisher = PublisherFactory.create()  # Publisher.objects.create
        # self.assertQuerySetEqual(models.Publisher.objects.all(), [publisher])
        self.assertEqual(models.Publisher.objects.all()[0], publisher)

    def test_model_str_method_has_instance_name_in_it(self):
        publisher = PublisherFactory.build()
        print("1. ===> ", publisher, "Nom du Publisher est: ", publisher.name)
        publisher.name = "First Publisher"
        print("2. ===> ", publisher, "Nom du Publisher est: ", publisher.name)
        print("La representaion textuelle du Publisher est", str(publisher))
        print("---->>>>>>>>>", publisher.name, "-----", str(publisher))
        self.assertIn(publisher.name, str(publisher))

    def test_muliplie_prix_par_10(self):
        book = NoCategoryBookFactory.create()
        # book.price = 1.5
        # book.save()
        prix_avant_mulitplication = book.price
        book.multiplie_prix_par_10()
        prix_apres_mult = book.price
        print("---->>>>>>.", prix_avant_mulitplication, prix_apres_mult)
        self.assertEqual(prix_avant_mulitplication * 10, prix_apres_mult)


# class CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.Category


# class CategoryModelTestCase(TestCase):
#     def test_can_create_category(self):
#         category = CategoryFactory.create()
#         self.assertQuerySetEqual(models.Category.objects.all(), [category])

#     def test_model_str_method_has_instance_name_in_it(self):
#         category = CategoryFactory.build()
#         category.name = "Some Category"
#         self.assertIn(category.name, str(category))


# class BookModelTestCase(TestCase):
#     def test_can_create_book(self):
#         book = NoCategoryBookFactory.create()
#         self.assertQuerySetEqual(models.Book.objects.all(), [book])

#     def test_can_add_categories_to_book(self):
#         book = NoCategoryBookFactory.create()
#         categories = CategoryFactory.create_batch(5)
#         book.categories.add(*categories)
#         self.assertQuerySetEqual(book.categories.all().order_by("id"), categories)

#     def test_model_str_method_has_instance_name_in_it(self):
#         book = NoCategoryBookFactory.build()
#         book.title = "Some Book"
#         self.assertIn(book.title, str(book))
