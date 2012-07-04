from django.conf.urls import patterns, url

urlpatterns = patterns('firstclass.views',
    url(r'^(?P<key>.{40})/$', 'view_message_online', name='view_message_online'),
)
