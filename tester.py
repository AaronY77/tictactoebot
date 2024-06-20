from tictactoe import initial_state,player,actions,result,winner,terminal,utility,minimax,minimaxhelper
def main():
    board=[["X",None,"O"],["X",None,None],["X",None,"O"]]
    print(winner(board))
if __name__ == "__main__":
    main()
