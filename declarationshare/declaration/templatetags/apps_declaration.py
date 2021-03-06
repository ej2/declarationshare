from django import template
from django.template.loader import render_to_string

from declarationshare.declaration.models import Declaration

register = template.Library()


@register.simple_tag()
def top_declarations():
    declarations = Declaration.objects.filter(nsfw=False).order_by("-date_created")

    return render_to_string("declaration/_list.html", {
        "declarations": declarations,
    })


@register.simple_tag()
def featured_declaration():
    declaration = Declaration.objects.all()[0]

    return declaration
