# Game of Life Rules
# A live cell will die if there are less than 2 neighbors
# A live cell will live if there are exactly 2 or 3 neighbors
# A live cell will die if there are more than 3 neighbors
#
# A dead cell will change to live if there are exactly 3 neighbors

# class Game:
#
#     def __init__(self, iState, rules, sizeLimit) :
#         self.iState = iState
#         self.rules = rules
#         self.sizeLimit = sizeLimit
#
#     def run(self, it) :
#         state = iState
#         prevState = None
#         progress = []
#         i = 0
#
#         while (! state.equals(prevState) and i < it):
#             prevState = state.copy()
#             progress.append(prevState.grid)
#             state = state.applyRules(self.rules, self.sizeLimit)
#             i += 1
#
#         progress.append(state.grid)
#         return(progress)
