from django import template
import re


register = template.Library()


@register.filter(name='numeric')
def numeric(value):
    # Remove caracteres não numéricos
    cleaned_value = re.sub(r'\D', '', value)
    # Adiciona "55" antes do número
    return f"55{cleaned_value}"


@register.filter
def format_currency(value):
    if value is None:
        return "R$ 0,00"
    try:
        value = float(value)
        return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except (ValueError, TypeError):
        return "R$ 0,00"
