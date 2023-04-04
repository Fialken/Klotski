from copy import deepcopy
import heapq

class Klostki:
    def __init__(self,board,pieces,move_history=[],escolhida=None,possible_moves=[]):
        self.board = deepcopy(board) 
        self.pieces=deepcopy(pieces)
        #usado no pygame
        self.escolhida= escolhida
        self.possible_moves= possible_moves

        self.move_history = [] + move_history + [self.board]

    def __str__(self): #mesmo codigo da folha2 que usaram para printar a board
        return convert_board_to_str(self.board)

    
    def children(self):
        # returns the possible moves
        functions = [self.move_up, self.move_down, self.move_left, self.move_right]

        children = []
        for func in functions:
            #print(func)##
            for piece in self.pieces:
                #print(piece)##
                child = func(piece) 
                if child: #if type(child) != str:
                    children.append(child)
        return children


#value of board;
#if value%2 == 0 and value < 10,double piece vertical
#if value%2 != 0 and value != 1 < 10, double piece horizontaly
#if value < 0, sigle piece
#if value == 1, big piece *peça objetivo*
#if value == 0, free space


    def move_up(self,piece): #mover as peças para cima
        #state = Klostki(self.board,self.pieces, self.move_history)
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
        #state = Klostki(self.board, self.pieces, self.move_history)
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
        #state = Klostki(self.board, self.pieces, self.move_history)
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
        #state = Klostki(self.board, self.pieces, self.move_history)
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


    def mover(self,p,row,col):
        if self.pieces[p][0]-1==row and self.pieces[p][1]==col:
            return self.move_up(p)
        if self.pieces[p][0]+1==row and self.pieces[p][1]==col:
            return self.move_down(p)
        if self.pieces[p][0]==row and self.pieces[p][1]-1==col:
            return self.move_left(p)
        if self.pieces[p][0]==row and self.pieces[p][1]+1==col:
            return self.move_right(p)
            


            
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
    #for i in range(len(resultados)):
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
            # found the best solution
            return current

        for child in current.children():
            if child not in visited:
                heapq.heappush(states, child)

    return None



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import os

nivel=problems(0) #nivel para jogar

def update(self):
    desenhar_problema(self)
    desenhar_moves(self)
    pygame.display.update()

WIDTH, HEIGHT = 800,800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Klotski")

#variables
RED = (255, 0, 0)
WHITE = (255,255,255)
FPS = 60
BLOCK_WIDTH = BLOCK_HEIGHT = 100
VEL = 5

#images for background and blocks
BACKGROUND = pygame.image.load(os.path.join("Assets", "space.png"))
WINNER = pygame.image.load(os.path.join("Assets", "winner.png"))
INDIVIDUAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "individual1.png"))
VERTICAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "vertical1.png"))
HORIZONTAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "horizontal1.png"))
FINAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "final.png"))


'''
def draw_window(vertical,horizontal,individual,final):
    WINDOW.fill(WHITE)
    WINDOW.blit(INDIVIDUAL_BLOCK_IMAGE,(individual.x,individual.y))
    WINDOW.blit(VERTICAL_BLOCK_IMAGE,(vertical.x,vertical.y))
    WINDOW.blit(HORIZONTAL_BLOCK_IMAGE,(horizontal.x,horizontal.y))
    WINDOW.blit(FINAL_BLOCK_IMAGE,(final.x,final.y))
    pygame.display.update()

def vertical_handle_movemente(keys_pressed,vertical):
    if keys_pressed[pygame.K_a]: #LEFT
        vertical.x -= VEL
    if keys_pressed[pygame.K_d]: #LEFT
        vertical.x += VEL
    if keys_pressed[pygame.K_w]: #LEFT
        vertical.y -= VEL
    if keys_pressed[pygame.K_s]: #LEFT
        vertical.y += VEL

def final_handle_movemente(keys_pressed,final):
    if keys_pressed[pygame.K_LEFT]: #LEFT
        final.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: #LEFT
        final.x += VEL
    if keys_pressed[pygame.K_UP]: #LEFT
        final.y -= VEL
    if keys_pressed[pygame.K_DOWN]: #LEFT
        final.y += VEL
'''

def get_position(nivel,pos):
    x,y=pos[0],pos[1]
    row= min((y-margem_y) // 100,len(nivel.board)-1)
    col= min((x-margem_x) // 100,len(nivel.board[0])-1)
    if row < 0 or col <0:
        return 0,0
    return row, col # x, y

margem_y=100
if len(nivel.board[0])==4: #controlo do x
    margem_x=200
else: margem_x=100

def desenhar_problema(self):       
    for p in self.pieces:
        if p >0:
            if p%2 == 0: #vert    #Rect(x,y,_,_)
                piece =pygame.Rect(100*self.pieces[p][1]+margem_x,100*self.pieces[p][0]+margem_y,BLOCK_WIDTH,2*BLOCK_HEIGHT)
                WINDOW.blit(VERTICAL_BLOCK_IMAGE,(piece.x,piece.y))
            else:
                if p != 1: #hori
                    piece =pygame.Rect(100*self.pieces[p][1]+margem_x,100*self.pieces[p][0]+margem_y,2*BLOCK_WIDTH,BLOCK_HEIGHT)
                    WINDOW.blit(HORIZONTAL_BLOCK_IMAGE,(piece.x,piece.y))
                else: #2x2
                    piece =pygame.Rect(100*self.pieces[p][1]+margem_x,100*self.pieces[p][0]+margem_y,2*BLOCK_WIDTH,2*BLOCK_HEIGHT)
                    WINDOW.blit(FINAL_BLOCK_IMAGE,(piece.x,piece.y))
        elif p!= 0: #uni
            piece =pygame.Rect(100*self.pieces[p][1]+margem_x,100*self.pieces[p][0]+margem_y,BLOCK_WIDTH,BLOCK_HEIGHT)
            WINDOW.blit(INDIVIDUAL_BLOCK_IMAGE,(piece.x,piece.y))

def desenhar_moves(self): #desenha onde são as possiveis jogadas
    p=self.escolhida
    if p:
        for func in self.possible_moves:
            if func==self.move_up:
                pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y-25), 20)

            if func==self.move_right:
                if p==1 or (p>0 and p%2!=0):
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+225, 100*self.pieces[p][0]+margem_y+50), 20)
                else: pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+125, 100*self.pieces[p][0]+margem_y+50), 20)
            if func==self.move_down:
                if p==1 or (p>0 and p%2==0):
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y+225), 20)
                    
                else:
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y+75), 20)
                
            if func==self.move_left:
                pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x-25, 100*self.pieces[p][0]+margem_y+50), 20)

def piece_chosen(self,row,col):
    piece=self.board[row][col]

    if self.escolhida:
        p=self.escolhida
        self.mover(p,row,col)
        self.escolhida= None



    if piece: #para representar onde é possivel mover
        self.escolhida=piece
        self.possible_moves=[]
        functions = [self.move_up, self.move_down, self.move_left, self.move_right]
        for func in functions:
            move = func(piece) 
            if move:
                self.possible_moves.append(func)
        return True
    return False




    





def main(game):
    
    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)

        if game.test_goal():
            WINDOW.blit(WINNER,(200,600))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col=get_position(game,pos)
                piece_chosen(game,row,col)
            


        update(game)
        WINDOW.blit(BACKGROUND, (0,0))

    pygame.quit()


if __name__ == "__main__":
    main(problems(0))

print(problems(0))