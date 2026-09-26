*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Documentation
    Open Browser    https://www.selenium.dev/    chrome
    Click Link    Documentation
    Wait Until Page Contains    Selenium Documentation
    [Teardown]    Close All Browsers
