from django.test import TestCase
from .models import Hero


class ModelTests(TestCase):

    def test_create_hero(self):
        hero = Hero.objects.create(name='younes', alias='younesman')
                # Hero.objects.get(name='younes') # to get object
                # Hero.objects.filter(name='younes') # to get objects - A queryset           
       
        self.assertEqual(hero.name, "younes")
        self.assertEqual(hero.alias, "younesman")
        