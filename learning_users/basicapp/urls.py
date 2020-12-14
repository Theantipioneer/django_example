from basicapp import views
from django.conf.urls import url

#TEMPLATE URLS!

app_name = "basicapp"

urlpatterns = [
    url("register/",views.register, name = "register" ),
    # url("basicapp/abc.html", ),
    # url("basicapp/abc.html", ),
]