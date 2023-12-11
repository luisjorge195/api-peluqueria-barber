from django.urls import path
from myapp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reservar_turno', views.reservar_turno)
]