*** Settings ***
Documentation   Automation Testing Demo
...             Settings, Test Cases, Variables and Keywords are all different modules
...             'Test Cases' module consists of name of the test case and then business/custom keywords or you can also say child steps
...             Under the 'Keywords' module > business keywords mentioned in the 'Test Case' module needs to be tied up in the form of selenium library keywords
Library     OperatingSystem
Library     String
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     DatabaseLibrary
#Suite Setup     Connect To Database        pymssql     ${DB_NAME}     ${DB_USER_NAME}     ${DB_HOST}     ${DB_PORT}
#Suite Teardown  Disconnect From Database
Resource        DatabaseConnection.robot
#Test Setup      DatabaseConnection.Connect
#Test Teardown   DatabaseConnection.Disconnect

*** Variables ***
${DB_NAME}              AcQuireODO
${DB_USER_NAME}         APAC\sharvive
#${DB_SERVER_NAME}       OLPOTAQRO2
${DB_HOST}              10.239.21.101
${DB_PORT}              60874
${sql}                  select * from dbo.CONTRACT;

*** Test Cases ***
Execute select statement
    ${output}=  execute sql string      ${sql}
    log to console      ${output}       None
    should be equal as strings   ${output}       None


#    cur = mssql.connection.cursor()
#    cur.execute(${sql}




