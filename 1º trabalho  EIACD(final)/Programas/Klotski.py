from copy import deepcopy
import heapq

class Klostki: #cria uma class
    def __init__(self,board,pieces,move_history=[],escolhida=None,possible_moves=[]): #a class contem um board que é uma matriz, contem um dicionario "pieces" com todas as peças do board
        self.board = deepcopy(board)                                                  #assossiadas as suas respetivas coordenadas, contem uma lista de movimentos possiveis,
        self.pieces=deepcopy(pieces)                                                  #e o "esolhida" indica se está alguma peça selecionada no momento
        self.move_history = [] + move_history + [self.board]
        #alterações para o pygame
        self.escolhida= escolhida #para saber qual peça foi selecionada pelo utilizador
        self.possible_moves= possible_moves #lista para saber quais são as possiveis moves da peça selecionada pelo utilizador


    def __str__(self): #codigo para imprimir o board
        return convert_board_to_str(self.board)

    
    def children(self):
        # retorna os movimentos possiveis
        functions = [Klostki.move_up, Klostki.move_down, Klostki.move_left, Klostki.move_right] #todos os movimentos existentes
        children = [] #cria uma lista vazia
        for func in functions:
            
            for piece in self.pieces:
                temp=deepcopy(self) #como nas funções de move_** o objeto é alterado, criamos uma cópia temporaria do objeto para modificar essa cópia e encontrar as possiveis childs
                child = func(temp,piece) #criar as childs apartir da cópia
                if child: #se a child for uma move possivel então vai adicionar
                    child.move_history.insert(-1,self.board) #adiciona a board do objeto inicial ao move history da nova child, insert(-1,) para ficar na ordem correta para quando pedida a solução
                    children.append(child) #adiciona a child há lista inicialmente criada
        return children #retorna os movimentos possiveis



#destinção das peças;
#se o valor for 1, entao pertence ao quadrado principal
#se o valor for 0, é um espaço livre
#se o valor for divisivel por 2 == 0 pertence a um retangulo vertical
#se o valor não for divisivel por 2 e for maior que 1 pertence a um retagulo horizontal
#se o valor for inferior a 0 é uma quadrado individual

