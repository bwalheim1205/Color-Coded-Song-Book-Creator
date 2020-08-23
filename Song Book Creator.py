#-----------------------------
# Song Book Creator
#     Converts formatted txt file into pdf easy read
#        sheet music
# Version: 1.0.0
# Creator: Brian Walheim
#-----------------------------

#-----------------------------
# Imports
#-----------------------------

#Python image library
from PIL import Image, ImageDraw, ImageFont

#-----------------------------
# Variables
#-----------------------------

#RGB Colors

blue = (20,20,255) #Note: C
pink = (255, 114, 152) #Note: C#
brown = (137, 61, 17) #Note: D
lightGreen = (172, 252, 60) #Note: D#
orange = (255, 133, 20) #Note: E
teal = (45, 252, 131) #Note: F
yellow = (255, 235, 15) #Note: F#
purple = (236, 116, 252) #Note: G
black = (0,0,0) #Note: G#
green = (0,100,0) #Note: A
babyBlue = (179, 251, 252) #Note: A#
red = (255,20,20) #Note: B

#Color to note map
colorNote = {"C": blue, "C#": pink, "D" : brown, "D#" : lightGreen, "E" : orange, "F" : teal, "F#" : yellow, "G" : purple, "G#" : black, "A" : green, "A#" : babyBlue, "B" : red}

#Note Config___________________________________

size = 75

horizontalSpacing = 40
verticalSpacing = 50
headerSpace = 70

resolution = (510, 700)

notesPerRow = int((resolution[0]-horizontalSpacing)/(size+horizontalSpacing))
numberOfRows = int((resolution[1]-headerSpace)/(size+verticalSpacing))


#Image Variables_______________________________

#2550,3300
img = Image.new('RGB', resolution, color = (255, 255, 255)) 
draw = ImageDraw.Draw(img)



#--------------------
#Functions
#--------------------

#Draw Function
def drawNote(x,y,note,color, phrase = ""):

  #Draws Note
  draw.ellipse((x,y,x+size,y+size), fill = color, outline = 'black', width = 1)
  draw.text((x+size/2-2,y+size/2-5), note, fill = "black")

  #Draws Phrase Paired With Note
  draw.text((x+size/2-len(phrase)*3, y+size+10), phrase, fill = "black")

#----------------
# Main
#----------------

#Reads formatted text file
musicFile = open("song.txt", "r")
title = musicFile.readline()[7:]
#print(title)
musicArray = musicFile.read().split("\n")
print(musicArray)
musicFile.close()

count = 0
images = []

draw.text((10, 10), "#1", fill = "black")
draw.text((int(resolution[0]/2 - (len(title)-7)*3),10), title, fill = "black")

for line in musicArray:
  if(count%(numberOfRows*notesPerRow)==0 and count != 0):
    images.append(img)
    img = Image.new('RGB', resolution, color = (255, 255, 255)) 
    draw = ImageDraw.Draw(img)

    #Draw Headers
    draw.text((10, 10), "#" + str(1 + int(count/(numberOfRows*notesPerRow))), fill = "black")
    draw.text((int(resolution[0]/2 - (len(title)-7)*3),10), title, fill = "black")


  if line != '' and line != "\n":
    note = line.split()[0]
    word = ""
    if len(line.split()) > 1 and line.split()[1] != "\n":

      for i in range(1, len(line.split())):
        word += line.split()[i] + " "
      print(word)
   
    drawNote(horizontalSpacing+(horizontalSpacing+size)*(count%notesPerRow), headerSpace + (verticalSpacing+size)*int((count%(numberOfRows*notesPerRow))/notesPerRow), note, colorNote[note], phrase = word)

    count+=1

images.append(img)

images[0].save(title+'.pdf', save_all = True, append_images = images[1:])

print("Saved")