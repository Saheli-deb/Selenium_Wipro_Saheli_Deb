*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}        https://www.selenium.dev/

*** Test Cases ***
Parameterized Browser Test
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Selenium
    [Teardown]    Close All Browsers
