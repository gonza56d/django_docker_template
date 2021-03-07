# Django
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('encasa.index.urls', 'index'), namespace='index')),
]
