import os

def main():

    data = os.popen('ps arxc -o pid -o %cpu -o %mem -o command').read().split("\n")
    outfile = open('processes.csv', 'w')
    
    for i in range(len(data)-1):
        line = data[i].split(sep=None, maxsplit=3)
        outfile.write(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "\n")
        
    outfile.close()

if __name__ == "__main__":
    exit(main())