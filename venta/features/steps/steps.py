from behave import *
from facturas import *

@given('a {values} to show')
def step_impl(context, values):
    context.app = Venta()
    context.values = values.split(',')

@when('the app show the products')
def step_impl(context):
    context.total = context.Venta.realizarVenta(String(context.values[0]),String(context.values[1]))

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.total == total)

