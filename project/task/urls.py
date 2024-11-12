from django.urls import path
from . import views
urlpatterns = [

    path('addToTask',views.addToTask,name="addToTask"),
    path('editTask/<int:id>',views.editTask,name="editTask"),
    path('deleteTask/<int:id>',views.deleteTask,name="home"),

]