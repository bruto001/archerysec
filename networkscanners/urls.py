from django.conf.urls import url
from . import views

app_name = 'networkscanners'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vul_details/', views.scan_vul_details, name='vul_details'),
    url(r'^launch_scan', views.launch_scan, name='launch_scan'),
    url(r'^scan_del', views.scan_del, name='scan_del'),
    url(r'^ip_scan', views.ip_scan, name='ip_scan'),
    url(r'^ip_table', views.ip_scan_table, name='ip_scan_table'),
    url(r'^openvas_setting', views.openvas_setting, name='openvas_setting'),
    url(r'^openvas_details', views.openvas_details, name='openvas_details'),
]