*** Settings ***
Documentation    Sauce Labs remote execution pattern

*** Variables ***
${SAUCE_URL}    %{SAUCE_REMOTE_URL}
${SAUCE_USER}   %{SAUCE_USERNAME}
${SAUCE_KEY}    %{SAUCE_ACCESS_KEY}

*** Test Cases ***
Remote Browser Configuration
    Log    Remote URL: ${SAUCE_URL}
    Log    Remote user loaded: ${SAUCE_USER}
    Log    Access key is supplied through environment variables
    # Configure provider-specific browser capabilities according
    # to the current Sauce Labs account/project setup.
