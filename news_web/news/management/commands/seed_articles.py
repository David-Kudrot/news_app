from django.core.management.base import BaseCommand
from news.models import Article


class Command(BaseCommand):
    help = 'Seed the database with sample articles'


def handle(self, *args, **options):
    sample = [
    {
    'title': 'Major breakthrough in renewable energy',
    'summary': 'Scientists announce a new efficient solar cell.',
    'content': 'Full content about the renewable energy breakthrough...\n'*5,
    'is_latest': True
    },
    {
    'title': 'Local sports team wins championship',
    'summary': 'Fans celebrate historic victory.',
    }]