#todos os movimentos
    def move_up(self,piece): #mover as peças para cima
        #state = Klostki(self.board,self.pieces, self.move_history)
        p = piece
        if p>0:
            if p%2==0: #verifica se é uma retangulo vertical
                if self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0: # verifica se tem espaço em cima da peça para a mover
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=p #atualiza a board
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0 #atualiza a board
                    self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1]) #atualiza o dicionario
                    return self
                else:
                    return None  #caso não haja espaço livre em cima 
                
            elif p != 1: #verifica se é um retangulo horizontal
                if self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0 and self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]+1]==0: #verifica se há espaço suficiente em cima para mover
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p #atualiza o board
                    self.board[self.pieces[p][0]-1][self.pieces[p][1]+1]=p #atualiza o board
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0 #atualiza o board
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0 #atualiza o board
                    self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1]) #atualiza o dicionario
                    return self
                else:
                    return None #caso não haja espaço livre em cima
                
            #peça principal     
            elif self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0 and self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]+1]==0: #verifica se há espaço suficiente em cima para mover
                self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p #atualiza o board
                self.board[self.pieces[p][0]-1][self.pieces[p][1]+1]=p #atualiza o board
                self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0 #atualiza o board
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=0 #atualiza o board
                self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1]) #atualiza o dicionario
                return self
            else:
                return None #caso não haja espaço livre em cima               

         #peça individual
        elif self.board[max(self.pieces[p][0]-1,0)][self.pieces[p][1]]==0:#verifica se há espaço suficiente em cima para mover
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0 #atualiza o board
            self.board[self.pieces[p][0]-1][self.pieces[p][1]]=p #atualiza o board
            self.pieces[p]=(self.pieces[p][0]-1,self.pieces[p][1]) #atualiza o dicionario
            return self
        else:
            return None #caso não haja espaço livre em cima  
    
    
    def move_down(self,piece): #move as peças para baixo, funciona exatamente igual ao move_up com as devidas alteraçoes para mover para baixo
        p = piece
        if p>0:
            if p%2==0: 
                if self.board[min(self.pieces[p][0]+2,len(self.board)-1)][self.pieces[p][1]]==0:
                    self.board[self.pieces[p][0]+2][self.pieces[p][1]]=p 
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p 
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0 
                    self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
                    return self
                else:
                    return None 
                
            elif p != 1:
                if self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]]==0 and self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]+1]==0:
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p
                    self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                    self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
                    return self
                else:
                    return None 
                
            elif self.board[min(self.pieces[p][0]+2,len(self.board)-1)][self.pieces[p][1]]==0 and self.board[min(self.pieces[p][0]+2,len(self.board)-1)][self.pieces[p][1]+1]==0:
                self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                self.board[self.pieces[p][0]+2][self.pieces[p][1]]=p
                self.board[self.pieces[p][0]+2][self.pieces[p][1]+1]=p
                self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
                return self
            else:
                return None 
            
        elif self.board[min(self.pieces[p][0]+1,len(self.board)-1)][self.pieces[p][1]]==0:
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.board[self.pieces[p][0]+1][self.pieces[p][1]]=p
            self.pieces[p]=(self.pieces[p][0]+1,self.pieces[p][1])
            return self
        else:
            return None 

    def move_left(self,piece): #move as peças para a esquerda, funciona exatamente igual ao move_up com as devidas alteraçoes para mover para esquerda
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
                    return None
                
            elif p != 1:
                if self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0:
                    self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
                    return self
                else:
                    return None
                
            elif self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0 and self.board[self.pieces[p][0]+1][max(self.pieces[p][1]-1,0)]==0:
                self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
                self.board[self.pieces[p][0]+1][self.pieces[p][1]-1]=p
                self.board[self.pieces[p][0]][self.pieces[p][1]+1]=0
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+1]=0
                self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
                return self
            else:
                return None
            
        elif self.board[self.pieces[p][0]][max(self.pieces[p][1]-1,0)]==0:
            self.board[self.pieces[p][0]][self.pieces[p][1]-1]=p
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]-1)
            return self
        else:
            return None
        
    def move_right(self,piece): #move as peças para a direita, funciona exatamente igual ao move_up com as devidas alteraçoes para mover para a direita
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
                    return None
                
            elif p != 1:
                if self.board[self.pieces[p][0]][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0:
                    self.board[self.pieces[p][0]][self.pieces[p][1]+2]=p
                    self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                    self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
                    return self
                else:
                    return None
                
            elif self.board[self.pieces[p][0]][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0 and self.board[self.pieces[p][0]+1][min(self.pieces[p][1]+2,len(self.board[1])-1)]==0:
                self.board[self.pieces[p][0]][self.pieces[p][1]+2]=p
                self.board[self.pieces[p][0]+1][self.pieces[p][1]+2]=p
                self.board[self.pieces[p][0]][self.pieces[p][1]]=0
                self.board[self.pieces[p][0]+1][self.pieces[p][1]]=0
                self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
                return self
            else:
                return None
            
        elif self.board[self.pieces[p][0]][min(self.pieces[p][1]+1,len(self.board[1])-1)]==0: 
            self.board[self.pieces[p][0]][self.pieces[p][1]+1]=p
            self.board[self.pieces[p][0]][self.pieces[p][1]]=0
            self.pieces[p]=(self.pieces[p][0],self.pieces[p][1]+1)
            return self
        else:
            return None

    def mover(self,p,row,col): #função para o objeto ser interativo no pygame quando selecionada a orientação para mover o peça selecionada
        #move_up
        if self.pieces[p][0]-1==row and self.pieces[p][1]==col:
            return self.move_up(p)
        #move_left
        if self.pieces[p][0]==row and self.pieces[p][1]-1==col:
            return self.move_left(p)
        
        #move_down 
        if p>0 and (p==1 or p%2==0):
            if self.pieces[p][0]+2==row and self.pieces[p][1]==col:
                return self.move_down(p)

        elif self.pieces[p][0]+1==row and self.pieces[p][1]==col:
            return self.move_down(p)
        
        #move_right
        if p >0 and (p==1 or p%2!=0):
            if self.pieces[p][0]==row and self.pieces[p][1]+2==col:
                return self.move_right(p)
            
        elif self.pieces[p][0]==row and self.pieces[p][1]+1==col:
            return self.move_right(p)
            
    def test_goal(self): #verifica se chegamos ao objetivo

        mid_of_board=len(self.board[0])//2-1 #como len(self.board[0]) é par irá ter o valor da posição da esquerda por isso depois +1 para verificar

        if 1==self.board[-1][mid_of_board] and self.board[-1][mid_of_board+1]==1: #verifica usando o dicionario se a peça principal está na posiçao correta
            return True
        return False
    
def dicionario(nivel_board): #cria um dicionario que para cada um dos diferentes valores do board associa á sua primeira coordenada da matriz( a parte da peça mais a cima e mais á esquerda)
    pieces = {} #cria um dicionario vazio
    for i in range(len(nivel_board)): #precorre as linhas da matriz
        for j in range(len(nivel_board[i])): #precorre as colunas da matriz
            piece_id = nivel_board[i][j] #valor na matriz da linha i e da coluna j
            if piece_id not in pieces and piece_id != 0: #verifica se o valor ainda nao existe o dicionario
                pieces[piece_id] = (i, j) #caso nao existe adiciona ao dicionario esse valor e assossia-lhe as suas coordenadas
    return pieces #retorna o dicionario correspondente ao board que recebeu
    
def problems(numero): #função onde podemos vir buscar os problemas
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
                 [2,1,1,0,0,0],
                 [0,-1,3,3,0,0],
                 [-2,6,-5,-6,4,0],
                 [-3,6,5,5,4,-4]],
                [[-1,1,1,-2],        #n9 
                 [0,1,1,4],
                 [0,-3,0,4],
                 [6,-4,-5,0],
                 [6,0,0,0]]] #uma lista de matrizes em que cada matriz é um board/nivel
    
    indicador = dicionario(niveis_boards[numero]) #cria um dicionario para o respetivo board selecionado usando a função "dicionario"
    return Klostki(niveis_boards[numero],indicador) #retorna um objeto da class Klotski com um board e o respetivo dicionario
    
        
