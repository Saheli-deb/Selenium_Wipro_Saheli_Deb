*** Settings ***
Resource    resources/common.resource
Suite Setup    Log Test Start
Suite Teardown    Log Test End
Test Setup    Log    Test setup
Test Teardown    Log    Test teardown

*** Test Cases ***
Resource And Lifecycle Demo
    Verify Text    Robot    Robot
