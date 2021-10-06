from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass

# --- Blog
#---------
# import datetime

# from django.utils.translation import ugettext_lazy as _
# from wagtail.core.fields import StreamField
# from wagtail.core.blocks import RichTextBlock
# from wagtail.images.blocks import ImageChooserBlock
# from wagtail.embeds.blocks import EmbedBlock
# from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
# from modelcluster.fields import ParentalKey
# from modelcluster.contrib.taggit import ClusterTaggableManager
# from taggit.models import TagBase, ItemBase


# class BlogCategory(models.Model):
#     name = models.CharField(
#         max_length=80, unique=True, verbose_name=_('Category Name'))
#     slug = models.SlugField(unique=True, max_length=80)
#     parent = models.ForeignKey(
#         'self', blank=True, null=True, related_name="children",
#         help_text=_(
#             'Categories, unlike tags, can have a hierarchy. You might have a '
#             'Jazz category, and under that have children categories for Bebop'
#             ' and Big Band. Totally optional.'),
#         on_delete=models.CASCADE,
#     )
#     description = models.CharField(max_length=500, blank=True)

#     class Meta:
#         abstract = True
#         ordering = ['name']
#         verbose_name = _("Blog Category")
#         verbose_name_plural = _("Blog Categories")

#     panels = [
#         FieldPanel('name'),
#         FieldPanel('parent'),
#         FieldPanel('description'),
#     ]

#     def __str__(self):
#         return self.name

#     def clean(self):
#         if self.parent:
#             parent = self.parent
#             if self.parent == self:
#                 raise ValidationError('Parent category cannot be self.')
#             if parent.parent and parent.parent == self:
#                 raise ValidationError('Cannot have circular Parents.')

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             unique_slugify(self, self.name)
#         return super().save(*args, **kwargs)


# class BlogTag(TagBase):
#     id = models.AutoField(primary_key=True)

#     class Meta:
#         verbose_name = "blog tag"
#         verbose_name_plural = "blog tags"


# class TaggedBlog(ItemBase):
#     id = models.AutoField(primary_key=True)
#     tag = models.ForeignKey(
#         BlogTag, related_name="tagged_blogs", on_delete=models.CASCADE
#     )
#     content_object = ParentalKey(
#         to='BlogPage',
#         on_delete=models.CASCADE,
#         related_name='tagged_items'
#     )


# class BlogPage(Page):

#     body = StreamField(
#         [
#             ("Text", RichTextBlock()),
#             ("Image", ImageChooserBlock()),
#             ("Embeded", EmbedBlock()), 
#         ],
#         blank=True
#     )
#     date = models.DateField(
#         _("Post date"),
#         default=datetime.datetime.today,
#         help_text=_("This date may be displayed on the blog post. It is not "
#                     "used to schedule posts to go live at a later date.")
#     )
#     tags = ClusterTaggableManager(through=TaggedBlog, blank=True)

#     content_panels = Page.content_panels + [
#         StreamFieldPanel("body"),
#         FieldPanel('tags'),
#     ]

#     class Meta:
#         verbose_name = _('Blog page')
#         verbose_name_plural = _('Blog pages')
