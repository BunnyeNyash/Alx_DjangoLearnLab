from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        permissions = {
            'Editors': ['can_create', 'can_edit'],
            'Viewers': ['can_view'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perms in permissions.items():
            group = Group.objects.get(name=group_name)
            for perm in perms:
                permission = Permission.objects.get(codename=perm, content_type__app_label='relationship_app')
                group.permissions.add(permission)
            self.stdout.write(self.style.SUCCESS(f'Assigned permissions to {group_name}'))
