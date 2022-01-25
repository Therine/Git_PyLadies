#https://pyladiesvienna.pythonanywhere.com/

#Creates a 10x10 table with nest tuples [['.','.','.'],['.','.','.'],['.','.','.']]
#So essentially a matrix
def draw_map():
   print([['.','.','.'],['.','.','.'],['.','.','.']])

draw_map()

for x in range(10):
    for y in range(10):
        print('.', end=" ")
        if (x,y) in [(0,0),]:
            print('x', end=" ")
        else:
            print('.', end=" ")