from django.urls import path
from web.views import index ,detailed, create

app_name = "web"


urlpatterns = [
    path('',index,name="index"),
    path('detailed/',detailed,name="detailed"),
    path('create/',create,name="create")
]