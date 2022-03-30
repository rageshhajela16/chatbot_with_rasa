## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "budget@budget.com"}
    - slot{"emailid": "budget@budget.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "budget@budg.com"}
    - slot{"emailid": "budget@budg.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "budget@bud.com"}
    - slot{"emailid": "budget@bud.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "budget@budget.com"}
    - slot{"emailid": "budget@budget.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "avp@avp.com"}
    - slot{"emailid": "avp@avp.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_3
* goodbye
    - default_fallback
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
    - slot{"min_budget": 700}
    - slot{"max_budget": 10000}
    - action_check_budget
    - slot{"min_budget": 700}
    - slot{"max_budget": 10000}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "av@db.com"}
    - slot{"emailid": "av@db.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"max_budget": 700, "min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 700}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "bjfajksf@gaje.com"}
    - slot{"emailid": "bjfajksf@gaje.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_3
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"min_budget": 700}
    - slot{"max_budget": 10000}
    - slot{"min_budget": 700}
    - action_check_budget
    - slot{"min_budget": 10000}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* city{"location": "America"}
    - slot{"location": "America"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* affirm{"affirm": "am fine thank you"}
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* affirm{"affirm": "am fine thank you"}
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* city{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* affirm{"affirm": "am fine thank you"}
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@bnd.com"}
    - slot{"emailid": "avp@bnd.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_howcanhelp
* restaurant_search
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 700, "max_budget": 10000}
    - slot{"max_budget": 10000}
    - slot{"min_budget": 700}
    - action_check_budget
    - slot{"min_budget": 700}
    - slot{"max_budget": 10000}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"location": "abcd@gef.co"}
    - slot{"location": "abcd@gef.co"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* out_of_scope{"out_of_scope": "where do we live?"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* greet{"greet": "hellloooooo"}
    - utter_greet
* out_of_scope{"out_of_scope": "ksafdlksjdf alkjlakjfsd"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_greet
* what_does_bot_do{"what_does_bot_do": "i am not sure"}
    - utter_what_does_bot_do
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* city{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - action_check_location
    - slot{"location": "ranchi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"min_budget": 300, "max_budget": 700}
    - slot{"max_budget": 700}
    - slot{"min_budget": 300}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet{"greet": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* min_budget{"min_budget": "300", "max_budget": "700"}
    - slot{"max_budget": "700"}
    - slot{"min_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 300}
    - slot{"max_budget": 700}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* out_of_scope{"out_of_scope": "I want to sleep"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* out_of_scope{"out_of_scope": "Wake me up in the morning"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* what_does_bot_do{"what_does_bot_do": "help", "affirm": "you"}
    - utter_what_does_bot_do
    - utter_ask_howcanhelp
    - action_restart

## interactive_story_1
* affirm
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* affirm
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* greet{"greet": "hu"}
    - default_fallback

## interactive_story_1
* affirm
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* greet{"greet": "namaste"}
    - utter_greet

## interactive_story_1
* affirm
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* affirm
    - utter_greet
* what_does_bot_do{"what_does_bot_do": "what"}
    - utter_what_does_bot_do
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* greet
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* affirm
    - utter_request_emailid
* send_email{"emailid": "budget@budget.com"}
    - slot{"emailid": "budget@budget.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* affirm
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "fgh@jkl.com"}
    - slot{"emailid": "fgh@jkl.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "he@yhe.com"}
    - slot{"emailid": "he@yhe.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* affirm
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"check_location": true}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "ade@kjg.com"}
    - slot{"emailid": "ade@kjg.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"check_location": true}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_request_email
* dont_send_email
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "max_budget": "3000", "emailid": "avp@ghi.com"}
    - slot{"cuisine": "chinese"}
    - slot{"emailid": "avp@ghi.com"}
    - slot{"location": "bangalore"}
    - slot{"max_budget": "3000"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bangalore", "max_budget": "3000", "emailid": "avp@ghi.com"}
    - slot{"emailid": "avp@ghi.com"}
    - slot{"location": "bangalore"}
    - slot{"max_budget": "3000"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* restaurant_search{"cuisine": "Mexican", "location": "bangalore", "max_budget": "13000", "emailid": "avp@ghi.com"}
    - slot{"cuisine": "Mexican"}
    - slot{"emailid": "avp@ghi.com"}
    - slot{"location": "bangalore"}
    - slot{"max_budget": "13000"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - utter_ask_location
* city{"location": "haridwar"}
    - slot{"location": "haridwar"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* max_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "axy@rtc.com"}
    - slot{"emailid": "axy@rtc.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* max_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "axy@rtc.com"}
    - slot{"emailid": "axy@rtc.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* max_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"email": "akfjsadklf@kjfkla.in"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* max_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"email": "akfjsadklf@kjfkla.in"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* city{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* city{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - action_check_location
    - slot{"location": "Mysore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"check_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* min_budget{"max_budget": "300"}
    - slot{"max_budget": "300"}
    - action_check_budget
    - slot{"min_budget": 0}
    - slot{"max_budget": 300}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_request_email
* send_email
    - utter_request_emailid
* send_email{"emailid": "avp@dxb.com"}
    - slot{"emailid": "avp@dxb.com"}
    - action_send_email
    - utter_email_sent
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart
## interactive_story_1
* greet{"greet": "hi"}
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_location
    - utter_ask_budget
* restaurant_search{"min_budget": "700", "max_budget": "10000"}
    - slot{"max_budget": "10000"}
    - slot{"min_budget": "700"}
    - action_check_budget
    - slot{"min_budget": 700}
    - slot{"max_budget": 10000}
    - slot{"check_budget": true}
    - action_search_restaurants
    - slot{"location": null}

## interactive_story_2
* greet{"greet": "hi"}
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* city{"location": "germany"}
    - slot{"location": "germany"}
    - action_check_location
    - slot{"location": null}
    - slot{"check_location": false}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* out_of_scope{"location": "bsidjf;sjdf"}
    - slot{"location": "bsidjf;sjdf"}

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* out_of_scope{"location": "bsidjf;sjdf"}
    - slot{"location": "bsidjf;sjdf"}
    - action_check_location

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* out_of_scope{"location": "bsidjf;sjdf"}
    - slot{"location": "bsidjf;sjdf"}
    - action_check_location

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* city{"location": "bsidjf;sjdf"}
    - slot{"location": "bsidjf;sjdf"}
    - action_check_location

## interactive_story_5
* greet
    - utter_greet
* out_of_scope{"location": "bsidjf;sjdf"}
    - slot{"location": "bsidjf;sjdf"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* goodbye
    - utter_goodbye
    - stop
    - reset_slots
    - action_restart

## interactive_story_1
* greet{"greet": "hi"}
    - utter_greet
* out_of_scope{"location": "asd;asd"}
    - slot{"location": "asd;asd"}
    - utter_out_of_scope
    - utter_what_does_bot_do
    - action_restart

## interactive_story_1
* stop
    - action_restart

## interactive_story_1
* send_email{"emailid": "avp@bnb.com"}
    - slot{"emailid": "avp@bnb.com"}
    - action_restart
## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "emailid": "jhiitiorfgad@outlook.com"}
    - slot{"cuisine": "chinese"}
    - slot{"emailid": "jhiitiorfgad@outlook.com"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - action_send_email

## interactive_story_1
* restaurant_search{"location": "bangalore", "cuisine": "american", "emailid": "testing@gmail.com"}
    - slot{"cuisine": "american"}
    - slot{"emailid": "testing@gmail.com"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"check_location": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - action_send_email

## interactive_story_1
* greet{"greet": "hi"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* city
    - action_check_location
