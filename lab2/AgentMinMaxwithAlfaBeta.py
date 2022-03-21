import copy
import random
import time

from exceptions import AgentException


# podejmuje decyzje
class RandomAgentMinMax:
    def __init__(self, my_token='o'):
        self.my_token = my_token

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')

        start_time = time.perf_counter()

        bestCol = self.minmax(connect4, 7, True, -1000000, 1000000)[0]

        print(round(time.perf_counter() - start_time,2), "seconds")

        return bestCol

    def minmax(self, connect4, depth, isMaximizing, alpha, beta):

        if connect4.check_game_over():
            if connect4.wins == self.my_token:
                return 0, 100000
            elif connect4.wins is None:
                return 0, 0
            else:
                return 0, -100000

        if depth == 0:
            return self.heuristicCheck(connect4, self.my_token)

        possibleMove = connect4.possible_drops()

        if isMaximizing:
            bestVal = -100000
            bestCol = 0
            for i in possibleMove:
                kopiaStanu = copy.deepcopy(connect4)
                kopiaStanu.drop_token(i)
                bestValTemp = self.minmax(kopiaStanu, depth - 1, False, alpha, beta)[1]

                if bestValTemp > bestVal:
                    bestVal = bestValTemp
                    bestCol = i

                #alfa beta reduction

                if bestValTemp > alpha:
                    alpha = bestValTemp
                if beta <= alpha:
                    break



        else:
            bestVal = 100000
            bestCol = 0
            for i in possibleMove:
                kopiaStanu = copy.deepcopy(connect4)
                kopiaStanu.drop_token(i)
                bestValTemp = self.minmax(kopiaStanu, depth - 1, True, alpha, beta)[1]

                if bestValTemp < bestVal:
                    bestVal = bestValTemp
                    bestCol = i

                #alfa beta reduction
                if bestValTemp < beta:
                    beta = bestValTemp
                if beta <= alpha:
                    break



        return bestCol, bestVal

    def heuristicCheck(self, connect4, token):
        bestVal = 3 * connect4.center_column().count(token)

        for i in connect4.iter_fours():
            if i == ([token, token, token, '_']):
                bestVal += 5

            if i == ([token, token, '_', '_']):
                bestVal += 5

            if token == 'x':
                if i == (['o', 'o', 'o', '_']):
                    bestVal -= 10
            else:
                if i == (['x', 'x', 'x', '_']):
                    bestVal -= 10

        return 0, bestVal

