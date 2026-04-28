*** Settings ***
Library       RequestsLibrary   #methods to connect to API
Library    Collections  #methods to work with lists and dictionaries

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Pet inventories
    [Documentation]    Get pet inventories by status
    Create Session    petapi    ${BASE_URL}  verify=True
    
    ${response}=    GET On Session    petapi    /store/inventory

    Should Be Equal As Integers    ${response.status_code}    200
    
    ${body}=    Set Variable    ${response.json()}

    Log To Console     ${body}
    Log To Console    ${response.status_code}

Place order
    [Documentation]    Place an order for a pet
    Create Session    petapi    ${BASE_URL}  verify=True

    ${payload}=    Create Dictionary
    ...  id=12366
    ...  petId=66321
    ...  quantity=1
    ...  shipDate=2026-04-28T07:01:08.754Z
    ...  status=placed
    ...  complete=true

    ${response}=    POST On Session    petapi    /store/order   json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    
    Should Be Equal As Integers    ${body}[id]   12366
    Should Be Equal As Strings    ${body}[status]   placed

    Log To Console     ${body}
    Log To Console    ${response.status_code}

    Set Suite Variable    ${ORDER_ID}    ${body}[id]

Find purchase order by ID
    [Documentation]    Find purchase order by ID
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=    GET On Session    petapi    /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}

    Should Be Equal As Integers    ${body}[id]   ${ORDER_ID}
    Should Be Equal As Strings    ${body}[status]   placed

    Log To Console     ${body}
    Log To Console    ${response.status_code}

Delete purchase order by ID
    [Documentation]    Delete purchase order by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    DELETE On Session    petapi    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}

E2E
    Create Session    e2eapi    ${BASE_URL}  verify=True
    ${payload}=    Create Dictionary
    ...  id=1216
    ...  petId=66311
    ...  quantity=1        
    ...  shipDate=2026-04-28T07:01:08.754Z
    ...  status=placed
    ...  complete=true    
    ${res1}=    POST On Session    e2eapi    /store/order   json=${payload}
    Should Be Equal As Integers    ${res1.status_code}    200
    ${body}=    Set Variable    ${res1.json()}
    Set Suite Variable    ${ORD_ID}    ${body}[id]
    Log To Console    Created order with id ${ORD_ID}
    
    GET On Session    e2eapi    /store/order/${ORD_ID}
    ${res2}=    GET On Session    e2eapi    /store/order/${ORD_ID}
    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    Found order with id ${ORD_ID}
    
    ${res3}=    DELETE On Session    e2eapi    /store/order/${ORD_ID}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    Deleted order with id ${ORD_ID}

    Log To Console    E2E test completed successfully