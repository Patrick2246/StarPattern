def patternStar():
  #top triangle
  space=5
  for rows in range(1,6):
    for count in range(1,space):
      print(" ", end="")
    for star in range(1,rows+1):
      print("*", end=" ")
    print()
    space-=1
  #down triangle
  space=2
  for rows in range(4,0,-1):
    for count in range(1,space):
      print(" ", end="")
    for star in range(1,rows+1):
      print("*", end=" ")
    print()
    space+=1

patternStar()