def convert_board_to_str(board): #faz o desenho da matriz na consola para quando a baixo nivel facilitar a visualização da board do objeto
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

def print_sequence(resultados): #faz o desenho de cada paço até chegar ao objetivo
    print("Steps:", len(resultados.move_history) - 1)
    for move in resultados.move_history:
        print(convert_board_to_str(move))
        print()



def bfs(problems): #pesquisa bfs
    queue = [problems] #cria uma lista que contem apenas o estado inicial

    while queue: #enquanto a lista nao estiver vazia
        board = queue.pop(0) #usa o primeiro elemento da lista
        
        if board.test_goal(): #verifica se esse elemento é final
            resultados=board
            break #caso seja, sai do ciclo
        
        for child in board.children(): #cada um dos movimentos possiveis
            queue.append(child) #acrescenta cada movimento possivel para o estado atual ao fim da lista

    return resultados #retorna o board em que encontrou a solução


def h1(board): #retorna um valor que resulta da soma de peças no lugar onde deveria estar a peça principal +1(que e a propria pecipal)
    mid_of_board=(len(board.board[0])//2)-1 
    if board.pieces[1]==(len(board.board)-2,mid_of_board):
        return 0 #retorna 0 se a peça principal estiver o sitio correto
    else:
        peças = [] #cria uma lista vazia que vai guardas as peças que estão na posiçao onde deveria estar a peça principal
        for i in range(-2,0): 
            for j in range(mid_of_board,mid_of_board+2): 
                if board.board[i][j] != 0 and board.board[i][j] != 1 and board.board[i][j] not in peças: # verifica se há peças no sitio da principal e garante que cada peça conta apenas uma vez
                    peças.append(board.board[i][j]) #adiciona as peças a lista
        return len(peças)+1 

def h2(board): #conta o numero de paços que seriam necessarios para a peça final chegar ao objetivo caso ela fosse a unica peça no tabuleiro
    mid_of_board=(len(board.board[0])//2)-1
    row,col = board.pieces[1]
    h2 = abs(len(board.board)-2-row) + abs(mid_of_board-col) +(h1(board)-1) #calcula o numero de paços
    return h2 

def greedy_search(problem, heuristic): #pesquisa greedy
    setattr(Klostki, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]#cria uma lista que contem o estado inicial do tabuleiro
    visited = set()#para não repetir estados
    while states:
        current=heapq.heappop(states)#retira o primeiro elemento da lisra
        visited.add(current)
        if current.test_goal():#verifica se o estado da lista é o objetivo
            return current

        for child in current.children():#cria novos estados apartir do estado analisado
            if child not in visited:
                heapq.heappush(states, child)#poe os estados na lista por ordem da heuristica utilizando uma heap
    return None

def a_star_search(problem, heuristic):
    return greedy_search(problem, lambda state: heuristic(state) + len(state.move_history) - 1)


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import os
pygame.init()


def update(self,margem_x,margem_y,steps_done):
    WINDOW.blit(BACKGROUND, (0,0))
    WINDOW.blit(RESET_BUTTON, (100,600))
    WINDOW.blit(HELP_BUTTON, (600,600))
    draw_text("Pode demorar um pouco", font3, TEXT_COL, 575,700)
    draw_text("Não mexer em nada", font3, TEXT_COL, 575,730) 
    steps="Steps: "+str(steps_done)   
    draw_text(steps, font1, TEXT_COL, 300,25)
    desenhar_problema(self,margem_x,margem_y)
    desenhar_moves(self,margem_x,margem_y)
    pygame.display.update()

def update_win(self,margem_x,margem_y,steps_done):
    WINDOW.blit(BACKGROUND, (0,0))
    WINDOW.blit(RESET_BUTTON, (100,600))
    WINDOW.blit(WINNER,(200,605))
    WINDOW.blit(NEXT_LVL, (600,600))
    steps="Steps: "+str(steps_done)
    draw_text(steps, font1, TEXT_COL, 300,25)
    desenhar_problema(self,margem_x,margem_y)
    desenhar_moves(self,margem_x,margem_y)
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
INTERVALO_TEMPO=100

#images for background and blocks
BACKGROUND = pygame.image.load(os.path.join("Assets", "space.png"))
WINNER = pygame.image.load(os.path.join("Assets", "winner.png"))
INDIVIDUAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "individual1.png"))
VERTICAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "vertical1.png"))
HORIZONTAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "horizontal1.png"))
FINAL_BLOCK_IMAGE = pygame.image.load(os.path.join("Assets", "final.png"))
RESET_BUTTON = pygame.image.load(os.path.join("Assets", "Button_Reset.png"))
SELECT_LEVEL_BUTTON = pygame.image.load(os.path.join("Assets", "Button_Select_Level.png"))
HELP_BUTTON = pygame.image.load(os.path.join("Assets", "Button_Help.png"))
NEXT_BUTTON = pygame.image.load(os.path.join("Assets", "Button_Next.png"))
RULES_BUTTON = pygame.image.load(os.path.join("Assets", "Button_Rules.png"))
NEXT_LVL = pygame.image.load(os.path.join("Assets", "next_lvl.png"))
LUGAR_OBJETIVO = pygame.image.load(os.path.join("Assets", "lugar_objetivo.png"))
BOARDER4X4 = pygame.image.load(os.path.join("Assets", "boarder4x4.png"))
BOARDER4X5 = pygame.image.load(os.path.join("Assets", "boarder4x5.png"))
BOARDER6X5 = pygame.image.load(os.path.join("Assets", "boarder6x5.png"))

