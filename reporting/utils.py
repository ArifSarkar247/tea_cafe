from ingredients.models import Ingredient
from usage.models import DailyUsage
from .models import DailyReport
from django.db.models import Sum
from decimal import Decimal

# Define how many grams/liters needed for 1 cup
PER_CUP_REQUIREMENTS = {
    'milk': Decimal('0.1'),   # 0.1 liter = 100 ml
    'sugar': Decimal('0.01'), # 0.01 kg = 10 gm
    'tea': Decimal('0.01'),   # 0.01 kg = 10 gm
}

CUP_PRICE = Decimal('15.00')  # income per cup

def calculate_daily_report(for_date):
    usages = DailyUsage.objects.filter(date=for_date).select_related('ingredient')

    usage_dict = {}
    total_expense = Decimal('0.00')

    for usage in usages:
        key = usage.ingredient.name.lower()
        usage_dict[key] = usage.quantity_used
        total_expense += usage.quantity_used * usage.ingredient.cost_per_unit

    try:
        milk_cups = usage_dict.get('milk', Decimal('0')) / PER_CUP_REQUIREMENTS['milk']
        sugar_cups = usage_dict.get('sugar', Decimal('0')) / PER_CUP_REQUIREMENTS['sugar']
        tea_cups = usage_dict.get('tea', Decimal('0')) / PER_CUP_REQUIREMENTS['tea']
        total_cups = int(min(milk_cups, sugar_cups, tea_cups))
    except ZeroDivisionError:
        total_cups = 0

    total_income = CUP_PRICE * total_cups
    profit = total_income - total_expense

    # Save or update the report
    DailyReport.objects.update_or_create(
        date=for_date,
        defaults={
            'total_cups': total_cups,
            'total_income': total_income,
            'total_expense': total_expense,
            'profit': profit,
        }
    )


# PDF rendering using xhtml2pdf
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

