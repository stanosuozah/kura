
# import pandas as pd

# # Load the data into a pandas DataFrame
# df = pd.read_csv("Fifa_world_cup_matches.csv")

# # Get the team name from the user
# # team_name = input("Enter a team name: ")
# t_name = 'spain'
# team_name = t_name.upper()

# # Find the row indices where the team name appears in the DataFrame
# team1_indices = df.index[df.apply(lambda row: team_name in row.values, axis=1)].tolist()

# # Find the corresponding values in the team1 and team2 columns
# team1_values = []
# team2_values = []
# for idx in team1_indices:
#     if team_name in df.at[idx, "team1"]:
#         team1_values.append(df.at[idx, "team1"])
#         team2_values.append(df.at[idx, "team2"])
#     elif team_name in df.at[idx, "team2"]:
#         team1_values.append(df.at[idx, "team2"])
#         team2_values.append(df.at[idx, "team1"])

# # Print the results
# if len(team1_values) > 0:
#     print(f"{team_name} is found in the following rows:")
#     for team1_value, team2_value in zip(team1_values, team2_values):
#         print(f"team1: {team1_value}, team2: {team2_value}")
# else:
#     print(f"{team_name} is not found in the DataFrame.")


import pandas as pd

df = pd.read_csv("Fifa_world_cup_matches.csv")

# Get the team name from the user
# team_name = input("Enter a team name: ")
t_name = 'spain'
team_name = t_name.upper()


# Find the rows where the team name appears in the DataFrame
matching_rows = []
for _, row in df.iterrows():
    if team_name in row["team1"] or team_name in row["team2"]:
        matching_rows.append(row)

# Create a new DataFrame with the matching rows
if len(matching_rows) > 0:
    matching_df = pd.DataFrame(matching_rows)
    print(matching_df.head())
else:
    print(f"No rows found containing {team_name}.")
