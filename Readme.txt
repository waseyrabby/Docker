Flashpoint Intel QA Coding Exercise

Mission Accepted

Automated 8  test cases for the Docker website using Webdriver and Pyhon.


1.	test__001 search-related test case
2.	test__002 Docker website title and url test case
3.	test__003 Signup related test case
4.	test__004 Login test case with valid username password
5.	test__005 Login test case with invalid username valipassword
6.	test__006 Login test case with valid username invalidpassword
7.	test__007 Login test case with invalid username invalid password
8.	test__008 Download link for mac OS




For Chromedriver to run test You have to set up binary path

chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

or u can do brew install chromedriver given u have homebrew installed.
then just self.driver=webdriver.Chrome().









