from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ...models import Book


class Command(BaseCommand):

    help = 'Create User roles and assign permissions'

    def handle(self, *args, **options):
        user_group = Group.objects.get_or_create(name='User')
        librarian_group = Group.objects.get_or_create(name='Librarian')
        admin_group = Group.objects.get_or_create(name='Admin')*

        content_type = ContentType.objects.get_for_model(Book)
        add_book = Permission.objects.get(codename='add_book', content_type=content_type)
        change_book = Permission.objects.get(codename='change_book', content_type=content_type)
        delete_book = Permission.objects.get(codename='delete_book', content_type=content_type)
        view_book = Permission.objects.get(codename='view_book', content_type=content_type)
        
        save_book = Permission.objects.get(codename='save_book', content_type=content_type)

        user_group.permissions.set([view_book])
        librarian_group.permissions.set([add_book, change_book, view_book])
        admin_group.permissions.set([add_book, change_book, view_book, delete_book])

        self.stdout.write(self.style.SUCCESS("Role and permissions created"))
