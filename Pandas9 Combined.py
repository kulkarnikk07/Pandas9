# Pandas9

# 1 Problem 1 : Game Play Analysis I ( https://leetcode.com/problems/game-play-analysis-i/ )

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df= activity.groupby(['player_id'])['event_date'].min().reset_index()
    return df.rename(columns = {'event_date':'first_login'})

# 2 Problem 2 : Customers Placing the Largest Number of Orders ( https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/ ) 

