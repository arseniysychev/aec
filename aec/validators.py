import enchant
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

en_dict_us = enchant.Dict("en_US")


def is_english(value):
    for item in value.split():
        if item and not en_dict_us.check(item):
            raise ValidationError(
                _('%(value)s is not in English dictionary. '
                  'Please correct %(word)s: %(suggest)s'),
                params={
                    'value': value,
                    'word': item,
                    'suggest': en_dict_us.suggest(item),
                },
            )
