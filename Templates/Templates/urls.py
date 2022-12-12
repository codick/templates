from django.urls import path, include
from temp_app import views

about = [
    path('', views.about)
]

urlpatterns = [
    path('', views.index),
    path('about/', include(about)),
    path('contacts/', views.contacts),
    path('', views.forms)
]
