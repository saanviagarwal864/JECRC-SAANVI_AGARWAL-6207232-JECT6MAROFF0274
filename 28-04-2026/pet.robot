*** Settings ***
Library       RequestsLibrary   #methods to connect to API
Library    Collections  #methods to work with lists and dictionaries
Library    JSONLibrary  #methods to work with JSON data

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${BASE_URL}  verify=True

    ${payload}=    Load Json From File    ${CURDIR}/../data/add_pet.json

    ${response}=  POST On Session    petapi   /pet   json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200

    Set Suite Variable    ${PET_ID}    ${response.json()}[id]

    Log To Console    ${response.json()}

Update an existing pet
    [Documentation]    Update an existing pet in the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=    Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=  PUT On Session    petapi   /pet   json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Find pet by ID
    [Documentation]    Find pet by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session    petapi   /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
    
Find pets by status
    [Documentation]    Find pets by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=  Create Dictionary    status=available
    ${response}=  GET On Session    petapi   /pet/findByStatus   params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
    
Upload an image
    [Documentation]    Upload an image for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary    additionalMetadata=Blue's image
    ${file_path}=  Set Variable      ${CURDIR}/../data/blue.jpg
    ${file}=  Evaluate    {'file': open($file_path, 'rb')}

    ${response}=  POST On Session    petapi   /pet/${PET_ID}/uploadImage
    ...  data=${form_data}
    ...  files=${file}

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Update pet with form data
    [Documentation]    Update a pet in the store with form data
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=  Create Dictionary    name=Sheero   status=available

    ${response}=  POST On Session    petapi   /pet/${PET_ID}
    ...  data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Delete pet
    [Documentation]    Delete a pet from the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  DELETE On Session    petapi   /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}
    