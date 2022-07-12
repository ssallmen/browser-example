*** Settings ***
Library    Browser
Library    Page.py

Test Setup     Browser.New Browser    headless=False
Test Teardown  Run Keyword If    '${TEST STATUS}'=='FAIL'    Browser.Take Screenshot    fullPage=True    filename=EMBED

*** Test Cases ***
Get All Field Values
    Browser.New Page    file://${CURDIR}/index.html
    ${input}=    Page.Get Field Value    Text input
    Log To Console    Text input=${input}
    ${area}=    Page.Get Field Value    Text area
    Log To Console    Text area=${area}
    ${delivery_option}=    Page.Get Field Value    Invoice Delivery Method
    Log To Console    Invoice Delivery Method=${delivery_option}
