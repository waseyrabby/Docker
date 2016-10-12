*** Settings ***
Documentation     Example test case using the gherkin syntax.
...
...               This test has a workflow similar to the keyword-driven
...               examples. The difference is that the keywords use higher
...               abstraction level and their arguments are embedded into
...               the keyword names.
...
...               This kind of _gherkin_ syntax has been made popular by
...               [http://cukes.info|Cucumber]. It works well especially when
...               tests act as examples that need to be easily understood also
...               by the business people.
Library           Docker.py
*** Test Cases ***
Test title This test will verify no result found when searched with invalid keyword.
    When User setup browser
    Then test 001 search with ivalid keyword
    Then User tearDown Browser

Test title This test will verify the title of docker website.

    When User setup browser
    Then test 002 VERIFY DOCKER WEBSITE TITLE URL
   Then User tearDown Browser

Test title This test will signup new user and show error when existing user try to sign up.

    When User setup browser
    Then test 003 docker signup
    Then User tearDown Browser

Test title This will test login with valid credential.

    When User setup browser
    Then test 004 login valid username valid password
    Then User tearDown Browser

Test title This will test login with invalid user credential.

   When User setup browser
    Then test 005 login ivalid username valid password
    Then User tearDown Browser

Test title This will test login with invalid password credential.

     When User setup browser
    Then test 006 login valid username ivalid password
   Then User tearDown Browser

Test title This will test login with invalid credential.

     When User setup browser
    Then test 007 login ivalid username ivalid password
    Then User tearDown Browser

Test title This test will verify if dounload link is valid.

    When User setup browser
    Then test 008 download mac link
    Then User tearDown Browser

*** Keywords ***

