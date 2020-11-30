from behave import *
from venta import *

@given('a {products} to show')
def step_impl(context, values):
    context.venta = Venta()
    context.products = products.split(',')

@when('Bill show the products')
def step_impl(context):
    context.total = context.venta.realizarVenta(String(context.values[0]),String(context.values[1]))

@then('the {total:d} of products')
def step_impl(context, total):
    assert (context.total == total)

