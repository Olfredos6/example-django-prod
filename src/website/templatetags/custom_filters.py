from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def makestars(rating):
    rating = round(rating)
    return format_html(
        "\n{}",
        mark_safe(
            '<i class="fas fa-star"></i>' * rating
            + '<i class="fas fa-star" style="color:#f2f2f2"></i>' * (5 - rating)
        ),
    )


@register.filter
def flatten_qs_on(queryset, attribute):
    """Takes a queryset and returns a string from flattenning the queryset on <atribute>
    """
    return ", ".join(queryset.values_list(attribute, flat=True))
