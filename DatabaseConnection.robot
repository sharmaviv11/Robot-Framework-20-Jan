*** Settings ***
Documentation    Suite description
Library     OperatingSystem
Library     String
Library     SeleniumLibrary
Library     BuiltIn
Library     Collections
Library     DatabaseLibrary
Library     Sql.py

*** Variables ***
${Driver}           SQLServer
${DB_NAME}          AcQuireODO
${DB_USER_NAME}     APAC\sharvive
${DB_SERVER_NAME}   OLPOTAQRO2
${DB_HOST}          10.239.21.101
${DB_PORT}          60874


*** Test Case ***
TC1
    Connect with SQL

#TC2
#    run sql

*** Keywords ***
Connect with SQL
#    [Tags]  Default
#    Connect To Database     pymssql     ${DB_SERVER_NAME}      ${DB_NAME}     ${DB_USER_NAME}     ${DB_HOST}     ${DB_PORT}
#    Connect To Database     pymssql     ${Driver}       ${DB_SERVER_NAME}      ${DB_NAME}
    ${data}=    database
    ${list}=    database_list
    get line count      ${data}


#run sql
#    database
