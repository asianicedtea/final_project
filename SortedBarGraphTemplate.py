from turtle import *

def drawBar(height):
    forward(height)
    right(90)
    forward(40)
    right(90)
    forward(height)
    left(180)
    begin_fill()
    
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
    data_values = readData()
    for i in range(len(data_values)):
        print(data_values[i])
    #get data list from readData()
    #print the list of data to the console window
 
    maxheight = max(data_values)
    numBars = len(data_values)
    
    #find numbars

    screen = Screen()
    #screen.setworldcoordinates(?,?,?,?)
    screen.setworldcoordinates(0,0, (40*numBars), maxheight)
    speed('fastest')
    for i in range(numBars):
        drawBar(data_value[i])
    #draw a bar for each element in the data list
    
    #sort the list
    new_data = data_values.sort()
    for i in range(len(new_data)):
        print(new_data[i])

    #print the sorted list to the console window
    
    reset()
    speed('fastest')
    for i in range(numBars):
        drawBar(new_data[i])
    #draw a bar for each element in the data list (again)

    screen.exitonclick()

if __name__ == "__main__":
    main()








