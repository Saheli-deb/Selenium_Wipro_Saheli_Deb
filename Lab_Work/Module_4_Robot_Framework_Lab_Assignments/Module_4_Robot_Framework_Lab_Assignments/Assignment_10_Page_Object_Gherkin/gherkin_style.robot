*** Settings ***
Resource    pages/login_page.resource

*** Keywords ***
Given User Opens Login Page
    Open Login Page

When User Logs In With Valid Credentials
    Enter Username    standard_user
    Enter Password    secret_sauce
    Click Login

Then Inventory Page Is Displayed
    Location Should Contain    inventory.html

*** Test Cases ***
Valid Login Flow
    Given User Opens Login Page
    When User Logs In With Valid Credentials
    Then Inventory Page Is Displayed
    [Teardown]    Close Login Browser
