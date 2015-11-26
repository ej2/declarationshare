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
    template_name = "declaration/manage.html"
    form_class = DeclarationForm