def get_position(nivel,pos,margem_x,margem_y):
    x,y=pos[0],pos[1]
    if x>100 and x<200 and y>600 and y<700: #reset ao nivel
        x,y=10,10
        return x,y
    
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_ESCAPE]:
        row = 15
        col = 15
        return row,col
        
    if x>600 and x<700 and y>600 and y <700:#pedir para AI resolver
        x,y=25,25
        return x,y
    
    #tamanho da board para identificar quando nao seleciona nenhuma peça nem função
    if len(nivel.board)==4: #4x4
        if x<200 or x>600 or y<100 or y>500:
                x,y=999,999
                return x,y
    elif len(nivel.board[0])==4: #4x5
        if x<200 or x>600 or y<100 or y>600:
                x,y=999,999
                return x,y
            
    if x<100 or x>700 or y<100 or y>600: #6x5
            x,y=999,999
            return x,y
    
    row= (y-margem_y) // 100
    col= (x-margem_x) // 100
    return row, col # x, y



def desenhar_problema(self,margem_x,margem_y):  
    #desenhar limite das bordas e onde é o local do objetivo
    if len(self.board)==4: #4x4
        WINDOW.blit(LUGAR_OBJETIVO,(300,300))
        WINDOW.blit(BOARDER4X4,(margem_x-5,margem_y-5))
    else:
        WINDOW.blit(LUGAR_OBJETIVO,(300,400))
        if len(self.board[0])==4: #board 4x5
            WINDOW.blit(BOARDER4X5,(margem_x-5,margem_y-5))
        else: #board 6x5
            WINDOW.blit(BOARDER6X5,(margem_x-5,margem_y-5))

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

