from minmaxClass import minmaxClass

from exceptions import GameplayException
from connect4 import Connect4
from AgentMinMaxwithAlfaBeta import *

connect4 = Connect4()
agent = RandomAgentMinMax()
while not connect4.game_over:
    print("---NEXT MOVE------")
    connect4.draw()

    try:
        if connect4.who_moves == agent.my_token:
            n_column = agent.decide(connect4)
        else:
            n_column = int(input(':'))
        connect4.drop_token(n_column)
    except (ValueError, GameplayException):
        print('invalid move')

connect4.draw()
