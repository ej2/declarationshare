from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from declarationshare.declaration.forms import DeclarationForm
from declarationshare.declaration.models import Declaration
from django.views.generic import DetailView, CreateView


class DeclarationDetailView(DetailView):
    model = Declaration
    template_name = "declaration/detail.html"

    context_object_name = "declaration"
    pk_url_kwarg = "declaration_id"


class DeclarationCreateView(CreateView):
    model = Declaration
    form_class = DeclarationForm
    template_name = "declaration/manage.html"

    def form_valid(self, form):
        self.object = form.save()

        return redirect(reverse("declaration:detail", args=[self.object.pk]))
