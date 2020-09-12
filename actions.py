from numpy import random
from typing import Any, Text, Dict, List
from typing import Any, Text, Dict, List
import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import ReminderScheduled, ReminderCancelled
from rasa_sdk.executor import CollectingDispatcher


import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd="",
        database="questions"
    )

mycursor = mydb.cursor()
myresult = []
hintlist = []
finfo = []
randomnum = 0
hintmaxx = 0
hintcnt = 0
failcnt = 0
failmax = 2
count = 0
i=0

class ActionIncreaseScore(Action):

    def name(self) -> Text:
        return "action_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global randomnum, myresult, hintlist, hintmaxx, hintcnt, finfo, count, i
        ansentity=next(tracker.get_latest_entity_values("answer"), None)
        count = count + 1
        if i == 4:
            return [FollowupAction("action_send_problem_link")]
        
        # dispatcher.utter_message(text="Hello World!")

        return [FollowupAction("action_quiz")]

class ActionQuiz(Action):

    def name(self) -> Text:
        return "action_quiz"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global randomnum, myresult, hintlist, hintmaxx, hintcnt, finfo,i,count
        quizentity=next(tracker.get_latest_entity_values("quiz"), None)
        queryy = 'select * from quizes'
        mycursor.execute(queryy)
        myresult = mycursor.fetchall()
        maxx = len(myresult)

       
        randomnum = random.randint(maxx)
        if i == 4:
            return [FollowupAction("action_send_problem_link")]        
        
        msg = myresult[i][1]
        buttons = [{"title": myresult[i][2], "payload": myresult[i][2]}, {"title": myresult[i][3],  "payload":myresult[i][3]}, {"title": myresult[i][4], "payload": myresult[i][4]}, {"title": myresult[i][5], "payload": myresult[i][5]}]      
        dispatcher.utter_button_message(msg+str(count), buttons)
        i = i+1

        return []



class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        #name = next(tracker.get_latest_entity_values("new"))
        dispatcher.utter_message("Opps! Unfortunately your time has ended! You final score is" + str(count) + "out of 5")

        return [FollowupAction("action_send_problem_link")]

class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message("Here's a new question for you. Given two strings text1 and text2, return the length of their longest common subsequence.I am setting the timer to 5 seconds.")

        dispatcher.utter_message("The quiz has started and so has the timer. We challenge you to finish it withing 20 minutest. Best of luck!")
        date = datetime.datetime.now() + datetime.timedelta(seconds=7200)
        entities = tracker.latest_message.get("new")


        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class Actionsendmail(Action):

    def name(self) -> Text:
        return "action_send_problem_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    

        global randomnum, myresult, count
        
        import smtplib

        EMAIL_ADDRESS = "benjaminimp10@gmail.com"
        EMAIL_PASSWORD = ""
        recieverid = str(tracker.get_slot('mail'))

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = 'RASA QUIZ SCORE'
            body = "here's the score of your RASA quiz: " + " " + str(count)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(EMAIL_ADDRESS, recieverid, msg)

        msg = "The link has been sent to your email id. Thank you for playing the Quiz. Hope you liked it."

        dispatcher.utter_message(text = msg)

        return [FollowupAction("utter_goodbye")]