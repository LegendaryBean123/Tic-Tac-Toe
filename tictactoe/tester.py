from tictactoe import player
from tictactoe import initial_state
from tictactoe import actions
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility
from tictactoe import minimax

E = None
X = "X"
O = "O"

state = [[E, E, E],
         [E, X, E],
         [E, E, E]]


#print(player(state))
#print(actions(state))
#print(winner(state))
#print(terminal(state))
#print(utility(state))
#print(state)
print(result(state, (4, 1)))

#print(minimax(state))

