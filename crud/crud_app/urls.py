
from django.urls import path
from . import views

urlpatterns = [

path('', views.create, name='create'),
path('display/', views.display, name='display'),
path('<int:id>', views.create, name='update'),
path('delete/<int:id>', views.delete, name='delete')

]
