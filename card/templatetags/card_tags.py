from django import template
from card.models import Card, BOXES

register = template.Library()

@register.inclusion_tag("card/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "box_number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes}