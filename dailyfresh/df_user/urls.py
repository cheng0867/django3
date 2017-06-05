from django.conf.urls import url
import views

urlpatterns = [
    url('^login$',views.login),
    url('^register$',views.login),
]