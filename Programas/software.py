

from copy import deepcopy
import heapq

class Klostki:
    def __init__(self,board,pieces,move_history=[]):
        self.board = deepcopy(board)
        self.pieces=deepcopy(pieces)
        self.move_history = [] + move_history + [self.board]

    def __str__(self):
        return convert_board_to_str(self.board)

    
    def children(self):
        # returns the possible moves
        functions = [self.move_up, self.move_down, self.move_left, self.move_right]

        children = []
        for func in functions:
            for piece in self.pieces:
                child = func(piece)
                if child:                    
                    children.append(child)

        return children


#value of board;
#if value%2 == 0 ,double piece vertical
#if value%2 != 0 , double piece horizontaly
#if value < 0, sigle piece
#if value == 1, big piece *peça objetivo*
#if value == 0, free space


    def move_up(self,piece): #mover as peças para cima
        state = Klostki(self.board,self.pieces, self.move_history)
        p = piece
        if p>0:
            if p%2==0: #mover as verticais
                if state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]]==0:
                    state.board[state.pieces[p][0]-1][state.pieces[p][1]]=p #atualiza a board
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=p #atualiza a board
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]]=0 #atualiza a board
                    state.pieces[p]=(state.pieces[p][0]-1,state.pieces[p][1]) #atualiza a posição do topo esquerdo da peça
                    return state
                else:                    
                    return None   
            elif p != 1:
                if state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]]==0 and state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]+1]==0:
                    state.board[state.pieces[p][0]-1][state.pieces[p][1]]=p
                    state.board[state.pieces[p][0]-1][state.pieces[p][1]+1]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                    state.board[state.pieces[p][0]][state.pieces[p][1]+1]=0
                    state.pieces[p]=(state.pieces[p][0]-1,state.pieces[p][1])
                    return state
                else:                    
                    return None   
            elif state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]]==0 and state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]+1]==0:
                state.board[state.pieces[p][0]-1][state.pieces[p][1]]=p
                state.board[state.pieces[p][0]-1][state.pieces[p][1]+1]=p
                state.board[state.pieces[p][0]+1][state.pieces[p][1]]=0
                state.board[state.pieces[p][0]+1][state.pieces[p][1]+1]=0
                state.pieces[p]=(state.pieces[p][0]-1,state.pieces[p][1])
                return state
            else:                
                return None                
            
        elif state.board[max(state.pieces[p][0]-1,0)][state.pieces[p][1]]==0:
            state.board[state.pieces[p][0]][state.pieces[p][1]]=0
            state.board[state.pieces[p][0]-1][state.pieces[p][1]]=p
            state.pieces[p]=(state.pieces[p][0]-1,state.pieces[p][1])
            return state
        else:            
            return None   
            
    def move_down(self,piece):
        state = Klostki(self.board, self.pieces, self.move_history)
        p = piece
        if p>0:
            if p%2==0: #mover as verticais
                if state.board[min(state.pieces[p][0]+2,len(state.board)-1)][state.pieces[p][1]]==0:
                    state.board[state.pieces[p][0]+2][state.pieces[p][1]]=p #atualiza a board
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]]=p #atualiza a board
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0 #atualiza a board
                    state.pieces[p]=(state.pieces[p][0]+1,state.pieces[p][1]) #atualiza a posição do topo esquerdo da peça
                    return state
                else:                   
                    return None 
            elif p != 1: #move horizontais 
                if state.board[min(state.pieces[p][0]+1,len(state.board)-1)][state.pieces[p][1]]==0 and state.board[min(state.pieces[p][0]+1,len(state.board)-1)][state.pieces[p][1]+1]==0:
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]]=p
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]+1]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                    state.board[state.pieces[p][0]][state.pieces[p][1]+1]=0
                    state.pieces[p]=(state.pieces[p][0]+1,state.pieces[p][1])
                    return state
                else:                    
                    return None 
            elif state.board[min(state.pieces[p][0]+2,len(state.board)-1)][state.pieces[p][1]]==0 and state.board[min(state.pieces[p][0]+2,len(state.board)-1)][state.pieces[p][1]+1]==0:
                state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                state.board[state.pieces[p][0]][state.pieces[p][1]+1]=0
                state.board[state.pieces[p][0]+2][state.pieces[p][1]]=p
                state.board[state.pieces[p][0]+2][state.pieces[p][1]+1]=p
                state.pieces[p]=(state.pieces[p][0]+1,state.pieces[p][1])
                return state
            else:                
                return None 
            
        elif state.board[min(state.pieces[p][0]+1,len(state.board)-1)][state.pieces[p][1]]==0:
            state.board[state.pieces[p][0]][state.pieces[p][1]]=0
            state.board[state.pieces[p][0]+1][state.pieces[p][1]]=p
            state.pieces[p]=(state.pieces[p][0]+1,state.pieces[p][1])
            return state
        else:            
            return None 

    def move_left(self,piece): 
        state = Klostki(self.board, self.pieces, self.move_history)
        p = piece
        if p>0:
            if p%2==0: 
                if state.board[state.pieces[p][0]][max(state.pieces[p][1]-1,0)]==0 and state.board[state.pieces[p][0]+1][max(state.pieces[p][1]-1,0)]==0:
                    state.board[state.pieces[p][0]][state.pieces[p][1]-1]=p
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]-1]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]]=0
                    state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]-1)
                    return state
                else:                    
                    return None
            elif p != 1:
                if state.board[state.pieces[p][0]][max(state.pieces[p][1]-1,0)]==0:
                    state.board[state.pieces[p][0]][state.pieces[p][1]-1]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]+1]=0
                    state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]-1)
                    return state
                else:                    
                    return None
            elif state.board[state.pieces[p][0]][max(state.pieces[p][1]-1,0)]==0 and state.board[state.pieces[p][0]+1][max(state.pieces[p][1]-1,0)]==0:
                state.board[state.pieces[p][0]][state.pieces[p][1]-1]=p
                state.board[state.pieces[p][0]+1][state.pieces[p][1]-1]=p
                state.board[state.pieces[p][0]][state.pieces[p][1]+1]=0
                state.board[state.pieces[p][0]+1][state.pieces[p][1]+1]=0
                state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]-1)
                return state
            else:                
                return None
        elif state.board[state.pieces[p][0]][max(state.pieces[p][1]-1,0)]==0:
            state.board[state.pieces[p][0]][state.pieces[p][1]-1]=p
            state.board[state.pieces[p][0]][state.pieces[p][1]]=0
            state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]-1)
            return state
        else:           
            return None
        
    def move_right(self,piece): 
        state = Klostki(self.board, self.pieces, self.move_history)
        p = piece
        if p>0:
            if p%2==0: 
                if state.board[state.pieces[p][0]][min(state.pieces[p][1]+1,len(state.board[1])-1)]==0 and state.board[state.pieces[p][0]+1][min(state.pieces[p][1]+1,len(state.board[1])-1)]==0:
                    state.board[state.pieces[p][0]][state.pieces[p][1]+1]=p
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]+1]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                    state.board[state.pieces[p][0]+1][state.pieces[p][1]]=0
                    state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]+1)
                    return state
                
                else: 
                    #print("Não é há espaço livre à direita")
                    return None
            elif p != 1:
                if state.board[state.pieces[p][0]][min(state.pieces[p][1]+2,len(state.board[1])-1)]==0:
                    state.board[state.pieces[p][0]][state.pieces[p][1]+2]=p
                    state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                    state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]+1)
                    return state
                else:
                    #print("Não é há espaço livre à direita")
                    return None
            elif state.board[state.pieces[p][0]][min(state.pieces[p][1]+2,len(state.board[1])-1)]==0 and state.board[state.pieces[p][0]+1][min(state.pieces[p][1]+2,len(state.board[1])-1)]==0:
                state.board[state.pieces[p][0]][state.pieces[p][1]+2]=p
                state.board[state.pieces[p][0]+1][state.pieces[p][1]+2]=p
                state.board[state.pieces[p][0]][state.pieces[p][1]]=0
                state.board[state.pieces[p][0]+1][state.pieces[p][1]]=0
                state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]+1)
                return state
            else:
                #print("Não é há espaço livre à direita")
                return None
        elif state.board[state.pieces[p][0]][min(state.pieces[p][1]+1,len(state.board[1])-1)]==0: 
            state.board[state.pieces[p][0]][state.pieces[p][1]+1]=p
            state.board[state.pieces[p][0]][state.pieces[p][1]]=0
            state.pieces[p]=(state.pieces[p][0],state.pieces[p][1]+1)
            return state
        else:
            #print("Não é há espaço livre à direita")
            return None

  
    def test_goal(self):
        
        mid_of_board=len(self.board[0])//2-1 #como len(self.board[0]) é par irá ter o valor da posição da esquerda por isso depois +1 para verificar

        if 1==self.board[-1][mid_of_board] and self.board[-1][mid_of_board+1]==1: #basta analisar se as duas coordenadas de baixo correspondem como é um quadrado 2x2
            return True
        return False
    
        
