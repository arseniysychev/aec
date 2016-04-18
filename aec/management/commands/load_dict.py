import csv

from django.core.management.base import BaseCommand

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

    def print_info(self, template='', context=None):
        if self.input_options['print']:
            context = context or {}
            print str(template).format(**context)

    def handle(self, *args, **options):
        self.input_options = options
        with open('data/lave1_lesson1.csv') as dict_file:
            csv_data = csv.DictReader(dict_file)
            for row in csv_data:
                row['translate'] = row['translate'].decode('utf-8')
                vocabulary_item = DictionarySerializer(data=row)
                if vocabulary_item.is_valid():
                    vocabulary_item.save()
                else:
                    self.print_info('word - {word}\nerror - {error}', dict(
                        word=row['word'],
                        error=vocabulary_item.errors))
