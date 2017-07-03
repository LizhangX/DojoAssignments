from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),

    url(r'^travels$', views.success, name="success"),
    url(r'^travels/join/(?P<plan_id>\d+)$', views.join, name="join"),


    url(r'^travels/destination/(?P<plan_id>\d+)$', views.destination, name="destination"),

    url(r'^travels/add$', views.display_add, name="display_add"),
    url(r'^travels/add_plan$', views.add_plan, name="add_plan"),



]