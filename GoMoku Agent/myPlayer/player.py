#######################################################
# Gomoku AI player
# Version 1.0
#
# Hadi Jalali Lak(932173), Talal Thaheem(956013), Tahmeed Ahmed(966983)
# Swansea University
# March 2020
#
# motivation taken from:
# Gomuku AI Player by Daniel Ford of Cardiff University
# available at: https://pats.cs.cf.ac.uk/@archive_file?p=525&n=final&f=1-1224795-final-report.pdf&SIG=a852f388b81ea43c0953ec0fb298084d16361371285eb9b836422360627fbd64
# Liao, Han, "New heuristic algorithm to improve the
# Minimax for Gomoku artificial intelligence" (2019).
# https://lib.dr.iastate.edu/creativecomponents/407
#  Sections 5.1 to 5.4 of
#  Artificial Intelligence: A Modern Approach by
#  Russell and Norvig
from gomokuAgent import GomokuAgent

from misc import winningTest
from misc import legalMove
import numpy as np

class Player(GomokuAgent):
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        GomokuAgent.__init__(self, ID, BOARD_SIZE, X_IN_A_LINE)

    # function to get all the possible moves from a board state but
    # instead of returning all the empty spots it looks for position
    # adjacent to a taken spot
    def getMoves(self, board, pID):
        moves = []
        winningMove = []
        for i in range(1, len(board) - 1):
            for j in range(1, len(board) - 1):
                if board[i][j] == 0:
                    # checking if there's a taken spot next to the chosen spot
                    if board[i][j - 1] != 0 or board[i][j + 1] != 0 or board[i + 1][j] != 0 or board[i - 1][j] != 0 or \
                            board[i - 1][j - 1] != 0 or board[i - 1][j + 1] != 0 or board[i + 1][j - 1] != 0 or \
                            board[i + 1][j + 1] != 0:

                        tempBoard = np.array(board)
                        tempBoard[i][j] = pID
                        # adding the move to the list if it's not already in
                        if (i, j) not in moves:
                            moves.append((i, j))
                        # check if the current chosen move leads to a winning state
                        # if it does, we only need to return this move
                        if winningTest(pID, tempBoard, 5):
                            winningMove.append((i, j))
                            break
        if len(winningMove) > 0:
            return winningMove

        return moves

    # function used to generate a value to be used in the minimax algorithm
    def evaluation(self, board, isOpponentsTurn, pID):
        # calculate the board score for the AI and opponent
        opponent_score = self.getScore(board, True, isOpponentsTurn, pID)
        my_score = self.getScore(board, False, isOpponentsTurn, pID)

        # change 0 to one to avoid 0 division problems
        if opponent_score == 0:
            opponent_score = 1.0

        # return the chance of AI winning compared to the opponent
        return my_score / opponent_score

    # function to calculate the board score which just sums the score of each row
    # column and diagonal line in the board
    # forOpponent is a boolean defining which player we are evaluating the board for
    # isOpponentsTurn is a boolean defining who's turn it is in the game
    def getScore(self, board, forOpponent, isOpponentsTurn, pID):
        tempBoard = np.array(board)

        return self.horizontal_score(tempBoard, forOpponent, isOpponentsTurn, pID) \
               + self.vertical_score(tempBoard, forOpponent, isOpponentsTurn, pID) \
               + self.diagonal_score(tempBoard, forOpponent, isOpponentsTurn, pID)

    # function to calculate the horizontal score
    def horizontal_score(self, board, forOpponent, isOpponentsTurn, pID):
        consecutiveGos = 0  # number of consecutive Gos counted in the currnt iteration
        score = 0
        blocks = 2  # number of sides blocked by the board edges or opponent Gos
        playingID = pID
        # if it's opponents urn change the id to opponents id
        if forOpponent:
            playingID = - pID
        # going through every row
        for i in range(len(board)):
            # go through every cell in the row
            for j in range(len(board)):
                # if there is a friendly GO in this position add to the consecutiveGos
                if board[i][j] == playingID:
                    consecutiveGos += 1
                elif board[i][j] == 0:
                    # if the current spot is empty and we had
                    # consecutive Gos before we reduce 1 from the blocks variable
                    # because we know this side is not blocked
                    if consecutiveGos > 0:
                        blocks -= 1
                        score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                        consecutiveGos = 0
                        # if this cell is empty next set will hav at most 1 blocked side
                        blocks = 1
                    # if this cell is empty next set will hav at most 1 blocked side
                    else:
                        blocks = 1
                # if there's an opponent Go in this cell and we've counted
                # consecutive friendly Go's before reset the counter to zero
                # and changed blocks value to 2 because the next set of Gos will have
                # at most 2 blocked sides
                elif consecutiveGos > 0:
                    score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                    consecutiveGos = 0
                    blocks = 2
                else:
                    blocks = 2
            # check if the was any consecutiveGos before we reached the end of the row
            if consecutiveGos > 0:
                score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
            # reset the values for the next row
            consecutiveGos = 0
            blocks = 2
        return score

    # same as horizontal_score but we go through columns instead of rows
    def vertical_score(self, board, forOpponent, isOpponentsTurn, pID):
        consecutiveGos = 0
        score = 0
        blocks = 2
        playingID = pID

        if forOpponent:
            playingID = - pID

        for j in range(len(board)):
            for i in range(len(board)):
                if board[i][j] == playingID:
                    consecutiveGos += 1
                elif board[i][j] == 0:
                    if consecutiveGos > 0:
                        blocks -= 1
                        score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                        consecutiveGos = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutiveGos > 0:
                    score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                    consecutiveGos = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutiveGos > 0:
                score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
            consecutiveGos = 0
            blocks = 2
        return score

    # calculating the score for the 2 diagonal directions
    def diagonal_score(self, board, forOpponent, isOpponentsTurn, pID):
        consecutiveGos = 0
        score = 0
        blocks = 2
        playingID = pID

        if forOpponent:
            playingID = - pID
        # bottom-left to top-right
        # k ranges from 0 to 21. if its negative we take zero to start
        # if it's bigger than the board size -1 we take the board size -1
        # for the ending value . the initialization of k range was inspired by some
        # similar solutions
        for k in range((2 * (len(board) - 1)) + 1):
            start = max(0, k - len(board) + 1)
            end = min(len(board) - 1, k)
            # go through the line
            for i in range(start, end + 1):
                j = k - i
                # the rest is exactly like the other two score functions
                if board[i][j] == playingID:
                    consecutiveGos += 1
                elif board[i][j] == 0:
                    if consecutiveGos > 0:
                        blocks -= 1
                        score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                        consecutiveGos = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutiveGos > 0:
                    score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                    consecutiveGos = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutiveGos > 0:
                score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
            consecutiveGos = 0
            blocks = 2

        # top-left to bottom-right
        for k in range(1 - len(board), len(board)):
            start = max(0, k)
            end = min(len(board) + k - 1, len(board) - 1)
            for i in range(start, end + 1):
                j = i - k
                if board[i][j] == playingID:
                    consecutiveGos += 1
                elif board[i][j] == 0:
                    if consecutiveGos > 0:
                        blocks -= 1
                        score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                        consecutiveGos = 0
                        blocks = 1
                    else:
                        blocks = 1
                elif consecutiveGos > 0:
                    score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
                    consecutiveGos = 0
                    blocks = 2
                else:
                    blocks = 2

            if consecutiveGos > 0:
                score += self.getConsecutiveGosScore(consecutiveGos, blocks, forOpponent == isOpponentsTurn)
            consecutiveGos = 0
            blocks = 2
        return score

    # function to calculate the score value based on the number of consecutive
    # Gos and number of sides blocked. The player's turn is also taken into consideration
    def getConsecutiveGosScore(self, consecutiveGos, blocks, currentlyPlaying):
        # if both sides of a Go set is blocked, it's basically worthless unless
        # there is 5 Gos in that consecutive set
        if blocks == 2 and consecutiveGos < 5: return 0
        # winning scenario
        if consecutiveGos == 5:
            return 100_000
        # player playing with 4 friendly consecutive Gos is
        # just a move away winning scenario
        if consecutiveGos == 4:
            if currentlyPlaying:
                return 10_000
            else:
                # if both sides are open then it's also a move away from a winning
                # scenario no matter what move opponent plays
                if blocks == 0:
                    return 20_000
                # with only 1 side open, there is a possibility of a winning move depending on
                # he opponent's move
                else:
                    return 500

        if consecutiveGos == 3:
            if blocks == 0:
                # with 3 Gos in a row, no blocked sides and AI playing, with 1 move
                # we can move to an state with 4 consecutive Gos and no blocked sides
                # which is a guaranteed win so it has a high score
                if currentlyPlaying:
                    return 50_000
                else:
                    # with opponent making the move it will force them to block a side
                    # which prevents them from attacking ( if they do attack we move to a guaranteed win state)
                    return 500
            else:
                if currentlyPlaying:
                    return 10
                else:
                    return 5
        # two consecutive Gos have a low score but it's still better thn the worst scenario
        if consecutiveGos == 2:
            if blocks == 0:
                if currentlyPlaying:
                    return 7
                else:
                    return 5
        if consecutiveGos == 1:
            return 1
        # return a very big number  to avoid the program crashing when there is
        # more than 5 consecutive Gos and for some reason they haven't been detected before
        return 200_000

    # main method for our AI decision-making
    # alpha hold the maximum
    # beta holds the minimum
    # alpha and beta are used accelerate the selection process.(the process is
    # explained below)
    def minimax(self, depth, board, alpha, beta, maximizingPlayer, pID):
        # generate all the possible and sensible moves
        allMoves = self.getMoves(board, pID)
        # if there is no ove found or we are at the last depth, return None as moves
        if len(allMoves) == 0 or depth == 0:
            correctMove = [self.evaluation(board, not maximizingPlayer, pID), None, None]
            return correctMove
        # in order to compare the different moves generated by the algorithm
        # with each other we need to save each move's resulted board's evaluation
        # score which is why a array of the size of 3 is created. in this array the
        # the first element will hold the evaluation score of the suggested move's board
        correctMove = np.zeros(3)
        # maximizing scenario
        if maximizingPlayer:
            # set the initial evaluation score to a number smaller than any case
            correctMove[0] = - 1.0
            # go through every move
            for move in allMoves:
                # play that move
                tempBoard = np.array(board)
                tempBoard[move] = pID
                # call this minimax again for the minimizing scenario which
                # is opponents best move. Thi will be called (Depth) times and
                # find the minimum score for out AI
                tempMove = self.minimax(depth - 1, tempBoard, alpha, beta, not maximizingPlayer, pID)
                # if the current evaluation score is bigger than the current alpha
                # (max score) then update alpha
                # however if the evaluation score is lower than the alpha, the subtree orognating
                # from this move will be discarded since the maximizing player would chose alpha either way
                if tempMove[0] > alpha:
                    alpha = tempMove[0]
                # we just need to check if the current node's score is less than
                # beta because beta holds the minimum value of the evaluation score for nodes above. and any
                # value higher than this will never be chosen by the minimizing player
                if tempMove[0] >= beta:
                    return tempMove

                # correctMove is set to the move with the highest evaluation score
                if tempMove[0] > correctMove[0]:
                    correctMove = tempMove
                    correctMove[1] = move[0]
                    correctMove[2] = move[1]
        # minimizing scenario
        else:
            # set the initial score a number bigger than any scenario
            # and set the initial move to the first move in the list
            correctMove[0] = 1_000_000
            firstMove = allMoves[0]
            correctMove[1] = firstMove[0]
            correctMove[2] = firstMove[1]
            # go through every move and play it on a temporary board which is an
            # exact copy of the current board
            for move in allMoves:
                tempBoard = np.array(board)
                tempBoard[move] = pID
                # generate minimax trees from this node until depth = 0
                tempMove = self.minimax(depth - 1, tempBoard, alpha, beta, not maximizingPlayer, pID)
                # if the current score is smaller than the beta (minimum score of nodes above)
                # then we update the beta.
                # any node with a bigger evaluation score will be discarded along with the originating subtree
                if tempMove[0] < beta:
                    beta = tempMove[0]
                # The aim in this sage is to find a ove with a higher score than alpha. so if
                # that's not the case we just break
                if tempMove[0] <= alpha:
                    return tempMove
                # correct move is set to the ove with the lowest evaluation score
                if tempMove[0] < correctMove[0]:
                    correctMove = tempMove
                    correctMove[1] = move[0]
                    correctMove[2] = move[1]
        return correctMove

    def move(self, board):
        # check if we are making the firs move if so, then chose the middle cell
        if np.all((board == 0)):
            return (5, 5)
        else:
            # call the minimax and use the second and the third elements to move
            # (since the first element holds the evaluation score of the move)
            # going with 3 depth caused time_outs so depth 2 is the best we were able to do
            minimaxOutput = self.minimax(2, board, - 1.0, 1_000_000, True, self.ID)
            return (minimaxOutput[1], minimaxOutput[2])
