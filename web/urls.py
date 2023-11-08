from django.urls import path
from web.views import index ,detailed, create, delete

app_name = "web"


urlpatterns = [
    path('',index,name="index"),
    path('detailed/<uuid:uuid>/',detailed,name="detailed"),
    path('delete/<uuid:uuid>/',delete,name="delete"),
    path('create/',create,name="create")
]