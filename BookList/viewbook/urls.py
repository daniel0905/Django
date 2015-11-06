from django.conf.urls import url
from viewbook import views

urlpatterns = [
    url(r'^page(?P<page>[0-9]+)/', views.ViewListBook.as_view(), name="viewlistbook"),
    url(r'^', views.ViewListBook.as_view(), name="viewlistbook1")
]