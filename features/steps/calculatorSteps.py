from nose.tools import assert_equals
from Calculator import Calculator

@step(u'I am using the calculator')
def select_calc(step):
    print('Attempting to use calculator...')
    calc = Calculator()


@step(u'I input "([^"]*)" add "([^"]*)"')
def given_i_input_group1_add_group1(step, x, y):
    result = world.calc.add(int(x), int(y))


@step(u'I should see "([^"]+)"')
def result(step, expected_result):
    actual_result = result
    assert_equals(int(expected_result), actual_result)

@given(u'I input "2" add "2"')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given I input "2" add "2"')
    pass

@then(u'I should see "4"')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then I should see "4"')
    pass