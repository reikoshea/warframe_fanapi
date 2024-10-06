from django.core.management.base import BaseCommand, CommandError
import subprocess
import os

class Command(BaseCommand):
    help = "Get Images from github"

    def handle(self, *args, **options):
        subprocess.call("./extract_images.sh")
