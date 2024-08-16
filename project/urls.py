from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultaCEP/', include('apps.consultaCEP.urls')),
    path('consultaPokemon/', include('apps.consultaPokemon.urls'))
]
