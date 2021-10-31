from django.db import models
from django.conf import settings
from django.utils import timezone

# PLACES = (
#     (1, 'キッチン下'),
#     (2, '冷蔵庫横'),
#     (3, '洗面台下'),
#     (4, '下駄箱'),
#     (5, 'その他'),
# )


PLACES = (
    (1, 'パントリー'),
    (2, 'キッチン・冷蔵庫'),
    (3, '洗面台下'),
    (4, 'トイレ'),
    (5, 'リビング・たんす'),
    (6, '下駄箱'),
    (7, 'その他'),
)

class Item(models.Model):
    registerer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField("品目", max_length=100)
    place = models.IntegerField(choices=PLACES)
    need = models.BooleanField(verbose_name='補充が必要か',  default=False)
    memo = models.TextField("備考", blank=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.item


# Create your models here.
