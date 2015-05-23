try:
    from django.conf.urls import url, patterns, include
except ImportError:
    from django.conf.urls.defaults import url, patterns, include

from .views import (
    view_200, view_201, view_302, view_404, needs_login, data_1,
    data_5,
)


urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^view/200/$', view_200, name='view-200'),
    url(r'^view/201/$', view_201, name='view-201'),
    url(r'^view/302/$', view_302, name='view-302'),
    url(r'^view/404/$', view_404, name='view-404'),
    url(r'^view/needs-login/$', needs_login, name='view-needs-login'),
    url(r'^view/data1/$', data_1, name='view-data-1'),
    url(r'^view/data5/$', data_5, name='view-data-5'),
)