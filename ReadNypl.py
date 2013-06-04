import argparse

def read_nypl():
    f = open('nypl', 'r')
    g = open('copy', 'r+')
    i = 0;
    temp_str = ""
    for line in f:
        temp_str = line
        g.write(temp_str)
        i += 1
        print i
    print "The deed is done"

def print_titles():
    f = open('copy', 'r')
    g = open('titles', 'w')
    i = 0;
    titles = ""
    while f.read(1) != "":
        f.seek(i)
        if f.read(5) == 'title':
            #print "wooop"
            j = i+6
            while (f.read(1)!= ',')and(f.read(4)!='nfo"')and(f.read(10)!=':"Lawrence')and(f.read(10)!=" 'Laurie a"):
                f.seek(j)
                titles += f.read(1)
                j += 1
            titles += '\n'
        i += 1;
    g.write(titles)


if __name__ == "__main__":
    read_nypl()
    print_titles()
