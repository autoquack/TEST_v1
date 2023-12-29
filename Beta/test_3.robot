*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser    https://stackoverflow.com/    Chrome
Suite Teardown    Close Browser

*** Test Cases ***
Test Website 1
    Go To     https://meta.stackoverflow.com/
    Sleep    5 seconds
    Log    Do test with same session cookies.