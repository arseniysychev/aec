import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from aec.apps.vocabulary.serializers import DictionarySerializer
from aec.apps.vocabulary.models import Word
from aec.apps.library.serializers import LibrarySerializer
from aec.apps.library.models import Library


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
        parser.add_argument(
            '--level',
            dest='level',
            help='Level for data.'
        )
        parser.add_argument(
            '--lesson',
            dest='lesson',
            help='Lesson for data.'
        )

    def print_info(self, template='', context=None):
        if self.input_options['print']:
            context = context or {}
            print str(template).format(**context)

    def handle(self, *args, **options):

        self.input_options = options

        if not options['level']:
            raise CommandError("Option `--level=...` must be specified.")

        if not options['lesson']:
            raise CommandError("Option `--lesson=...` must be specified.")

        if not options['file']:
            raise CommandError("Option `--file=...` must be specified.")

        file_path = os.path.join(settings.BASE_DIR,
                                 'data/{f}'.format(f=options['file']))

        if not os.path.isfile(file_path):
            raise CommandError("File does not exist at the specified path.")

        try:
            library = Library.objects.get(level=options['level'],
                                          lesson=options['lesson'])
        except ObjectDoesNotExist:
            library_serializer = LibrarySerializer(data=options)
            if library_serializer.is_valid():
                library_serializer.save()
                library = Library.objects.get(pk=library_serializer.data['id'])
            else:
                raise CommandError(library_serializer.errors)

        with open(file_path) as dict_file:
            csv_data = csv.DictReader(dict_file)
            for row in csv_data:
                row['english'] = row['english'].lower()
                self.print_info('***\n{english}', row)
                try:
                    vocabulary = Word.objects.get(english=row['english'])
                    self.print_info('{english} - lexicon already exist', row)
                    vocabulary.library.add(library)
                    vocabulary.save()
                except ObjectDoesNotExist:
                    row['translate'] = row['translate'].decode('utf-8')
                    row['library'] = [library.id, ]
                    vocabulary_serializer = DictionarySerializer(data=row)
                    if vocabulary_serializer.is_valid():
                        vocabulary_serializer.save()
                    else:
                        self.print_info('error - {error}', dict(
                            word=row['english'],
                            error=vocabulary_serializer.errors))
