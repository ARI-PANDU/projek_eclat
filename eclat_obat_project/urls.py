
from django.contrib import admin
from django.urls import path
from eclat_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analisis/', views.analisis, name='analisis'),
    path('kelola-obat/', views.kelola_obat, name='kelola_obat'),
]