def desenhar_moves(self,margem_x,margem_y): #desenha onde são as possiveis jogadas
    
    p=self.escolhida
    if p:
        for func in self.possible_moves:
            #temp1=deepcopy(self)
            if func==Klostki.move_up:
                pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y-25), 20)

            if func==Klostki.move_right:
                if p==1 or (p>0 and p%2!=0):
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+225, 100*self.pieces[p][0]+margem_y+50), 20)
                else: pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+125, 100*self.pieces[p][0]+margem_y+50), 20)
            if func==Klostki.move_down:
                if p==1 or (p>0 and p%2==0):
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y+225), 20)
                    
                else:
                    pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x+50, 100*self.pieces[p][0]+margem_y+125), 20)
                
            if func==Klostki.move_left:
                pygame.draw.circle(WINDOW, RED, (100*self.pieces[p][1]+margem_x-25, 100*self.pieces[p][0]+margem_y+50), 20)

def piece_chosen(self,row,col,steps_done,solved):
    piece=self.board[row][col]
    teste=deepcopy(self)
    if self.escolhida:
        p=self.escolhida
        self.mover(p,row,col)
        self.escolhida= None
        if teste.board!=self.board:
            steps_done+=1
            solved=None


    if piece: #para representar onde é possivel mover
        self.escolhida=piece
        self.possible_moves=[]
        functions = [Klostki.move_up, Klostki.move_down, Klostki.move_left, Klostki.move_right]
        for func in functions:
            temp2=deepcopy(self)
            move = deepcopy(func(temp2,piece))
            if move:
                self.possible_moves.append(func)

    return steps_done,solved




#####implementação do menu inicial
N1 = pygame.image.load(os.path.join("Assets", "N1.png"))
N2 = pygame.image.load(os.path.join("Assets", "N2.png"))
N3 = pygame.image.load(os.path.join("Assets", "N3.png"))
N4 = pygame.image.load(os.path.join("Assets", "N4.png"))
N5 = pygame.image.load(os.path.join("Assets", "N5.png"))
N6 = pygame.image.load(os.path.join("Assets", "N6.png"))

N7 = pygame.image.load(os.path.join("Assets", "N7.png"))
N8 = pygame.image.load(os.path.join("Assets", "N8.png"))
N9 = pygame.image.load(os.path.join("Assets", "N9.png"))


CENTRAR=0


RULES_BUTTON_FINAL = pygame.image.load(os.path.join("Assets", "rules_300x250.png"))
SELECT_LEVEL = pygame.image.load(os.path.join("Assets", "select_level_300x250.png"))
LIGHTBLUE=(52,78,91) #COR DO MENU INICIAL

