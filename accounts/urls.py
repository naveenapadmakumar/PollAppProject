from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import LoginView, RegisterView

urlpatterns=[
path('signup/', RegisterView.as_view(), name='signup'),
path('login/',LoginView.as_view(),name='login'),
path('logout/', views.logout, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)