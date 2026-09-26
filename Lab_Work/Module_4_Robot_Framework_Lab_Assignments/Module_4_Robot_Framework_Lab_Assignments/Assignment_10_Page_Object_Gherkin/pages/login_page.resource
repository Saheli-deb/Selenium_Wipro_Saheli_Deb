*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Login Page
    Open Browser    https://www.saucedemo.com/    chrome

Enter Username
    [Arguments]    ${username}
    Input Text    id=user-name    ${username}

Enter Password
    [Arguments]    ${password}
    Input Password    id=password    ${password}

Click Login
    Click Button    id=login-button

Close Login Browser
    Close All Browsers
