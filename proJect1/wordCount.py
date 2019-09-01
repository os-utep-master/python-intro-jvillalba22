#Jennifer Villalba 08/31/20119
#Project 1 Operating of Systems
import re

def main():
    #open file and edit to get all to lowercase
    file = open('testEx.txt', 'r')

    lines = [line.lower() for line in file]
    with open('testEx.txt', 'w') as out:
        out.writelines(lines)
    #create the new file and create the list
    with open("testEx.txt", "r") as f:
        words = f.read().split()

    #get rid of special characters
    u = 0
    for i in words:
        i = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", i)
        words[u] = i #make sute list gets copy withot the puctuation
        u = u + 1
     #count how make words (list to dictionary
    dict = {i: words.count(i) for i in words}


    #create new file
    f = open("list1.txt", "w")
    for i in sorted(dict):
        f.write("%s" % re.escape(i)) #write word on file
        #write the value of how many times does the word repeats
        x = dict[i]
        f.write(" %d\n" %x)
    f.close()

if __name__ == '__main__':
    main()
