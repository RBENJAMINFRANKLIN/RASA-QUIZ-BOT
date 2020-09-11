## intent:greet
- hey
- hello
- hi
- good morning
- hiya
- good evening
- good afternoon


## intent:goodbye
- bye
- goodbye
- see you around
- see you later

<!-- ## lookup:names
import pandas as pd
df = pd.read_csv('https://query.data.world/s/k6cd3d2bwkd3c3oi3m75yix5ne7rec') -->


## intent:out_of_scope
- please help with my ice cream it's dripping
- bot is dead



## intent:get_email
- [gmail.com](mail)
- [edu.in](mail)
- [yahoo](mail)
- [benjamin10051999@gmail.com](mail)
- my email id is [ankit@gmail.com](mail)

## regex:mail
- [A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}

## intent:quiz
- [quiz](quiz)
- [quiz](quiz) master
- i wanna play [quiz](quiz)
- let's play [quiz](quiz)
- [quiz](quiz) competition
- [personalised](quiz)
- [keyword-based](quiz) 
- [None of the above](quiz)
- [one-line deploy script](quiz)
- [Kubernetes/Openshift](quiz)
- [Docker Compose](quiz)
- rasa [run actions]{"entity":"quiz","value":"run actions"}
- rasa [server]{"entity":"quiz","value":"server"}
- [tokenization](quiz)
- [featurization](quiz)
- [entity recognition](quiz)

## intent:answer
- this is the [answer](answer)
- [contextual]{"entity":"answer","value":"contextual"}
- [All of the above]{"entity":"answer","value":"All of the above"}
- [unfeaturized]{"entity":"answer","value":"unfeaturized"}
- [rasa run]{"entity":"answer","value":"rasa run"}
- [validation]{"entity":"answer","value":"validation"}
- the answer is [rasarun]{"entity":"answer","value":"rasarun"}
- answer is [rasa run]{"entity":"answer","value":"rasa run"}
- it is [rasa run]{"entity":"answer","value":"rasa run"}
