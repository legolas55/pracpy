import sqlite3

connection = sqlite3.connect("sounds_like_a_gym.db")
cursor = connection.cursor()


cursor.execute("""DROP TABLE Members;""")
cursor.execute("""DROP TABLE Organization;""")


sql_command = """
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

cursor.execute(sql_command)


sql_command = """
CREATE TABLE Organization ( 
ID INTEGER PRIMARY KEY, 
MEMBER_ID VARCHAR(20), 
LOCATION VARCHAR(30), 
DUES DECIMAL(19,4));"""

cursor.execute(sql_command)

members_data = [ ("William", "Shakespeare",
                  "1000 Innovation Way",
                  "Apt 400","Fake London",
                  "Georgia","33009",
                  "123-456-789","105"),
                  ("John", "Smith",
                  "123 No Work No Eat Drive",
                  "Apt 1","Fake Plymouth",
                  "Massachusetts","01810",
                  "978-756-2313","40"),
                 ("Abraham", "Lincoln",
                  "678 Honest Drive",
                  "Apt 200","Hodgenville",
                  "Kentucky","2234",
                  "456-874-9432","200"),
                 ("William", "Wallace",
                  "234 BraveHeart Way",
                  "Apt 101","Scottsdale",
                  "Michigan","3406",
                  "679-223-1458","27"),
                 ("Amelia", "Earhart",
                  "556 Atlantic Street",
                  "Apt 19","Pacific",
                  "California","",
                  "123-111-789","213"),
                 ("Marie", "Curie",
                  "8901 Chemistry Way",
                  "Apt 120","Amherst",
                  "Virginia","12345",
                  "876-456-789","35"),
                 ("Boudicca", "",
                  "1000 Britan Way",
                  "Apt 101","Rome",
                  "Georgia","11009",
                  "111-222-333","22"),]
               
for member in members_data:
    members_format_str =( 'INSERT INTO members(ID, FIRST_NAME,'
                          'LAST_NAME, STREET_ADDRESS, APARTMENT_NUMBER,'
                          'CITY, STATE, ZIPCODE, PHONE_NUMBER, AGE)'
                          'VALUES (NULL, "{first}", "{last}", "{street_address}",'
                          '"{apartment_number}", "{city}", "{state}","{zipcode}",'
                          '"{phone_number}","{age}");')

    sql_command = members_format_str.format(first=member[0],
                                            last=member[1],
                                            street_address = member[2],
                                            apartment_number = member[3],
                                            city = member[4],
                                            state = member[5],
                                            zipcode = member[6],
                                            phone_number = member[7],
                                            age=member[8])
    cursor.execute(sql_command)

    sql_command="SELECT * FROM members ORDER BY ID DESC LIMIT 1"
    
    cursor.execute(sql_command)
    result = cursor.fetchone()
    members_table_id=result[0]
    
    gym_location= "Alpharetta"
    gym_dues = 30.00 
    if(result[-1] > 65):
        gym_dues=0
        
    organization_format_str=('INSERT INTO organization(ID, MEMBER_ID,'
                             'LOCATION, DUES) VALUES (NULL, "{member_id}",'
                             '"{location}", "{dues}");')
    
    sql_command = organization_format_str.format(member_id = members_table_id,
                                                 location = gym_location,
                                                 dues = gym_dues)

    cursor.execute(sql_command)

    
    
cursor.execute("SELECT * FROM Members") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)


cursor.execute("SELECT * FROM Organization") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)


#Write a query that lists each member name, address, dues and location.
    
sql_command=('SELECT Members.FIRST_NAME, Members.LAST_NAME, Members.STREET_ADDRESS, Members.APARTMENT_NUMBER,Members.CITY, Members.STATE, Members.ZIPCODE, Organization.DUES,Organization.LOCATION FROM Members INNER JOIN Organization ON Members.ID=Organization.Member_ID;')

#sql_command=("SELECT members.First_
cursor.execute(sql_command)

print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)

#Write a SQL Query to pull all members that are over 45

#Write a SQL Query to pull all members that have a dues value of 0.


