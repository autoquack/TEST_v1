*** Settings ***
Library    OperatingSystem

*** Keywords ***

*** Variables ***

*** Test Cases ***
TEST
    Count Files In Directory

    Run Keyword If    $var_in_py_expr1 == $var_in_py_expr2
    ...    Keyword    @args
    ...  ELSE IF    condition_in_py_expr
    ...    Keyword    @args
    ...  ELSE
    ...    Keyword    @args