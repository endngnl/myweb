from django.conf.urls import url
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/', views.about),
    url(r'^kontak-abi/', views.kontak_abi),
    url(r'^blog/', views.blog),
    url(r'^date/', views.date),
        
]