def convert_board_to_str(board):
    board_str = ""
    for row in range(len(board)):
        board_str += "| "
        for col in range(len(board[0])):
            if board[row][col] == 0:
                board_str += ' '
            else:
                board_str += str(board[row][col])
            board_str += " | "
        board_str += "\n------------------\n"
    return board_str

def print_sequence(resultados):
    
    print("Steps:", len(resultados.move_history) - 1)
    for move in resultados.move_history:
        print(convert_board_to_str(move))
        print()

def problems(numero): #adicionar o numero do board para resolver/jogar
    niveis_boards=[[[0,1,1,0],      #n1
                    [0,1,1,0],
                    [2,0,0,-4],
                    [2,-1,-2,-3]],
                [[3,3,1,1],         #n2
                 [0,2,1,1],
                 [-1,2,0,-2],
                 [0,0,-3,-4]],
                [[4,-3,1,1],        #n3
                 [4,2,1,1],
                 [0,2,-1,0],
                 [-4,0,-2,0]],  
                [[-1,3,3,-2],       #n4 
                 [2,1,1,4],
                 [2,1,1,4],
                 [6,-3,-4,8],
                 [6,0,0,8]],
                [[2,0,0,0],         #n5
                 [2,-1,-2,0],
                 [1,1,3,3],
                 [1,1,4,0],
                 [-3,0,4,0]],
                [[3,3,1,1],         #n6 
                 [0,0,1,1],
                 [5,5,0,-1],
                 [0,0,2,0],
                 [-2,0,2,0]],
                [[1,1,0,-1,0,0],    #N7
                 [1,1,0,0,0,0],
                 [0,3,3,0,0,0],
                 [0,2,5,5,-2,0],
                 [-3,2,0,-4,0,0]],
                [[2,1,1,0,0,0],      #N8
                 [2,1,1,0,0 ,0],
                 [0,-1,3,3,0,0],
                 [-2,6,-5,-6,4,0],
                 [-3,6,5,5,4,-4]],
                [[-1,1,1,-2],        #n9 
                 [0,1,1,4],
                 [0,-3,0,4],
                 [6,-4,-5,0],
                 [6,0,0,0]]]
    
    indicador = dicionario(niveis_boards[numero])
    return Klostki(niveis_boards[numero],indicador)

