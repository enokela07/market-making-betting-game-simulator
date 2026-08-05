"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    ev = 0
    for i in range(len(values)):
        ev += values[i]*probabilities[i]

    return ev
    pass

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    prob = 1/sides
    values = [i+1 for i in range(sides)]
    probabilities = [prob for i in range(sides)]
    mid = expected_value(values, probabilities)

    reroll_faces = []
    reroll_ev = []

    for value in values:
        if value < mid:
            reroll_faces.append(value)
            reroll_ev.append(mid)

        else:
            reroll_ev.append(value)

    final_ev = expected_value(reroll_ev, probabilities)

    result = {}

    result['value'] = final_ev
    result['reroll_faces'] = reroll_faces

    return result

    pass

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    expected_values = []
    for i in range(1, sides+1):
        e_v = (i+sides)/2 - (i-1)*reroll_cost/(sides -i+1)
        expected_values.append(e_v)

    max_ev = max(expected_values)
    treshold = expected_values.index(max_ev)+1
    result = {}
    result['threshold'] = treshold
    result['value'] = max_ev

    return result

    
    pass

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

