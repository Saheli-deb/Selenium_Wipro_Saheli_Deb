*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Selenium Home
    Open Browser    https://www.selenium.dev/    chrome

Verify Home Page
    Title Should Be    Selenium

Close Browser Session
    Close All Browsers

*** Test Cases ***
Keyword Driven Demo
    Open Selenium Home
    Verify Home Page
    [Teardown]    Close Browser Session
