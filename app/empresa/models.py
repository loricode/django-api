from django.db import models

class Persona(models.Model):
	
   nombre = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
   apellido = models.CharField(blank=True, max_length=100, verbose_name='Apellido')
   
   def __str__(self):
       return 'nombre:%s, apellido:%s'%(self.nombre, self.apellido)
               
		
		
   class Meta:
       ordering = ['nombre']
       verbose_name = 'Persona'
       verbose_name_plural = 'Personas'	

#python app/manage.py makemigrations
#python app/manage.py migrate 
#debe crear la base de datos para que puedan migrar as tablas       