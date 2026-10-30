from django.db import models

class Tree(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    tree_name = models.CharField(max_length=200, null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    zone = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        app_label = 'trees'  # Hii inatatua lile kosa la RuntimeError moja kwa moja!

    def __str__(self):
        return f"{self.tree_name or 'Mti usio na Jina'} ({self.serial_number})"
