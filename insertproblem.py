import mysql.connector


def DataUpdate(question, choice1, choice2, choice3, choice4):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd="",
        database="questions"
    )

    mycursor = mydb.cursor()

    #sql = "CREATE TABLE QUIZES (pid INT PRIMARY KEY AUTO_INCREMENT, question VARCHAR(500), choice1 VARCHAR(250), choice2 VARCHAR(250), choice3 VARCHAR(250), choice4 VARCHAR(250));"
    sql = 'INSERT INTO QUIZES(question, choice1, choice2, choice3, choice4) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}");'.format(question, choice1, choice2, choice3, choice4)

    mycursor.execute(sql)

    mydb.commit()

    print("done")

if __name__=="__main__":
    question = input("Enter the question: ")
    choice1 = input("Enter the first choice: ")
    choice2 = input("Enter the second choice: ")
    choice3 = input("Enter the third choice: ")
    choice4 = input("Enter the fourth choice: ")
   
    
    DataUpdate(question, choice1, choice2, choice3, choice4)

