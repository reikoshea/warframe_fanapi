from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Load data from wiki dump"

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-drop-collections",
            action="store_true",
            help="Skip dropping the collection before importing data",
        )

    def handle(self, *args, **options):
        import utils
        if (options["skip_drop_collections"]):
            utils.load_wiki(False)
        else:
            utils.load_wiki()
