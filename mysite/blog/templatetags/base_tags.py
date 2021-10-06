from django import template

from blog.models import BlogBrand


register = template.Library()

@register.inclusion_tag("blog/tags/blog_brand.html", takes_context=True)
def blog_brand(context):
    return {
        "request": context["request"],
        "blog_brand": BlogBrand.objects.first()
    }
