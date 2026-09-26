*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Login With Valid Data
    [Template]    Login
    standard_user    secret_sauce

*** Keywords ***
Login
    [Arguments]    ${username}    ${password}
    Open Browser    https://www.saucedemo.com/    chrome
    Input Text    id=user-name    ${username}
    Input Password    id=password    ${password}
    Click Button    id=login-button
    Location Should Contain    inventory.html
    [Teardown]    Close All Browsers
