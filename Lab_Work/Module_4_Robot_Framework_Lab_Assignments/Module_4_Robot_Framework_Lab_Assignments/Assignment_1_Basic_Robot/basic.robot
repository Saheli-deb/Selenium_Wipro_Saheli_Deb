*** Settings ***
Documentation    Basic Robot Framework lab assignment

*** Test Cases ***
Verify Basic Calculation
    ${result}=    Evaluate    10 + 20
    Should Be Equal As Integers    ${result}    30
    Log    Basic Robot Framework test passed
