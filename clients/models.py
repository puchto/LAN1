from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Auth_record(models.Model):
    loc_file = models.CharField(max_length = 50)
    cl_address = models.CharField(max_length = 50)
    mac = models.CharField(max_length = 17)
    ip_add = models.CharField(max_length = 15)
    kl_service = models.CharField(max_length = 1)
    downl = models.CharField(max_length = 6)
    upl = models.CharField(max_length = 6)
    
    class Meta:
        db_table = "LAN_Sosnowiec_klienci"
        
    def __str__(self):
        return self.cl_address
