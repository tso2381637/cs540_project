from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'cid'),
    ('2', 'city'),
    ('3', 'latitude'),
    ('4', 'longitude'),
    ('5', 'street_name'),
('6', 'injured_count'),
('7', 'crash_time'),
)

# Create your models here.

class AllCleanedCrashData(models.Model):
    cid = models.BigIntegerField(verbose_name="cid")
    city = models.TextField(verbose_name="city")
    latitude = models.FloatField(verbose_name="latitude",max_length=8 ,blank=True, null=True)
    longitude = models.FloatField(verbose_name="longitude",max_length=8, blank=True, null=True)
    street_name = models.TextField(verbose_name="streetName", blank=True, null=True)
    injured_count = models.TextField(verbose_name="injuredCount", blank=True, null=True)
    crash_time = models.DateTimeField(verbose_name="crashTime", blank=True, null=True)

class WeaTest(models.Model):
    id = models.BigIntegerField(verbose_name="id",primary_key=True)
    cond1 = models.CharField(db_column='cond1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cond2 = models.CharField(db_column='cond2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cond3 = models.CharField(db_column='cond3', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wea_test'



def query_data_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = AllCleanedCrashData.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(cid__icontains=search_value)|
                                        Q(city__icontains=search_value) |
                                        Q(latitude__icontains=search_value) |
                                        Q(longitude__icontains=search_value)|
                                        Q(street_name__icontains=search_value) |
                                        Q(injured_count__icontains=search_value) |
                                        Q(crash_time__icontains=search_value)

        )

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }