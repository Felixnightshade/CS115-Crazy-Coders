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
    """
    Call loadDatabase and assign it to a variable
    Ask the user for a name, assign it to a variable, and handle it according to the directions.
    While True:
        Print EXACTLY…
        Enter a letter to choose an option:
        e - Enter preferences
        r - Get recommendations
        p - Show most popular artists
        h - How popular is the most popular
        m - Which user has the most likes
        q - Save and quit

        On “e” call enterPreferences and assign the result to the dict element corresponding to the current user. Ie. database[username] = enterPreferences
        On “r” call recommendations and print the results
        On “p” call popular and print the results
        On “h” call highestPopularity and print the result
        On “m” call mostLikesUser and print the result
        On “q” call saveDatabase then break
    """


def loadDatabase(filename: str = "musicrecplus.txt") -> dict:
    """
    Takes in file name to read database from.
    Returns dict with format {UserName: (Artist1, Artist2, Artist3)}
    """
    # TODO Implement loadDatabase
    pass


def enterPreferences(username: str):
    """
    Takes in username.
    Returns ???
    """
    # TODO Plan enterPreferences
    # TODO Implement enterPreferences
    pass


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
