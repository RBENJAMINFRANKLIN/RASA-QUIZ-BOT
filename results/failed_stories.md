## happy path 1 (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: action_select_and_display_problem -->
* mood_great: amazing   <!-- predicted: name_entry: [amazing](approach) -->
    - utter_happy   <!-- predicted: action_default_ask_affirmation -->


## happy path 2 (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: action_select_and_display_problem -->
* mood_great: amazing   <!-- predicted: name_entry: [amazing](approach) -->
    - utter_happy   <!-- predicted: action_default_ask_affirmation -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: action_select_and_display_problem -->
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: hint1: yes -->
    - utter_happy   <!-- predicted: action_first_hint -->


## sad path 2 (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: action_select_and_display_problem -->
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: approach: not [really](info) -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 3 (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: action_select_and_display_problem -->
* mood_unhappy: very terrible   <!-- predicted: approach: very terrible -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: approach: [no](approach) -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## bot challenge (C:\Users\USER\AppData\Local\Temp\tmpzzpkv3ql\22311b88441448cc8aca3682da99f830_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: goodbye: are you a bot? -->
    - utter_iamabot   <!-- predicted: action_default_ask_affirmation -->


