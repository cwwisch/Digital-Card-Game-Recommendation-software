from Card_Game_Tree import digital_cg as dcg
from user_input_for_recommendations import get_preferences

def get_recommendations():
    preferences = dict(get_preferences())
    return preferences

print(get_recommendations())