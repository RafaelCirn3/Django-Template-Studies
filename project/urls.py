from django.contrib import admin
from django.urls import path, include

#incluse as urls utilizadas pelos seus apps para que sejam utilizadas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultaCEP/', include('apps.consultaCEP.urls'))
]
