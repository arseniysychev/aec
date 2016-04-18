import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from aec.apps.vocabulary.serializers import DictionarySerializer


class Command(BaseCommand):
    args = ''
    help = 'load vocabulary from csv_file'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.input_options = None

    def add_arguments(self, parser):
        parser.add_argument(
            '-p', '--print',
            default=False,
            action='store_true',
            dest='print',
            help='Print info.'
        )
        parser.add_argument(
            '-f', '--file',
            dest='file',
            help='File for load to db.'
        )

    def print_info(self, template='', context=None):
        if self.input_options['print']:
            context = context or {}
            print str(template).format(**context)

    def handle(self, *args, **options):
        if not options['file']:
            raise CommandError("Option `--file=...` must be specified.")

        file_path = os.path.join(settings.BASE_DIR,
                                 'data/{f}'.format(f=options['file']))

        if not os.path.isfile(file_path):
            raise CommandError("File does not exist at the specified path.")

        self.input_options = options
        with open(file_path) as dict_file:
            csv_data = csv.DictReader(dict_file)
            for row in csv_data:
                row['translate'] = row['translate'].decode('utf-8')
                vocabulary_item = DictionarySerializer(data=row)
                if vocabulary_item.is_valid():
                    vocabulary_item.save()
                    self.print_info('{word}', row)
                else:
                    self.print_info('word - {word}\nerror - {error}', dict(
                        word=row['word'],
                        error=vocabulary_item.errors))
