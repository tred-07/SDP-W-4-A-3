from django.urls import path,include
from .views import addCategory
urlpatterns = [
    path('addCategory/',addCategory,name='addToCategory')
]
