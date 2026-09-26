*** Keywords ***
Log Test Start
    Log    Test started

Log Test End
    Log    Test finished

Verify Text
    [Arguments]    ${actual}    ${expected}
    Should Be Equal    ${actual}    ${expected}
