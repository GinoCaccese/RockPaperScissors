import tkinter as tk
import sys
import time

root = tk.Tk()


#all of the photos
rock_image = tk.PhotoImage(file = 'Rock.png')
paper_image = tk.PhotoImage(file = 'Paper.png')
scissors_image = tk.PhotoImage(file = 'Scissors.png')
background_image = tk.PhotoImage(file = 'cover.png')
frame_image = tk.PhotoImage(file = 'cover2.png' )

images = {1:rock_image, 2:paper_image, 3:scissors_image}

canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack()

back_image = tk.Label(root, image = background_image)
back_image.place(relwidth = 1, relheight = 1)

p1 = 0
p2 = 0
#frame1, label_p1, button_r_p1, button_p_p1, and button_s_p1 are all for player one. 
#I could have made a for loop or a while loop but i guess somewhere in my head i decided
#that would be too easy so now im making all of this x2 for player 2's turn.
def player_1():
    frame1 = tk.Label(root, image = frame_image)
    frame1.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

    label_p1 = tk.Label(frame1, text ='Player 1', fg = '#FF0000', bg = '#FFFFFF', font = ('',50), anchor = 'n')
    label_p1.pack()

    button_r_p1 = tk.Button(frame1, image = rock_image, command = lambda: (chosen_p1(1,0,0), player_2()) )
    button_r_p1.place(x=10, y = 160)

    button_p_p1 = tk.Button(frame1, image = paper_image, command = lambda: (chosen_p1(0,1,0), player_2()) )
    button_p_p1.place(x= 150, y = 160)

    button_s_p1 = tk.Button(frame1,image = scissors_image, command = lambda: (chosen_p1(0,0,1), player_2()) )
    button_s_p1.place(x= 290, y = 160)

#Player 2's stuff. Dont ask why i am doing it this way because to be honest, i have absolutely no reason
#make a button for rock, paper, and scissors for player 1 as well as player 2
def player_2():
    frame2 = tk.Label(root, image = frame_image)
    frame2.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

    label_p2 = tk.Label(frame2, text ='Player 2', fg = '#0000FF', bg = '#FFFFFF', font = ('',50), anchor = 'n')
    label_p2.pack()

    button_r_p2 = tk.Button(frame2, image = rock_image, command = lambda: chosen_p2(1,0,0) )
    button_r_p2.place(x=10, y = 160)

    button_p_p2 = tk.Button(frame2, image = paper_image, command = lambda: chosen_p2(0,1,0) )
    button_p_p2.place(x= 150, y = 160)

    button_s_p2 = tk.Button(frame2,image = scissors_image, command = lambda: chosen_p2(0,0,1) )
    button_s_p2.place(x= 290, y = 160)
    
