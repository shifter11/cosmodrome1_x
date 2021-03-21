
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'music'),
    path('filmmaking', views.filmmaking, name = 'film'),
    path('contact', views.contact_us, name = 'contacts')
]
