from django.core.management.base import BaseCommand

from allauth_sniperlinks.utils import bump_sniperlink_cache_version


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bump_sniperlink_cache_version()
        self.stdout.write('Sniperlink cache version incremented\n')