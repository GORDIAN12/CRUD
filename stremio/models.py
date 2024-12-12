from django.db import models

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombreE = models.CharField(max_length=100, verbose_name='NOMBRE')
    cedula = models.CharField(max_length=100, verbose_name='CURP')
    especialidad = models.CharField(max_length=20, verbose_name="ESPECIALIDAD")
    usuario = models.CharField(max_length=30, verbose_name='USUARIO', default="UNKNOWN")
    curp2 = models.CharField(max_length=30, verbose_name='CURP2', default="UNKNOWN")

    def __str__(self):
        fila='CEDULA: '+self.cedula+'-'+'NOMBRE: '+self.nombreE+'ESP: '+self.especialidad
        return fila

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='NOMBRE')
    curp = models.CharField(max_length=100, verbose_name='CURP')
    telefono = models.CharField(max_length=20, verbose_name="NUMERO CELULAR") 
    especialidad = models.CharField(max_length=20, verbose_name="ESPECIALIDAD")

    def __str__(self):
        fila='CURP: '+self.curp+'-'+'NOMBRE: '+self.nombre+'ESP: '+self.especialidad
        return fila
