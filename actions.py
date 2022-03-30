from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_sdk import Action
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset
from email.message import EmailMessage
import smtplib
import zomatopy
import requests
import json
import re

final_res_to_email = []
user_key = "2b2c609d9001d59124adaa3f7d562490"


class ActionSearchRestaurants(Action):
    config = {"user_key": user_key}

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        response = "---------------\n"
        zomato = zomatopy.initialize_app(self.config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')

        min_budget = int(tracker.get_slot('min_budget'))
        max_budget = int(tracker.get_slot('max_budget'))

        res, lat, lon = self._get_location(loc, zomato)
        if res == 0:
            response += 'Sorry, city location cannot be found!'
            dispatcher.utter_message(response)
        else:
            restaurants = self._get_restaurants(lat, lon, cuisine, zomato)
            budget_res = list(filter(lambda x: x[2] >= min_budget and x[2] <= max_budget, restaurants))[:10]
            budget_res_sorted = sorted(budget_res, key=lambda x: x[3], reverse=True)
            if len(budget_res_sorted) == 0:
                response += 'Sorry, no restaurants found!'
                dispatcher.utter_message(response)
                return [Restarted()]
            else:
                budget_res_sorted_top5 = budget_res_sorted[:5]
                global final_res_to_email
                final_res_to_email = budget_res_sorted[:10]
                counter = 1
                for el in budget_res_sorted_top5:
                    response += str(counter) + ". " + el[0] + " in " + el[1] + f" has been rated {el[3]}" + "\n"
                    counter += 1
                response += "---------------\n"
                dispatcher.utter_message("Here are our top recommendations:" + "\n" + response)
        return [SlotSet('location', loc)]

    @staticmethod
    def _get_location(loc, zomato):
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat, lon = 0, 0
        res = len(d1["location_suggestions"])
        if res > 0:
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return res, lat, lon

    @staticmethod
    def _get_restaurants(lat, lon, cuisine, zomato):
        all_cuisines = {'american': 1, 'chinese': 25, 'italian': 55,
                        'mexican': 73, 'north indian': 50, 'south indian': 85}
        result = []
        for val in range(0, 100, 20):
            results = zomato.restaurant_search("", lat, lon, str(all_cuisines.get(cuisine.lower())), start=val)
            d = json.loads(results)
            for restaurant in d['restaurants']:
                result.append((restaurant['restaurant']['name'],
                               restaurant['restaurant']['location']['address'],
                               float(restaurant['restaurant']['average_cost_for_two']),
                               float(restaurant['restaurant']['user_rating']['aggregate_rating'])))
        return result


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        to_email = tracker.get_slot('emailid')
        from_email = "foodierecommender@gmail.com"
        password = "upgrad@2020"
        subject = "Top " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        body = "Hi there! Here are the " + subject + "."
        body += "\n------------------------\n\n"
        count = 1
        for res in final_res_to_email:
            body += str(count) + ". " + res[0] + " in " + res[1]
            body += f", with average budget for two people as Rs. {res[2]} and "
            body += f"has been rated {res[3]}" + "\n\n"
            count += 1

        # Open SMTP connection to email server.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(from_email, password)
        msg = EmailMessage()

        # prepare message properties
        msg['Subject'] = subject
        msg['From'] = from_email
        msg.set_content(body)
        msg['To'] = to_email

        try:
            s.send_message(msg)
            dispatcher.utter_message("**** Email sent. Happy dining. ****")
        except smtplib.SMTPRecipientsRefused:
            dispatcher.utter_message(f"Unable to send email")
        except smtplib.SMTPAuthenticationError:
            dispatcher.utter_message(f"Authentication error when sending email")
        s.quit()
        return [Restarted()]


class Actiondefaultfallback(Action):
    def name(self):
        return 'default_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "**** How can I help you today ****")
        return [Restarted()]


class ActionOutOfScope(Action):
    def name(self):
        return 'out_of_scope'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "**** Sorry we can't fullfil the request. ****")
        return [AllSlotsReset()]


class ActionStop(Action):
    def name(self):
        return 'stop'

    def run(self, dispatcher, tracker, domain):
        #stop = tracker.get_slot('stop')
        #if stop=='stop' then exit()
        return [AllSlotsReset()]
        #return [exit()]


class VerifyLocation(Action):
    tier_1 = []
    tier_2 = []

    def __init__(self):
        self.tier_1 = ['ahmedabad', 'bangalore', 'chennai', 'delhi',
                       'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.tier_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati',
                       'amritsar', 'asansol', 'aurangabad', 'bareilly',
                       'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal',
                       'bhubaneswar', 'bikaner', 'bokaro steel city',
                       'chandigarh', 'coimbatore', 'cuttack', 'dehradun',
                       'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode',
                       'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur',
                       'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior',
                       'hubli-dharwad', 'indore', 'jabalpur', 'jaipur',
                       'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
                       'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode',
                       'kurnool', 'lucknow', 'ludhiana', 'madurai',
                       'malappuram', 'mathura', 'goa', 'mangalore', 'meerut',
                       'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik',
                       'nellore', 'noida', 'palakkad', 'patna', 'pondicherry',
                       'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela',
                       'salem', 'sangli', 'siliguri', 'solapur', 'srinagar',
                       'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur',
                       'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain',
                       'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city',
                       'vijayawada', 'visakhapatnam', 'warangal']

    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not self._verify_location(loc):
            dispatcher.utter_message("We do not operate in that area yet. We operate only in indian tier-1 and tier-2 cites")
            return [Restarted()]
        else:
            dispatcher.utter_message("Happy to serve. We operate in " + loc.capitalize())
            return [SlotSet('location', loc), SlotSet("check_location", True)]

    def _verify_location(self, loc):
        if loc:
            return loc.lower() in self.tier_1 or loc.lower() in self.tier_2


class VerifyBudget(Action):

    def name(self):
        return "action_check_budget"

    def run(self, dispatcher, tracker, domain):
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        error_msg = "Sorry! Price range not supported."
        try:
            min_budget = int(tracker.get_slot('min_budget'))
            max_budget = int(tracker.get_slot('max_budget'))

        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('min_budget', None), SlotSet('max_budget', None), SlotSet('check_budget', False)]
        if min_budget in min_dict and (max_budget in max_dict or max_budget > 700):
            return [SlotSet('min_budget', min_budget), SlotSet('max_budget', max_budget), SlotSet('check_budget', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [Restarted()]


def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, res_all, limit=20):
    base_url = 'https://developers.zomato.com/api/v2.1/'
    headers = {'Accept': 'application/json', 'user-key': user_key}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+f"&count={limit}", headers=headers).content).decode("utf-8")
    except:
        return
    res = json.loads(results)
    res_all.extend(res['restaurants'])
