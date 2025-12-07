from turtle import *

def drawBar(height):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(height)
    #draw one bar of the specified height
    #turtle will start where the last bar left off
    return

def readData():
    data_list = []
    file_name = input()
    string_data_list = file_name.readlines()
    
    for i in range(len(string_data_list)):
        data_list[i] = int(string_data_list[i])
    #read the data into myList
    #Use open() and readlines()
    #Convert each element into an int
    #One way to do it is to loop through and assign myList[i] = int(myList[i])

    return data_list

def main():
    print(readData())
    #get data list from readData()
    #print the list of data to the console window
 
    maxHeight = 0
    for myList[i] in range(len(myList)):
        if myList[i] >=maxHeight:
            maxHeight = myList[i]
        else:
            maxHeight = maxHeight
    numbars = len(myList)
    
    #find numbars

    screen = Screen()
    #screen.setworldcoordinates(?,?,?,?)
    screen.setworldcoordinates((40*numbars),(40*numbars), maxHeight, maxHeight)
    speed('fastest')
    for myList[i] in range(len(myList()):
        drawBar(myList[i])
    #draw a bar for each element in the data list
    print(myList.sort())
    #sort the list

    #print the sorted list to the console window
    
    reset()
    speed('fastest')
     for myList[i] in range(len(myList()):
        drawBar(myList[i])
    #draw a bar for each element in the data list (again)

    screen.exitonclick()

if __name__ == "__main__":
    main()