def get_pos2(pos1):
    x,y=pos1[0],pos1[1]
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            return 998

    if x>250 and x<550 and y>150 and y<400:
        #abrir_rules
        lvl=menu_rules()
        return lvl #para o ciclo nao parar *lvl=999 é o codigo para saber q o lvl ainda nao foi escolhido
    if x>250 and x<550 and y>400 and y<650:
        lvl=menu_level()
        return lvl
    
    return 999

def get_pos_nivel(pos2): #saber qual nivel foi escolhido
    x2,y2=pos2[0],pos2[1]
    level_temp=999

    if y2<200 and x2>100+CENTRAR and x2<300+CENTRAR:#nivel1
        level_temp=0
    if y2<200 and x2>300+CENTRAR and x2<500+CENTRAR:#nivel2
        level_temp=1
    if y2<200 and x2>500 and x2<700:#nivel3
        level_temp=2
    if y2>300 and y2<500 and x2>100+CENTRAR and x2<300+CENTRAR:#nivel4
        level_temp=3
    if y2>300 and y2<500 and x2>300+CENTRAR and x2<500+CENTRAR:#nivel5
        level_temp=4
    if y2>300 and y2<500 and x2>500+CENTRAR and x2<700+CENTRAR:#nivel6
        level_temp=5
    if y2>600 and x2>100+CENTRAR and x2<300+CENTRAR:#nivel7
        level_temp=6
    if y2>600 and x2>300+CENTRAR and x2<500+CENTRAR:#nivel8
        level_temp=7
    if y2>600 and x2>500+CENTRAR and x2<700+CENTRAR:#nivel9
        level_temp=8
    
    return level_temp

def menu_level(): #criar janela para escolher os niveis
    lvl2=999
    run2=True
    WINDOW.blit(BACKGROUND, (0,0))
    WINDOW.blit(N1, (100+CENTRAR,0))
    WINDOW.blit(N2, (300+CENTRAR,0))
    WINDOW.blit(N3, (500+CENTRAR,0))
    WINDOW.blit(N4, (100+CENTRAR,300))
    WINDOW.blit(N5, (300+CENTRAR,300))
    WINDOW.blit(N6, (500+CENTRAR,300))
    WINDOW.blit(N7, (100+CENTRAR,600))
    WINDOW.blit(N8, (300+CENTRAR,600))
    WINDOW.blit(N9, (500+CENTRAR,600))
    #falta imagem dos niveis, como eles são

    pygame.display.update()
    
    
    while run2 and lvl2==999:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run2 = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos2 = pygame.mouse.get_pos()
                lvl2=get_pos_nivel(pos2)

        keys_pressed=None
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            pygame.time.wait(INTERVALO_TEMPO)
        if keys_pressed[pygame.K_ESCAPE]:
            flag=1
            menu_inicial(run2,flag)





    if run2==False:
        pygame.quit()
        lvl2=998#codigo para saber que o jogo foi fechado


    return lvl2

def menu_rules():
    lvl3=999
    run3=True
    while run3 and lvl3==999:
        keys_pressed=None
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            pygame.time.wait(INTERVALO_TEMPO)
        if keys_pressed[pygame.K_ESCAPE]:
            lvl3=997

        WINDOW.fill(LIGHTBLUE)
        WINDOW.blit(SELECT_LEVEL,(225,300))
        rules = ["Your playing Klotsky, a simple board game from the twentieth century.","The rules are simple, you have to move the main piece to the midle posicion in the bottom line.","In order to do so you can move any piece using the free spaces."]
        n = 0
        for _ in range(3):
            draw_text(rules[n], font3, TEXT_COL, 50,100+50*n)
            n+=1
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run3 = False

            if evento.type == pygame.MOUSEBUTTONDOWN: 
                    pos3 = pygame.mouse.get_pos()
                    x,y=pos3[0],pos3[1]
                    if x>250 and x<550 and y>300 and y<600:
                        lvl3=menu_level()

   

    if run3==False:
        pygame.quit()
        lvl3=998

    return lvl3

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WINDOW.blit(img, (x,y))


def draw_final(text, font3, text_col, x, y):
    img = font3.render(text,True, text_col)
    WINDOW.blit(img ,(x, y))