def dicionario(nivel_board):
    pieces = {}
    for i in range(len(nivel_board)):
        for j in range(len(nivel_board[i])):
            piece_id = nivel_board[i][j] # 0, 1, 2
            if piece_id not in pieces and piece_id != 0:
                pieces[piece_id] = (i, j) # pieces[2] = (1, 0)
    return pieces

def bfs(problems):


    queue = [problems]

    while queue:
        board = queue.pop(0)
        
        if board.test_goal():
            resultados=board
            break
        
        for child in board.children():
            
            queue.append(child)

            
    return resultados

def h1(board):
    mid_of_board=(len(board.board[0])//2)-1
    if board.pieces[1]==(len(board.board)-2,mid_of_board):
        return 0
    else:
        peças = []
        for i in range(-2,0):
            for j in range(mid_of_board,mid_of_board+2):
                if board.board[i][j] != 0 and board.board[i][j] != 1 and board.board[i][j] not in peças:
                    peças.append(board.board[i][j])
        return len(peças)+1


def h2(board):
    # heuristic function 2
    # returns the sum of manhattan distances from incorrect placed pieces to their correct place

    mid_of_board=(len(board.board[0])//2)-1
    row,col = board.pieces[1]
    h2 = abs(len(board.board)-2-row) + abs(mid_of_board-col) +(h1(board)-1)

    return h2


def greedy_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    setattr(Klostki, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice

    while states:
        current=heapq.heappop(states)
        visited.add(current)
 

        if current.test_goal():
            return current

        for child in current.children():
            if child not in visited:
                visited.add(child)
                heapq.heappush(states, child)

    return None

def a_star_search(problem, heuristic):
    return greedy_search(problem, lambda state: heuristic(state) + len(state.move_history) - 1)
