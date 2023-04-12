
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd


class ActionShowFixtures(Action):

    def name(self) -> Text:
        return "show_fixtures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv('Fifa_world_cup_matches.csv')
        selected_cols = df[['team1', 'team2']]
        selected_cols = selected_cols.to_html()    

        dispatcher.utter_message(text="here is all of your data {}".format(selected_cols))
        return []

class ActionTeamMatches(Action):

    def name(self) -> Text:
        return "team_matches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv("Fifa_world_cup_matches.csv")
        t_name = tracker.get_slot('team')
        print(t_name)
        team_name = t_name.upper()


        # Find the rows where the team name appears in the DataFrame
        matching_rows = []
        for _, row in df.iterrows():
            if team_name in row["team1"] or team_name in row["team2"]:
                matching_rows.append(row)

        # Create a new DataFrame with the matching rows
        if len(matching_rows) > 0:
            matching_df = pd.DataFrame(matching_rows)
            sel_col = matching_df[['team1','team2','date']]
            sel_col = sel_col.to_html()    
            dispatcher.utter_message(text="here is all of your data {}".format(sel_col))            
            # print(matching_df.head())
        else:
            dispatcher.utter_message(text ="no team found with the name that you have entered")