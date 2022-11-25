from django.db import models

# Create your models here.
class Consulta(models.Model):
   id= models.AutoField(primary_key=True)
   cliente= models.CharField(max_length=35)
   consulta=models.CharField(max_length=240)
   def __str__(self):
       return str(self.id)+" "+self.cliente
class Respuesta(models.Model):
   id= models.AutoField(primary_key=True)
   id_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
   tecnico= models.CharField(max_length=100)
   respuesta=models.CharField(max_length=240)

   def __str__(self):
       return str(self.id)+" "+self.tecnico

class User(models.Model):
   id= models.AutoField(primary_key=True)
   user = models.CharField(max_length=100)
   password= models.CharField(max_length=100)
   rol=models.CharField(max_length=50)