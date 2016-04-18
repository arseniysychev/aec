import random
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class CustomManager(models.Manager):
    def random_item(self, ids):
        print len(ids)
        random_item = None
        while ids and not random_item:
            random_id = random.choice(ids)
            try:
                random_item = self.get(pk=random_id)
            except ObjectDoesNotExist:
                ids.pop(random_id)
                if not self.filter(pk__in=ids).count():
                    return None
        return random_item
