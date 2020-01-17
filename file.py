'''
    Andres Schuchert
    CS 5001
    December 2, 2018
'''
def is_empty(users):
    '''
    Function name: is_empty
    Parameters: list
    Return: boolean
    Description: Return true if a list of users is empty or false otherwise
    '''
    if len(users) == 0:
        return True
    else:
        return False

def read_users(filename):
    '''
    Function name: read_users
    Parameters: string
    Return: list
    Description: Read a file and return a list of usernames and scores
    '''
    try:
        infile = open(filename,"r")
        users = infile.readlines()
        user_list = []
        for i in range(len(users)):
            users[i] = users[i].replace("\n","")
            index = users[i].rfind(" ")
            user = users[i][:index]
            score = users[i][index+1:]
            user_list.append([user,score])
        return user_list
    except OSError:
        return []

def add_user(filename, name, score):
    '''
    Function name: add_user
    Parameters: string, string, int
    Return: none
    Description: Write a username and score to the end of the file
    '''
    try:
        outfile = open(filename, "a")
        outfile.write(name + " " + str(score) + "\n")
        outfile.close()
    except OSError:
        print("Error: writing file.")
        return 

def add_users(filename, users):
    '''
    Function name: add_users
    Parameters: string, lst
    Return: none
    Description: Overwrite file and rewrite all usernames and scores to file
    '''
    try:
        outfile = open(filename,"w")
        for i in range(len(users)):
            outfile.write(users[i][0] + " " + str(users[i][1]) + "\n")
        outfile.close()
    except OSError:
        print("Error: Cannot write to file.")
        return 

def determine_highscore(filename, users, username, score):
    '''
    Function name: determine_highscore
    Parameters: string, list, string, int
    Return: none
    Description: If the score is higher than the score listed at top of the
    file then write the new username with the high score at top, otherwise
    add the user and score to the bottom
    '''
    if score > int(users[0][1]):
        user = [username,score]
        users.insert(0,user)
        add_users(filename,users)
    else:
        add_user(filename,username, score)
    
