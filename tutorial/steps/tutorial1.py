from behave import *

@given(u'I have the number 20')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have the number 20')

@given(u'I have the numer 30')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have the numer 30')

@when(u'I sum the numbers')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I sum the numbers')

@then(u'The result should be 50')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The result should be 50')
