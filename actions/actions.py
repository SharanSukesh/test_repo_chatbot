# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHospitalLocations(Action):

    def name(self) -> Text:
        return "action_hospital_locations"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity'] == 'location':
                name = e['value']
                #print(name)           
            if name == 'Bangalore':
                dispatcher.utter_message(text="There are hospitals in bangalore at : address1, address2, address3! Which one would you like to book?")
            elif  name == 'Mumbai':
                dispatcher.utter_message(text="There are hospitals in mumbai at : address1, address2, address3! Which one would you like to book?")
            else:
                dispatcher.utter_message(text="There are hospitals in delhi at : address1, address2, address3! Which one would you like to book?")

        return []
    
class ActionNameCheck(Action):

    def name(self) -> Text:
        return "action_check_name"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        if(len(entities)) == 0 :
            dispatcher.utter_message('Before we continue, could you please tell me your name?')
        else:
            for e in entities:
                if e['entity'] == 'name':
                    name = e['value']
                if name == '':
                    dispatcher.utter_message(text="Before we continue, could you please tell me your name?")
                else:
                    dispatcher.utter_message("Great {name}, how can I help you?".format(name = name))

        return []
