from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.models import TagBase, GenericTaggedItemBase


class IconColorTag(TagBase):
    classification = models.CharField(max_length=100)
    color = models.CharField(max_length=8, default="FFFFFF")
    icon = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class TagAttributes(models.Model):
    tag = models.ForeignKey(IconColorTag, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return ':'.join([self.name, self.value])


class TagClassification(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class TaggedThing(GenericTaggedItemBase):
    # TaggedWhatever can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects.
    tag = models.ForeignKey(
        IconColorTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )
