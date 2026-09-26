*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Selenium Website
    Open Browser    https://www.selenium.dev/    chrome
    Title Should Be    Selenium
    Wait Until Page Contains    Selenium
    [Teardown]    Close All Browsers
