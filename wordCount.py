#Jennifer Villalba
import re
import sys

def main():
    #ask input manually
    #prompt = input("Enter file name: \n")

    #run the code with inputfile and output from terminal
    prompt = sys.argv[1]
    outFile = sys.argv[2]


    #not change original
    import shutil
    shutil.copy(prompt, "prompt.txt")

    file = open('prompt.txt', 'r')
    #change all to lower case letters no have A = a
    lines = [line.lower() for line in file]
    with open('prompt.txt', 'w') as out:
        out.writelines(lines)

    with open('prompt.txt', "r") as f:
        words = f.read().split()

    #get rid of special characters
    u = 0
    for i in words:
        i = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", i)
        words[u] = i
        u = u + 1
     #count how words that repeat and make it the value of the word
    dict = {i: words.count(i) for i in words}

  # print(dict)
    f = open(outFile, "w")
    for i in sorted(dict):
        f.write("%s" % re.escape(i))
        x = dict[i]
        f.write(" %d\n" %x)
    f.close()

    print("Done!!")

if __name__ == '__main__':
    main()
