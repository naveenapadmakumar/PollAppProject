from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path


urlpatterns= [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
