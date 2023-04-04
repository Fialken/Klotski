

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
        functions = [Klostki.move_up, Klostki.move_down, Klostki.move_left, Klostki.move_right]
        children = []
        for func in functions:
            
            for piece in self.pieces:
                temp=deepcopy(self)
                child = func(temp,piece)
                if child: 
                    child.move_history.insert(-1,self.board)                  
                    children.append(child)
        return children


#value of board;
#if value%2 == 0 and value < 10,double piece vertical
#if value%2 != 0 and value != 1 < 10, double piece horizontaly
#if value < 0, sigle piece
#if value == 1, big piece *peça objetivo*
#if value == 0, free space


    def move_up(self,piece): #mover as peças para cima
        p = piece
        if p>0:
            if p%2==0: #mover as verticais
                if self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0:
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0 #atualiza a board
                    self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1]) #atualiza a posição do topo esquerdo da peça
                    return self
                else:
                    #print("Nao há espaço livre em cima")
                    return None   
            elif p != 1:
                if self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0 and self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]+1]==0:
                    
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]+1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                    self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1])
                    return self
                else:
                    #print("Nao há espaço livre em cima")
                    return None   
            elif self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0 and self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]+1]==0:
                
                self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p
                self.board[self.pieces[p][0]-1][self.pieces[p][1]+1]=p
                self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=0
                self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1])
                return self
            else:
                #print("Nao há espaço livre em cima")
                return None                
            
        elif self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0:
           
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p
            self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1])
            return self
        else:
            #print("Nao há espaço livre em cima")
            return None   
            
    def move_down(self,piece):
        
        p = piece
        if p>0:
            if p%2==0: #mover as verticais
                if self.board[min(self.pieces[p][0]+2,len(self.board[1])-1)][self.pieces[p][1]]==0:
                    
                    self.board[self.pieces[p][0]+2][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0 #atualiza a board
                    self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1]) #atualiza a posição do topo esquerdo da peça
                    return self
                else:
                    #print("Nao há espaço livre em baixo")
                    return None 
            elif p != 1: #move horizontais 
                if self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]]==0 and self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]+1]==0:
                   
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                    self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
                    return self
                else:
                    #print("Nao há espaço livre em baixo")
                    return None 
            elif self.board[min(self.pieces[p][0]+2,len(self.board)-1)][self.pieces[p][1]]==0 and self.board[min(self.pieces[p][0]+2,len(self.board)-1)][self.pieces[p][1]+1]==0:
                
                self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                self.board[self.pieces[p][0]+2][self.pieces[p][1]]=p
                self.board[self.pieces[p][0]+2][self.pieces[p][1]+1]=p
                self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
                return self
            else:
                #print("Nao há espaço livre em baixo")
                return None 
            
        elif self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]]==0:
            
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p
            self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
            return self
        else:
            #print("Nao há espaço livre em baixo")
            return None 

    def move_left(self,piece): 
        
        p = piece
        if p>0:
            if p%2==0: 
                if self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0 and self.board[self.pieces[p][0]+1][max(self.pieces[p][1]-1,0)]==0:
                    
                    self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]-1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
                    return self
                
                else: 
                    #print("Não é há espaço livre à esquerda")
                    return None
            elif p != 1:
                if self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0:
                    
                    self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
                    return self
                else:
                    #print("Não é há espaço livre à esquerda")
                    return None
            elif self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0 and self.board[self.pieces[p][0]+1][max(self.pieces[p][1]-1,0)]==0:
                
                self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
                self.board[self.pieces[p][0]+1][self.pieces[p][1]-1]=p
                self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=0
                self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
                return self
            else:
                #print("Não é há espaço livre à esquerda")
                return None
        elif self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0:
            
            self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
            return self
        else:
            #print("Não é há espaço livre à esquerda")
            return None
        
    def move_right(self,piece): 
       
        p = piece
        if p>0:
            if p%2==0: 
                if self.board[self.pieces[p][0]][min(self.pieces[p][1]+1,len(self.board[1])-1)]==0 and self.board[self.pieces[p][0]+1][min(self.pieces[p][1]+1,len(self.board[1])-1)]==0:
                    
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=p
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
                    return self
                
                else: 
                    #print("Não é há espaço livre à direita")
                    return None
            elif p != 1:
                if self.board[self.pieces[p][0]][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0:
                    
                    self.board[self.pieces[p][0]][self.pieces[p][1]+2]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
                    return self
                else:
                    #print("Não é há espaço livre à direita")
                    return None
            elif self.board[self.pieces[p][0]][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0 and self.board[self.pieces[p][0]+1][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0:
                
                self.board[self.pieces[p][0]][self.pieces[p][1]+2]=p
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+2]=p
                self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0
                self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
                return self
            else:
                #print("Não é há espaço livre à direita")
                return None
        elif self.board[self.pieces[p][0]][min(self.pieces[p][1]+1,len(self.board[1])-1)]==0: 
            
            self.board[self.pieces[p][0]][self.pieces[p][1]+1]=p
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
            return self
        else:
            #print("Não é há espaço livre à direita")
            return None

        
            
    def test_goal(self):
        # checks if the board is complete
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
    # prints the sequence of states
    for move in resultados.move_history:
        print(convert_board_to_str(move))
        print()

def problems(numero): #adicionar o numero do board para resolver/jogar
    niveis_boards=[[[0,1,1,0],
                    [0,1,1,0],
                    [2,0,0,-4],
                    [2,-1,-2,-3]],
                   [[0,3,3,0],
                [0,0,1,1],
                [0,0,1,1],
                [0,4,0,0],
                [0,4,-2,0]]]
    
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
    

    mid_of_board=(len(board.board[0])//2)-1
    row,col = board.pieces[1]
    h2 = abs(len(board.board)-2-row) + abs(mid_of_board-col) +(h1(board)-1)

    return h2


def greedy_search(problem, heuristic):
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



print('BFS')
print_sequence(bfs(problems(1)))

print('H1')
print_sequence(greedy_search(problems(1),h1))



print('H2')

print_sequence(greedy_search(problems(1),h2))

#print_sequence(greedy_search(problems(0),h2))
