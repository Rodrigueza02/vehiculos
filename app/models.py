from django.db import models
# Create your models here.
class vehicle(models.Model):
    COLOR=(
        ('1','ROJO'),
        ('2','AZUL'),
        ('3','VERDE'),
        ('4','NEGRO'),
    )
    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color_vehiculo=models.CharField('color',max_length=1,choices=COLOR)
    modelo=models.IntegerField()
    
    
    def _str_(self):
        return self.placa
