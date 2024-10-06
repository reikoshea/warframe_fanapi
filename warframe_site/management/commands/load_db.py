from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Get Images from github"

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-drop-collections",
            action="store_true",
            help="Skip dropping the collection before importing data",
        )

    def handle(self, *args, **options):
        import utils
        if (options["skip_drop_collections"]):
            utils.load_db(False)
        else:
            utils.load_db()
