from django.core.management.base import BaseCommand
from profiles.models import Category, Subcategory
from profiles.static_data import CATEGORIES

class Command(BaseCommand):
    help = 'Load static data into the database'

    def handle(self, *args, **kwargs):
        for category_data in CATEGORIES:
            category = Category.objects.create(name=category_data['name'])
            for subcategory_data in category_data['subcategories']:
                Subcategory.objects.create(category=category, name=subcategory_data['name'])