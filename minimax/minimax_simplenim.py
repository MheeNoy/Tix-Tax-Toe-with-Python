

def minimax(state, is_maximizing):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score
   
    return (max if is_maximizing else min)(
       minimax(new_state, is_maximizing = not is_maximizing)
       for new_state in possible_new_states(state)
    )
    

def best_move(state):
  
    return max((minimax(new_state, is_maximizing=False),new_state )
    for new_state in possible_new_states(state))
     



def possible_new_states(state):
   for pile, counters in enumerate(state):
       for take in range(1,(counters+1) //2):
           yield state[:pile] + (counters - take, take) + state[pile + 1 :]
           
      # print (f' {pile} state : {state} in Remain : {remain}')

def evaluate(state, is_maximizing):
    if all(counters <= 2 for counters in state):
        return 1 if is_maximizing else -1



