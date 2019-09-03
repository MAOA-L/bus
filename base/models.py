import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True, default=uuid.uuid1)
    gmt_create = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, )
    gmt_modified = models.DateTimeField(verbose_name="最后更新时间", auto_now=True, )
    is_active = models.BooleanField(verbose_name='是否有效', default=True)

    class Meta:
        abstract = True
