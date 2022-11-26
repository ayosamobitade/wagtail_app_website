from django.db import models

# Create your models here.

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChoosePanel
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag

class BlogPage(Page):
    description = models.Charfield(max_length = 255, blank = True,)
    content_panels = Page.content_panels + [FieldPanel("description", classname = 'full')]


    class PostPage(Page):
        header_mage = models.Foreignkey('wagtailimages.Image', null = True, on_delete = models.SET_NULL, related_name = '+', )
        conntent_panels = Pages.content_panels + [ImagesChooserPanel('header_image'),]


@register_snippet
class BlogCategory(models.Models):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, max_length = 80)

    panels = [
        FieldPanel('name'),
        FiledPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plura = 'Categories'


@register_snippet
class Tag(TaggitTag):
    class Meta:
        Proxy = True