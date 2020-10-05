a = [[" "," "," "], [" "," "," "], [" "," "," "]]

def how_to_play():
    print("This application is a console version of the BINGO! game.\n")

    print("to play this game you need two players.\n")
    
    print("Player 1 = X \n")
    
    print("Player 2 = O \n")
    
    print("to input your X or your 0 write the specific location on the 3x3 board \n")
    
    print("for example: middle left or top right.\n")

    print("remember! center is middle so middle center is middle middle")
    
# assigning variable

def top_Left(shape):
    if a[0][0] == " ":
        a[0][0] = shape
       
        
    
def top_Middle(shape):
    if a[0][1] == " ":
        a[0][1] = shape
       
        
    
def top_Right(shape):
    if a[0][2] == " ":
        a[0][2] = shape
        
        
   
def middle_Left(shape):
    if a[1][0] == " ":
        a[1][0] = shape
        
        

def middle_Middle(shape):
    if a[1][1] == " ":
        a[1][1] = shape
        
        

def middle_Right(shape):
    if a[1][2] == " ":
        a[1][2] = shape
      
        

def bottom_Left(shape):
    if a[2][0] == " ":
        a[2][0] = shape
        
       

def bottom_Middle(shape):
    if a[2][1] == " ":
        a[2][1] = shape
              

def bottom_Right(shape):
    if a[2][2] == " ":
        a[2][2] = shape
        
       


    

#identification 

def player_A():
    print("Player a's Turn.\n")

def player_B():
    print("Player b's Turn.\n")

def ask_For_Input():
    print("please input your location. write in this form ('top left')")


#main logic 

def main():
    if location == "top left":
        top_Left(shape) 

    elif location == "top middle":
        top_Middle(shape)

    elif location == "top right":
        top_Right(shape)
    
    elif location == "middle left":
        middle_Left(shape)
    
    elif location == "middle middle":
        middle_Middle(shape)
    
    elif location == "middle right":
        middle_Right(shape) 
    
    elif location == "bottom left":
        bottom_Left(shape) 

    elif location == "bottom middle":
        bottom_Middle(shape) 
  
    elif location == "bottom right":
        bottom_Right(shape) 
    
    else: 
        raise Exception("sorry, this is not a valid location")


#bingo checking

def top_Right_From_Top(shape_bingo):
    return a[0][0] == shape_bingo and a[0][1] == shape_bingo and a[0][2] == shape_bingo
    # to the right from top


def diagonal_To_Bottom_Right(shape_bingo):
    return a[0][0] == shape_bingo and a[1][1] == shape_bingo and a[2][2] == shape_bingo    
    # diagonal to bottom right


def bottom_Left_From_Top(shape_bingo):
    return a[0][0] == shape_bingo and a[1][0] == shape_bingo and a[2][0] == shape_bingo      
    # to the bottom left from top


def bottom_Middle_From_Mid_Top(shape_bingo):
    return a[0][1] == shape_bingo and a[1][1] == shape_bingo and a[2][1] == shape_bingo       
    # to the bottom middle from the middle top


def bottom_Right_From_Top_Right(shape_bingo):
    return a[0][2] == shape_bingo and a[1][2] == shape_bingo and a[2][2] == shape_bingo        
    # bottom right from top right


def middle_Left_From_Right(shape_bingo):
    return a[1][0] == shape_bingo and a[1][1] == shape_bingo and a[1][2] == shape_bingo       
    # middle left from middle right


def bottom_Left_To_Bottom_Right(shape_bingo):
    return a[2][0] == shape_bingo and a[2][1] == shape_bingo and a[2][2] == shape_bingo       
    # bottom left to bottom right


def bottom_Left_From_Top(shape_bingo):
    return a[2][0] == shape_bingo and a[1][1] == shape_bingo and a[0][2] == shape_bingo      
    # bottom left to top right

# printing bingo 

def checker():
    if top_Right_From_Top(shape_bingo):
        return True
        
    elif diagonal_To_Bottom_Right(shape_bingo):
        return True
        
    elif bottom_Left_From_Top(shape_bingo):
        return True
        
    elif bottom_Middle_From_Mid_Top(shape_bingo):
        return True
        

    elif bottom_Right_From_Top_Right(shape_bingo):
        return True
        

    elif middle_Left_From_Right(shape_bingo):
        return True
        
    
    elif bottom_Left_To_Bottom_Right(shape_bingo):
        return True
       

    elif bottom_Left_From_Top(shape_bingo):
        return True
       
        

def shape_A():
    global shape 
    shape = "x"

def shape_Bingo_A():
    global shape_bingo
    shape_bingo = "x"

def shape_B():
    global shape
    shape = "O"

def shape_Bingo_B():
    global shape_bingo
    shape_bingo = "O"

def Bingo_A():
    print("BINGO! Player A wins!")

def Bingo_B():
    print("BINGO! Player B wins!")

def Turn():
    return True

def player_turn(turn):
    if turn == True:
        shape_A()
        shape_Bingo_A()
    elif turn == False:
        shape_B()
        shape_Bingo_B()

def player(play):
    if play == True:
        return "a"
    elif play == False:
        return "b" 






bingo = False

play = True
turn = True

game_round = 1

how_to_play()

while bingo == False:
    print("\nplayer " + player(play) + " turn. please input your location")
    location = input()
    player_turn(turn)
    
    try:
        main()
        bingo_win = checker()
        print(a)
        if bingo_win == True:
            print("winner is" + " " + player(play))
            bingo = True
        elif game_round == 9:
            bingo = True
        elif turn == True:
            game_round += 1
            turn = False
            play = False
            print(game_round)
        elif turn == False:
            game_round += 1
            turn = True
            play = True
            print(game_round)
    except:
        print("please input another location")
