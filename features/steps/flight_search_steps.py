from behave import given, when, then
from behave.log_capture import capture


@given("the user is on search page")
def user_on_search_page(context):
    context.web.open("http://blazedemo.com/")


@when("user selects Paris as departure city")
def user_select_departure_city(context):
    context.web.find_by_xpath("//select[@name='fromPort']/option[text()='Paris']").click()

@when("user selects London as destination city")
def user_select_destination_city(context):
    context.web.find_by_xpath("//select[@name='toPort']/option[text()='London']").click()

@when("clicks on Find Flights button")
def user_clicks_on_find_flights(context):
    context.web.find_by_xpath("//input[@type='submit']").click()

@then("flights are found")
def flights_are_found(context):
    elements = context.web.finds_by_xpath("//table/tbody/tr")
    assert len(elements) > 1