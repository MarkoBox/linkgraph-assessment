from django.core.management.base import BaseCommand
from market_data.tasks import update_market_data


class Command(BaseCommand):
    help = "Fetches new market data and updates the DB"

    def handle(self, *args, **options):
        update_market_data()
        self.stdout.write(self.style.SUCCESS('Successfully updated DB'))
