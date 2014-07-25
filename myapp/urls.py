from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                        url(r'^autocomplete/$',PersonCompleteView.as_view(),name='person_auto_complete'),
                        url(r'^add/$', ProjectAddView.as_view(),
                        name='project_add'),)
