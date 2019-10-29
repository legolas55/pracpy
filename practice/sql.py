"""To Do  
"""

import sqlite3

#Helper Functions
def select_all_from_table(tablename, sql_cursor):
    """ Prints all results from a table named tablename.
        Args: table_name - table name to query (Case sensative)
              sql_cursor - sqlite3 cursor object
        Returns: Doesn't return, but will print all results.
    """
    
    sql = "SELECT * FROM {0}".format(tablename)
    sql_cursor.execute(sql)
    # print("fetchall:")
    all_results = sql_cursor.fetchall()
    for result in all_results:
        print(result)

def run_sql_command_return_all_results(command, sql_cursor):
    """ Prints all results of 
    """
    sql_cursor.execute(command)
    # print("fetchall:")
    all_results = sql_cursor.fetchall()
    for result in all_results:
        print(result)

def query_if_table_exists(table_name):
    """ Query if a table exsists in the sqlite)master meta data table.
        Args: table_name - table name to query (Case sensative)
        Returns: Length of the list object that contains the tables that matched.
    """

    SQL_COMMAND="SELECT sql FROM sqlite_master WHERE type='table' AND name ='{0}'".format(table_name)
    CURSOR.execute(SQL_COMMAND)
    all_results = CURSOR.fetchall()
    #print(all_results)
    return(len(all_results))


#Create a database and a connection object
    
CONNECTION = sqlite3.connect("sounds_like_a_gym.db")
CURSOR = CONNECTION.cursor()


#If this file is rerun, the tables will need to be dropped if they exsist since
#the database exsists in a file and not in memory
# Running the database in memory has certain advantanges and disadvantages

if query_if_table_exists("Members"):
           CURSOR.execute("""DROP TABLE Members;""")

if query_if_table_exists("Organization"):
           CURSOR.execute("""DROP TABLE Organization;""")

#Functions to create the Members and Organization tables
           
SQL_COMMAND = """
CREATE TABLE Members (
ID INTEGER PRIMARY KEY,
FIRST_NAME VARCHAR(30),
LAST_NAME VARCHAR(40),
STREET_ADDRESS VARCHAR(100),
APARTMENT_NUMBER VARCHAR(20) DEFAULT NULL,
CITY VARCHAR(50),
STATE VARCHAR(25),
ZIPCODE VARCHAR(10),
PHONE_NUMBER VARCHAR(20),
AGE INT(10));"""

CURSOR.execute(SQL_COMMAND)


SQL_COMMAND = """
CREATE TABLE Organization (
ID INTEGER PRIMARY KEY,
MEMBER_ID VARCHAR(20),
LOCATION VARCHAR(30),
DUES DECIMAL(19,4));"""

CURSOR.execute(SQL_COMMAND)




#Sample Data Table used for testing
MEMBERS_DATA = [("William", "Shakespeare",
                 "1000 Innovation Way",
                 "Apt 400", "Fake London",
                 "Georgia", "33009",
                 "123-456-789", "105"),
                ("John", "Smith",
                 "123 No Work No Eat Drive",
                 "Apt 1", "Fake Plymouth",
                 "Massachusetts", "01810",
                 "978-756-2313", "40"),
                ("Abraham", "Lincoln",
                 "678 Honest Drive",
                 "Apt 200", "Hodgenville",
                 "Kentucky", "2234",
                 "456-874-9432", "200"),
                ("William", "Wallace",
                 "234 BraveHeart Way",
                 "Apt 101", "Scottsdale",
                 "Michigan", "3406",
                 "679-223-1458", "27"),
                ("Amelia", "Earhart",
                 "556 Atlantic Street",
                 "Apt 19", "Pacific",
                 "California", "",
                 "123-111-789", "213"),
                ("Marie", "Curie",
                 "8901 Chemistry Way",
                 "Apt 120", "Amherst",
                 "Virginia", "12345",
                 "876-456-789", "35"),
                ("Boudicca", "",
                 "1000 Britan Way",
                 "Apt 101", "Rome",
                 "Georgia", "11009",
                 "111-222-333", "22"), ]

#Load the sample data into the databse
# I pictured this as a gym member who was signing up for a gym at a specific location.
# The location is in Alpharetta and the dues are 30 if the member is under 65.
# The dues are setup that way so that there would be members with 0 dues.

for member in MEMBERS_DATA:
    members_format_str = (
        'INSERT INTO members(ID, FIRST_NAME,'
        'LAST_NAME, STREET_ADDRESS, APARTMENT_NUMBER,'
        'CITY, STATE, ZIPCODE, PHONE_NUMBER, AGE)'
        'VALUES (NULL, "{first}", "{last}", "{street_address}",'
        '"{apartment_number}", "{city}", "{state}","{zipcode}",'
        '"{phone_number}","{age}");')

    SQL_COMMAND = members_format_str.format(first=member[0],
                                            last=member[1],
                                            street_address=member[2],
                                            apartment_number=member[3],
                                            city=member[4],
                                            state=member[5],
                                            zipcode=member[6],
                                            phone_number=member[7],
                                            age=member[8])
    CURSOR.execute(SQL_COMMAND)

    SQL_COMMAND = "SELECT * FROM members ORDER BY ID DESC LIMIT 1"

    CURSOR.execute(SQL_COMMAND)
    result_insert = CURSOR.fetchone()
    members_table_id = result_insert[0]
    
    gym_location = "Alpharetta"
    gym_dues = 30.00

    if result_insert[-1] > 65:
        gym_dues = 0

    organization_format_str = ('INSERT INTO organization(ID, MEMBER_ID,'
                               'LOCATION, DUES) VALUES (NULL, "{member_id}",'
                               '"{location}", "{dues}");')

    SQL_COMMAND = organization_format_str.format(member_id=members_table_id,
                                                 location=gym_location,
                                                 dues=gym_dues)

    CURSOR.execute(SQL_COMMAND)
    
# See if the tables are filled with the correct data from the sample
# dataset
select_all_from_table("Members", CURSOR)
select_all_from_table("Organization", CURSOR)

# Write a query that lists each member name, address, dues and location.

SQL_COMMAND = (
    'SELECT Members.FIRST_NAME, Members.LAST_NAME, Members.STREET_ADDRESS,'
    'Members.APARTMENT_NUMBER,Members.CITY, Members.STATE, Members.ZIPCODE,'
    'Organization.DUES,Organization.LOCATION FROM Members INNER JOIN '
    'Organization ON Members.ID=Organization.Member_ID;')

run_sql_command_return_all_results(SQL_COMMAND, CURSOR)

# Write a SQL Query to pull all members that are over 45

SQL_COMMAND = (
    'SELECT Members.FIRST_NAME,Members.LAST_NAME, Members.AGE FROM Members '
    'WHERE Members.AGE > 45;')

run_sql_command_return_all_results(SQL_COMMAND, CURSOR)

# Write a SQL Query to pull all members that have a dues value of 0.
SQL_COMMAND = (
    'SELECT Members.FIRST_NAME,Members.LAST_NAME,Organization.DUES FROM '
    'Members INNER JOIN Organization ON Members.ID=Organization.Member_ID '
    'WHERE Organization.DUES =0;')

run_sql_command_return_all_results(SQL_COMMAND, CURSOR)
