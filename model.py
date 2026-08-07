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

# Step 4 - red_black_card_game_value
#helper function to recursively find V(r,b)
def V(r ,b ):
    if r == 0:
        return 0
    if b == 0:
        return r
    total = r+b
    r_prob = r/total
    b_prob = b/total
    return max(0, r_prob*(1 + V(r-1, b))+b_prob*(-1+V(r, b-1)))


def red_black_card_game_value(num_red, num_black):
    # TODO: return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.

    if num_red == 0 and num_black == 0:
        return {"value": 0.0, "stop_now": True}

    if num_red == 0:
        return {"value": 0.0, "stop_now": True}

    if num_black == 0:
        return {"value": float(num_red), "stop_now": False}

    V_table = [[0 for i in range(num_black+1)] for i in range(num_red+1)]
    V_table[1][0] = 1

    
    for r in range(num_red+1):
        for b in range(num_black+1):
            V_table[r][b] = V(r, b)

    
    

    r_prob = num_red/(num_black+num_red)
    b_prob = num_black/(num_black+num_red)

    value = V_table[num_red][num_black]
    cont = r_prob*(1 + V_table[num_red-1][num_black]) + b_prob*(-1 + V_table[num_red][num_black-1])
    stop_now = (cont <= 0)

    result = {}
    result['value'] = value
    result['stop_now'] = stop_now
    return result

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
  
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    bid = fair_value - spread_width/2
    ask = fair_value + spread_width/2

    return {'bid':bid, 'ask':ask}
    pass

# Step 6 - execute_trade
def execute_trade(state, side, bid, ask, size=1):
    # TODO: apply a counterparty trade against your bid/ask and return updated state
    new_cash = 0
    new_inventory = 0

    if side == 'buy':
        new_cash = state['cash']+ size*ask
        new_inventory = state['inventory']-size

    if side == 'sell':
        new_cash = state['cash']- size*bid
        new_inventory = state['inventory']+size

    new_state = {}
    new_state['cash'] = new_cash
    new_state['inventory']= new_inventory

    return new_state
    pass

# Step 7 - mark_to_market_pnl
def mark_to_market_pnl(cash, inventory, settlement_value):
    # TODO: return total P&L given cash, remaining inventory, and settlement value.

    return cash + inventory*settlement_value
    pass

# Step 8 - adverse_selection_loss
import numpy as np

def adverse_selection_loss(fair_value, bid, ask, informed_values, informed_probabilities):
    # TODO: expected loss = E[(v-ask)*1{v>ask}] + E[(bid-v)*1{v<bid}] over informed_values.
    l = 0
    for i in range(len(informed_values)):
        prob = informed_probabilities[i]
        val = informed_values[i]
        l += prob*max(((val-ask), 0))
        l += prob*max(((bid -val), 0))

    return l
    pass

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

