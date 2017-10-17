from django.conf.urls import url
from . import views

app_name = "message_board"
urlpatterns = [
    # ex: /message_board/
    url(r'^$', views.IndexView.as_view(), name="index"),
    # ex: /message_board/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail")
]
