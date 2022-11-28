"""
Created on 11/27/22
@author:   Samuel Friedman
@author:   Gabriel Talbert Bunt
@author:   Collin Smith
@author:   Marcus Hom
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Group Project
Team: Crazy Coders
"""


def main():
    '''Where the main loop is run - Marcus'''

    userDict = loadDataBase('musicrecplus_ex1.txt')
    
    while True:
        option = input('Enter a letter to choose an option:' + '\n' + '\t' + 'e - enter preferences' + '\n' + '\t' 'r - get recommendations' + '\n' + '\t' \
           + 'p - show most popular artists'  + '\n' + '\t' + 'h - how popular is the most popular' + \
           '\n' + '\t' + 'm - which user has the most likes ' + '\n' + '\t' + 'q - save and quit')

        if option == 'e':
            pass
        if option =='r':
            pass
            
        if option == 'p':
           pass
        
        if option == 'h':
            pass
            
        if option == 'm':
            pass
            
        if option == 'q':
            return None
        
        if option not in ['e', 'r', 'p', 'h', 'm', 'q']:
            print("That is not an option.")


def loadDataBase(filename):
    '''loads the database from the file named musicrecplus.txt,
    if it exists. Otherwise it creates the file. Checks if user is
    in the database, if not it adds to database along with their preferences- Marcus'''
    myfile = open(filename, "r")
    database = {}
    name = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n')
    for x in myfile:
        [userName, artists] = x.strip().split(':')
        #seperates contents of file into userName list and artists list
        artistList = artists.split(',')
        #creates an artistList of each artist that are seperated by commas
        artistList.sort()
        database[userName] = artistList
        #assigns username as key and artistlist as value in the database dictionary
    myfile.close()
    aList=[]
    if name not in database:
        #if the user is not already in the database, it asks for their preferences
        while True:
            artist = input('Enter an artist that you like (Enter to finish): \n')
            if artist != '':
                aList.append(artist.title())
            else:
                break
        aList.sort()
        database[name]=aList
        #adds the new user and their preferences to dictionary
    return database


def recommendations(username: str, database: dict) -> tuple:
    """
    Takes in username and database dict.
    Returns a tuple of artist names.
    """
    # TODO Implement recommendations
    pass


def popularity(artist: str, database: dict) -> int:
    """
    Takes in an artist name and database dict.
    Returns the number of users that liked the artist.
    """
    # TODO Implement popularity
    pass


def popular(database: dict) -> tuple:
    """
    Takes in a database dict.
    Returns a tuple of the top 3 most liked artists.
    """
    # TODO Implement popular
    pass


def highestPopularity(database: dict) -> int:
    """
    Takes in a database dict.
    Returns the popularity of the artist with the most likes.
    """
    # TODO Implement highestPopularity
    pass


def mostLikesUser(database: dict) -> str:
    """
    Takes in a database dict.
    Returns the name of the user that has liked the most artists.
    """
    # TODO Implment mostLikesUser
    pass


def saveDatabase(database: dict, filename: str) -> None:
    """
    Takes in a database dict and file name.
    Saves the database dict to the file according to the spec.
    """
    # TODO Implement saveDatabase
    pass


"""
DATABASE SPEC

Each user is on their own line
Format is “UserName:Artist1,Artist2,Artist3, . . .”
Because we load the entire database every run, 
overwrite the existing database instead of appending when saving.
"""

if __name__ == "__main__":
    main()
