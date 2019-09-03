from django.db import models

from base.models import BaseModel


class Area(BaseModel):
    """区域"""
    name = models.CharField(verbose_name="区域", max_length=32)
    url = models.CharField(verbose_name="url", max_length=255)


class BusInfo(BaseModel):
    area = models.ForeignKey("bus_info.Area", verbose_name="所属区域", max_length=32, on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="信息", max_length=32, unique=True)
    code = models.CharField(verbose_name="供获取站点和实时信息使用", max_length=32)


class BusInfoStation(BaseModel):
    bus = models.ForeignKey("bus_info.BusInfo", verbose_name="bus", on_delete=models.CASCADE,
                            related_name="%(class)s_bus")
    station = models.ForeignKey("bus_info.Station", verbose_name="station", on_delete=models.CASCADE,
                                related_name="%(class)s_station")


class Station(BaseModel):
    name = models.CharField(verbose_name="站名", max_length=32)