#define font
font1 = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("arialblack",25)
font3 = pygame.font.SysFont("arialblack",13)

#text color
TEXT_COL = (255,255,255)

def menu_inicial(run,flag): 
    lvl=999
    while run and lvl==999:
        
        pygame.display.update()
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed=None
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            pygame.time.wait(INTERVALO_TEMPO)
        if keys_pressed[pygame.K_ESCAPE]:
            flag = 0
        if keys_pressed[pygame.K_SPACE]:
            flag = 1
        #

        if flag == 0:#inicio
            WINDOW.fill(LIGHTBLUE)
            draw_text("Press Space to start", font1, TEXT_COL, 160, 350)

        if flag == 1:#rules ou lvls
            WINDOW.fill(LIGHTBLUE)
            WINDOW.blit(RULES_BUTTON_FINAL,(250,150))
            WINDOW.blit(SELECT_LEVEL,(250,400))
            draw_text("Press ESC to go Back", font2, TEXT_COL, 500,770)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos1 = pygame.mouse.get_pos()
                    lvl=get_pos2(pos1)
                    if lvl==998: #se fechar a window no menu da seleção de niveis ou nas regras
                        return 999
                    elif lvl==997:#selecionar esc voltar para primeira window
                        flag=1
                        lvl=999
    if run==False:
        pygame.quit()
        
    
    return lvl
    
#####


def margens(nivel): #para adaptar as marguens em função da dimensão da board
    #margens para a board ficar centrada
    margem_y=100
    if len(nivel.board[0])==4: #controlo do x
        margem_x=200
    else: margem_x=100
    return margem_x,margem_y

def AI_SOLVER(game): #pedir para o algoritmo A* resolver o nivel na atual 
    return a_star_search(game, h2)






def main():
    clock = pygame.time.Clock()
    run = True
    solved=None
    flag=0
    steps_done=0
    nivel=menu_inicial(run,flag)
    if nivel==999 or nivel==998: #caso seja fechado o jogo no menu inicial
        return
    
    game=problems(nivel)    
    reset=deepcopy(game)

    while run:
        margem_x,margem_y=margens(game)
        clock.tick(FPS)

        if game.test_goal():
            solved=None
            
            update_win(game,margem_x,margem_y,steps_done)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pos2 = pygame.mouse.get_pos()
                x,y= pos2[0], pos2[1]
                if x>600 and x<700 and y>600 and y <700:
                    if nivel<8:
                        nivel+=1
                        game=problems(nivel)
                        reset=deepcopy(game)
                        steps_done=0

                    else:
                        nivel=menu_level()
                        steps_done=0
                        if nivel==998:
                            return
                        game=problems(nivel)
                        reset=deepcopy(game)
                
                    
        else:  
            update(game,margem_x,margem_y,steps_done)
        
        keys_pressed=None
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed:
            pygame.time.wait(INTERVALO_TEMPO)

        if keys_pressed[pygame.K_ESCAPE]:
            solved=None
            nivel=menu_level()

            if nivel==998 or nivel==997:
                return
            game=problems(nivel)
            reset=deepcopy(game)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col=get_position(game,pos,margem_x,margem_y)
                
                if row<10 and col<10: #mover as peças
                    steps_done,solved=piece_chosen(game,row,col,steps_done,solved)

                elif row==10 and col==10: #reset no nivel
                    game=deepcopy(reset)
                    solved=None
                    steps_done=0
                
                elif row ==25 and col==25:#pedir para AI resolver
                    if not game.test_goal():
                        steps_done+=1
                    if not solved and not game.test_goal():
                        solved=AI_SOLVER(game)
                        del solved.move_history[0] #elimina do move history a board no estado em que foi pedida ajuda para avançar para o proximo step
                        board_temp=solved.move_history.pop(0)
                        game=Klostki(board_temp,dicionario(board_temp))
                    elif not game.test_goal():
                        board_temp=solved.move_history.pop(0)
                        game=Klostki(board_temp,dicionario(board_temp))
                        

    pygame.quit()

if __name__ == "__main__":
    main()
