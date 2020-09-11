import mysql.connector

def DataUpdate(statement, hint1, hint2, valid_keywords, invalid_keywords, link, company, topic):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd="",
        database="dsalgo"
    )

    mycursor = mydb.cursor()

    sql = "CREATE TABLE PROBLEMS (statement VARCHAR(500), hint1 VARCHAR(500), hint2 VARCHAR(500), valid_keywords VARCHAR(500), invalid_keywords VARCHAR(500), link VARCHAR(500))"
    #sql = 'INSERT INTO PROBLEMS (statement, hint1, hint2, valid_keywords, invalid_keywords, link, company, topic) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}");'.format(statement, hint1, hint2, valid_keywords, invalid_keywords, link, company, topic)

    mycursor.execute(sql)

    mydb.commit()

    print("done")

if __name__=="__main__":
    statement = input("Enter the statement: ")
    hint1 = input("Enter the first hint: ")
    hint2 = input("Enter the second hint: ")
    valid_keywords = input("write the valid keywords seperated by ',' : ")
    invalid_keywords = input("invalid keywords: ")
    link = input("link of the problem: ")
    company_name = input("company it was asked in: ")
    tag = input("tag/topic: ")
    DataUpdate(statement, hint1, hint2, valid_keywords, invalid_keywords, link, company_name, tag)