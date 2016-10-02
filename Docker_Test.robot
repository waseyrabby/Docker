*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    [Tags]    test_001_search_with_ivalid_keyword
    Provided precondition
    When
    Then
    [Tags]    test__002_Verify_docker_website_title_url
    Provided precondition
    When
    Then
    [Tags]    test_001_search_with_ivalid_keyword
    Provided precondition
    When
    Then
    [Tags]    test_003_docker_signup
    Provided precondition
    When
    Then
    [Tags]    test_001_search_with_ivalid_keyword
    Provided precondition
    When
    Then
    [Tags]    test_001_search_with_ivalid_keyword
    Provided precondition
    When
    Then
    [Tags]    test_001_search_with_ivalid_keyword
    Provided precondition
    When
    Then
*** Keywords ***
Provided precondition
    Setup system under test