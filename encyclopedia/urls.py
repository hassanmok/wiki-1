from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name='entry'),
    path("search/", views.search, name='search'),
    path("Create_New_Page/", views.Create_New_Page, name='Create_New_Page'),
    path("edit/", views.edit, name='edit'),
    path("new_edit/", views.new_edit, name='new_edit'),
    path("random/", views.random_entry, name='random')
]
