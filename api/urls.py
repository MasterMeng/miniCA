from django.urls import path
from .import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetial.as_view()),
    path('keys', views.KeyList.as_view()),
    path('keys/<int:pk>', views.KeyDetial.as_view()),
    path('csrs', views.CSRList.as_view()),
    path('csrs/<int:pk>', views.CSRDetial.as_view()),
    path('certs', views.CertList.as_view()),
    path('certs/<int:pk>', views.CertDetial.as_view()),
]
