from django.contrib import admin
from .models import Cine
from. models import Venta
from. models import Empleado
from. models import Boleto
from. models import Cliente 
from. models import Proyeccion
from. models import Pelicula 
from. models import Sala

# Register your models here.
admin.site.register(Cine)
admin.site.register(Venta)
admin.site.register(Empleado)
admin.site.register(Boleto)
admin.site.register(Cliente)
admin.site.register(Proyeccion)
admin.site.register(Pelicula)
admin.site.register(Sala)