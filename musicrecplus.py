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
    """Where the main loop is run -Marcus"""

    userDict = loadDataBase("musicrecplus_ex2_a.txt")

    while True:
        option = input(
            """
            Enter a letter to choose an option:\n
            \te - Enter preferences\n
            \tr - Get recommendations\n
            \tp - Show most popular artists\n
            \th - How popular is the most popular\n
            \tm - Which user has the most likes\n
            \tq - Save and quit\n
            """
        )

        if option == "e":
            pass
        elif option == "r":
            pass
        elif option == "p":
            print(mostPopular(userDict))
        elif option == "h":
            print(howPopular(userDict))
        elif option == "m":
            pass
        elif option == "q":
            return
        else:
            print("That is not an option.")


def loadDataBase(filename):
    """loads the database from the file named musicrecplus.txt,
    if it exists. Otherwise it creates the file. Checks if user is
    in the database, if not it adds to database along with their preferences- Marcus"""
    myfile = open(filename, "r")
    database = {}
    name = input(
        "Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n"
    )
    for x in myfile:
        [userName, artists] = x.strip().split(":")
        # seperates contents of file into userName list and artists list
        artistList = artists.split(",")
        # creates an artistList of each artist that are seperated by commas
        artistList.sort()
        database[userName] = artistList
        # assigns username as key and artistlist as value in the database dictionary
    myfile.close()
    aList = []
    if name not in database:
        # if the user is not already in the database, it asks for their preferences
        while True:
            artist = input("Enter an artist that you like (Enter to finish): \n")
            if artist != "":
                aList.append(artist.title())
            else:
                break
        aList.sort()
        database[name] = aList
        # adds the new user and their preferences to dictionary
    return database


def recommendations(username: str, database: dict) -> tuple:
    """
    Takes in username and database dict.
    Returns a tuple of artist names.
    """
    # TODO Implement recommendations
    pass


def mostPopularHelper(userDict):
    """returns the artist that occurs in users preferences the most. Is a helper for
    most popular function -Marcus"""
    artistPopularity = {}
    for x in userDict:
        if x[-1] != "$":
            # excludes users who are private
            for i in userDict[x]:
                if i not in artistPopularity:
                    artistPopularity[i] = 1
                    # if artist is not in the dictionary, it adds one instance to the new dictionary
                else:
                    artistPopularity[i] += 1
                    # if artist is already in dictionary, value of 1 is added to the artist count
    return sorted(artistPopularity.items(), key=lambda x: x[1], reverse=True)
    # returns a list sorted by value from greatest to least, so most popular artist will be at index 0, least will be at the end


def mostPopular(userDict):
    """returns the top 3 artists that appear in users preferences. -Marcus"""
    mostPop = mostPopularHelper(userDict)[:3]
    a = ""
    # takes the top 3 most popular artists
    for x in mostPop:
        if x == "":
            a = "Sorry, no artists found"
        a += str(x[0]) + "\n"
    return a


def howPopular(userDict):
    """returns how popular the most popular artist is. -Marcus"""
    x = mostPopularHelper(userDict)[0]
    a = ""
    if x == "":
        a = "Sorry, no artists found"
    a = str(x[1])
    return a


def enterPreferences():
    """guides user to enter their preferences"""


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
