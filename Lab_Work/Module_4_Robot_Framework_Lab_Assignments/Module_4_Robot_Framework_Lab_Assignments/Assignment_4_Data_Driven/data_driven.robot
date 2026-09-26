*** Test Cases ***
Validate Multiple Values
    [Template]    Validate Text
    Robot Framework
    Selenium
    Python Automation
    API Testing

*** Keywords ***
Validate Text
    [Arguments]    ${text}
    Should Not Be Empty    ${text}
    Log    Validated: ${text}
