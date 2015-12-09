from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from declarationshare.declaration.forms import DeclarationForm
from declarationshare.declaration.models import Declaration
from django.views.generic import DetailView, CreateView, ListView


class DeclarationDetailView(DetailView):
    model = Declaration
    template_name = "declaration/detail.html"

    context_object_name = "declaration"
    pk_url_kwarg = "declaration_id"


class BaseDeclarationCreateView(CreateView):
    model = Declaration
    form_class = DeclarationForm

    def form_valid(self, form):
        self.object = form.save()

        return redirect(reverse("declaration:detail", args=[self.object.pk]))


class IAmCreateView(BaseDeclarationCreateView):
    template_name = "declaration/new_am.html"

    def get_form_kwargs(self):
        kwargs = super(IAmCreateView, self).get_form_kwargs()
        kwargs['declare_type'] = "AM"
        return kwargs


class IWillCreateView(BaseDeclarationCreateView):
    template_name = "declaration/new_will.html"

    def get_form_kwargs(self):
        kwargs = super(IWillCreateView, self).get_form_kwargs()
        kwargs['declare_type'] = "WILL"
        return kwargs


class DeclarationListView(ListView):
    context_object_name = 'declarations'
    template_name = "declaration/list.html"
    paginate_by = 100

    def get_queryset(self):
        return Declaration.objects.filter(nsfw=False)


class NSFWDeclarationListView(ListView):
    context_object_name = 'declarations'
    template_name = "declaration/list.html"
    paginate_by = 100

    def get_queryset(self):
        return Declaration.objects.filter(nsfw=True)