def end(a, b):
    #a is representing player 1, and b is representing player 2.

    if a == 1 and b == 1:
        #this part is a draw
        
        #this label is for making a new frame within the canvas
        frame3 = tk.Label(root, image = frame_image)
        frame3.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)
        
        #this label if for showing the players choice
        label_p1_1 = tk.Label(frame3, image = images[p1], bg ='#FFFFFF')
        label_p1_1.place(x=60, y=160)

        #this label is for showing the player with their choice above them
        label_p1_1 = tk.Label(frame3, text = 'Player 1', bg = '#FFFFFF', font = ('',20))
        label_p1_1.place(x = 55, y = 270)

        #this label is for showing the players choice
        label_p2_1 = tk.Label(frame3, image = images[p2], bg = '#FFFFFF')
        label_p2_1.place(x=240, y = 160)

        #this label is for showing the players name with their choice above them
        label_p2_2 = tk.Label(frame3, text = 'Player 2', bg = '#FFFFFF', font = ('',20))
        label_p2_2.place(x=245, y = 270)
        
        #this label is for showing that the end result of the game is a draw
        label3 = tk.Label(frame3, text = 'Draw!', fg = '#000000', bg = '#FFFFFF', font= ('',50) )
        label3.pack()
        
        exit_button = tk.Button(frame3, text = 'EXIT', anchor = 'ne', command = lambda: sys.exit())
        exit_button.pack()

        play_again = tk.Button(frame3, text = 'Play Again', command = lambda: player_1())
        play_again.place(x = 165, y = 350)


    elif a == 1 and b == 0:
        #this part is player 1 wins
        
        #this label is for making a new frame within the canvas
        frame3 = tk.Label(root, image = frame_image)
        frame3.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

        #this label is for show the player choice
        label_p1_1 = tk.Label(frame3, image = images[p1], bg ='#FFFFFF')
        label_p1_1.place(x=60, y=160)

        #this label is for showing the player and their choice above
        label_p1_1 = tk.Label(frame3, text = 'Player 1', bg = '#FFFFFF', font = ('',20))
        label_p1_1.place(x = 55, y = 270)

        #this label is to show the players choice 
        label_p2_1 = tk.Label(frame3, image = images[p2], bg = '#FFFFFF')
        label_p2_1.place(x=240, y = 160)

        #this label is for showing the players name with their choice above them
        label_p2_2 = tk.Label(frame3, text = 'Player 2', bg = '#FFFFFF', font = ('',20))
        label_p2_2.place(x=245, y = 270)
        
        #this label is for displaying the winner 
        label3 = tk.Label(frame3, text = 'Player 1 Wins!', fg = '#FF0000', bg = '#FFFFFF', font= ('',40), anchor = 'center')
        label3.pack()

        #this button allows the player to exit the program if they would like
        exit_button = tk.Button(frame3, text = 'EXIT', anchor = 'ne', command = lambda: sys.exit())
        exit_button.pack()

        #this button allows the player to play again if they would like
        play_again = tk.Button(frame3, text = 'Play Again', command = lambda: player_1())
        play_again.place(x = 165, y = 350)

    elif a == 0 and b == 1:
        #this part is player 2 wins
       
        #this label makes a new frame 
        frame3 = tk.Label(root, image = frame_image)
        frame3.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

        #this label show the players choice
        label_p1_1 = tk.Label(frame3, image = images[p1], bg ='#FFFFFF')
        label_p1_1.place(x=60, y=160)

        #this label shows the player and their choice above them
        label_p1_1 = tk.Label(frame3, text = 'Player 1', bg = '#FFFFFF', font = ('',20))
        label_p1_1.place(x = 55, y = 270)

        #this label shows the players choice
        label_p2_1 = tk.Label(frame3, image = images[p2], bg = '#FFFFFF')
        label_p2_1.place(x=240, y = 160)

        #this label shows the player with their choice above
        label_p2_2 = tk.Label(frame3, text = 'Player 2', bg = '#FFFFFF', font = ('',20))
        label_p2_2.place(x=245, y = 270)
        
        #this label is shows the winner
        label3 = tk.Label(frame3, text = 'Player 2 Wins!', fg = '#0000FF', bg = '#FFFFFF', font= ('',40), anchor = 'center')
        label3.pack()

        #the exit button variable sets a button for the player if they want to leave
        exit_button = tk.Button(frame3, text = 'EXIT', anchor = 'ne', command = lambda: sys.exit())
        exit_button.pack()

        #the play again button allows the player to play again if they would like
        play_again = tk.Button(frame3, text = 'Play Again', command = lambda: player_1())
        play_again.place(x = 165, y = 350)



#rock beats scissors 
#paper beats rock 
#scissors beats paper

#All this function does is gets the input from player 1 and player 2.
#p1 and p2 are currently defined as integer inputs but will later be turned
#into numbers through a button function with tkinter
'''
def get_in():
    global p1, p2
    p1 = int(input('Player 1: Pick Rock(1), Paper(2), or Scissors(3): '))
    p2 = int(input('Player 2: Pick Rock(1), Paper(2), or Scissors(3): '))
'''
#This function goes through 9 if statements and they basically decide
#if player 1 wins, if player 2 wins, or if there is a draw
#the function will then return a string which will be outputted at the top
#throught the text function in a label. This will happen at the end as well
#as the middle of the game
def decide():
    global p1, p2
    #decide each of the players choices and decided whether there is a winner or a draw
    #use a lot of if statements
    if p1 == p2:
        end(1,1)
    #rock wins
    elif p1 == 1 and p2 == 3:
        end(1,0)
    elif p2 == 1 and p1 == 3:
        end(0,1)

    #paper wins
    elif p1 == 2 and p2 == 1:
        end(1,0)
    elif p2 == 2 and p1 == 1:
        end(0,1)

    #scissors win
    elif p1 == 3 and p2 == 2:
        end(1,0)
    elif p2 == 3 and p1 == 2:
        end(0,1)

#this function changes the players inputs from integers to strings
#this will tie into the GUI when it is all over, because on the end screen it
#will display the players choosings. I will use p1 and p2 and turn them into 
#the text in a label since they are now strings after calling this function
'''
def p_output():
    global p1, p2
    #Changing the Player 1's choosings to strings from integers
    if p1 == 1:
        p1 = 'Rock'
    elif p1 == 2:
        p1 = 'Paper'
    elif p1 == 3:
        p1 = 'Scissors'
    #Changing the Player 2's choosings to strings from integers
    if p2 == 1:
        p2 = 'Rock'
    elif p2 == 2:
        p2 = 'Paper'
    elif p2 == 3:
        p2 = 'Scissors'
'''

#changes the button they pressed into a number corresponding to rock paper or scissors
def chosen_p1(r, p, s):
    global p1
    if r == 1:
        p1 = 1
    elif p == 1:
        p1 = 2
    elif s == 1:
        p1 = 3
    

#changes the button they pressed into a number corresponding to rock paper or scissors
def chosen_p2(r, p, s):
    global p2
    if r == 1:
        p2 = 1
    elif p == 1:
        p2 = 2
    elif s == 1:
        p2 = 3
    
    decide()
#   get_in()

#   p_output()
player_1()
root.mainloop()