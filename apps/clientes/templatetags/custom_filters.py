from django import template
import re


register = template.Library()


@register.filter(name='numeric')
def numeric(value):
    # Remove caracteres não numéricos
    cleaned_value = re.sub(r'\D', '', value)
    # Adiciona "55" antes do número
    return f"55{cleaned_value}"
