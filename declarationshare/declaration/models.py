from django.db import models
from django_extensions.db import fields

from declarationshare.users.models import User

DELCARATION_TYPE = (
    ("WILL", "I will",),
    ("AM", "I am",),
)

FREQUENCY = (
    ("D", "daily",),
    ("W", "weekly",),
    ("M", "monthly",),
    ("Y", "yearly",),
    ("N", "never",),
)


class Declaration(models.Model):
    text = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=4, null=False, choices=DELCARATION_TYPE)
    date_created = fields.CreationDateTimeField(editable=True)
    reminder_frequency = models.CharField(max_length=1, default="N")
    user = models.ForeignKey(User, null=True, blank=True, related_name="declarations")

    anonymous = models.BooleanField(default=False)
    nsfw = models.BooleanField(default=False)
    author = models.CharField(max_length="50", null=True)

    ip_address = models.CharField(max_length=45, null=True, blank=True)

    def __unicode__(self):
        return "{0} {1}".format(self.get_type_display(), self.text)

    def display_author(self):
        if self.anonymous:
            return "Anonymous"
        else:
            return self.author
