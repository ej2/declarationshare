# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^/new/am$', views.IAmCreateView.as_view(), name="new_am"),
    url(r'^/new/will$', views.IWillCreateView.as_view(), name="new_will"),
    url(r'^choose/$', TemplateView.as_view(template_name='declaration/choose.html'), name="choose"),
    url(
        regex=r'^list/$',
        view=views.DeclarationListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^nsfw/$',
        view=views.NSFWDeclarationListView.as_view(),
        name='nsfw'
    ),
    url(
        regex=r'^(?P<declaration_id>[\w.@+-]+)/$',
        view=views.DeclarationDetailView.as_view(),
        name='detail'
    ),



]
