from django.shortcuts import render

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
    fields = '__all__'

    template_name = "declaration/manage.html"
    #form_class = DeclarationForm

    def form_valid(self, form):
        self.object = form.save()

        return render(self.request, 'declaration/create_success.html', {'news': self.object})
