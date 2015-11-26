# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.DeclarationCreateView.as_view(), name="new"),
    url(
        regex=r'^(?P<declaration_id>[\w.@+-]+)/$',
        view=views.DeclarationDetailView.as_view(),
        name='detail'
    ),

]
