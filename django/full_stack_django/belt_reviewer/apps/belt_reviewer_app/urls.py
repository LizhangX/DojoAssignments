from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^success$', views.success, name="success"),
    url(r'^books/add$', views.display_add, name="display_add"),
    url(r'^books/add_books$', views.add, name="add"),
    url(r'^books/add_review/(?P<book_id>\d+)$', views.add_review, name="add_review"),
    url(r'^books/(?P<book_id>\d+)$', views.book, name="book"),
    url(r'^books/delete/(?P<review_id>\d+)$', views.delete_review, name="delete_review"),
    url(r'^users/(?P<user_id>\d+)$', views.view_user, name="view_user"),
]