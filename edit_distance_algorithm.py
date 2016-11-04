#Charlotte List
#Edit Distance Implementation
#October 16, 2016

def find_cost(a, b, vc, cc):
#if same there is no cost
    alpha = 0 
    if a == b:
        alpha = 0
    #check if vowels or constants
    elif a in ["a","e","i","o","u"]:
        if b in ["a","e","i","o","u"]:
            alpha = cc
        elif b not in ["a","e","i","o","u"]:
            alpha = vc
    elif a not in ["a","e","i","o","u"]:
        if b in ["a","e","i","o","u"]:
            alpha = vc
        elif b not in ["a","e","i","o","u"]:
            alpha = cc
    return alpha

def calculate_distance(x, y, d, vc, cc):
    #x, y are the two strings
    #d is the delta, cost of insert or delete
    #vv, cc, and vc are the alpha, cost of substitution
    rows = len(x)+1
    cols = len(y)+1
    
    #create two dimensional array of size row by cols
    array = [[0 for i in range(cols)] for i in range(rows)]

    #base cases, when one string is empty
    for row in range(1, rows):
        array[row][0]=row*d

    for col in range(1, cols):
        array[0][col]=col*d
    
    #now need to fill the array
    for col in range(1, cols):
        for row in range(1, rows):
            #need to find out what the alpha cost is
            #index in to get the letters
            a = x[row-1]
            b = y[col-1]
            alpha = find_cost(a, b, vc, cc)
            #recurrence 
            array[row][col]=min(array[row-1][col] + d,
                                array[row][col-1] + d,
                                array[row-1][col-1] + alpha)            

    #traceback to get the sequence of edits
    i=row
    j=col
    #list to hold the sequence of edits
    trace = []
    trace.append((i, j))
    while i>0 and j>0:

    #NEED TO CHECK IF THE BOX ABOVE PLUS DELTA OR ALPHA IS THE SMALLEST
        if ((array[i-1][j-1]+find_cost(x[i-1], y[j-1], vc, cc))<= array[i-1][j]+d) and ((array[i-1][j]+d) <= (array[i][j-1]+d)): 
            #substitution
            trace.append((i-1, j-1))
            i=i-1
            j=j-1
            
        elif ((array[i-1][j-1]+find_cost(x[i-1], y[j-1],vc, cc)) <= (array[i][j-1]+d)) and ((array[i][j-1]+d) <= (array[i-1][j]+d )):
            #substitution
            trace.append((i-1, j-1))
            i=i-1
            j=j-1
            
        elif ((array[i-1][j]+d) <= (array[i][j-1]+d)) and ((array[i-1][j]+d) < (array[i-1][j-1]+find_cost(x[i-1], y[j-1],vc, cc))):
            #deletion
            trace.append((i-1, j))
            i=i-1
            
        elif ((array[i][j-1]+d) < (array[i-1][j]+d)) and ((array[i][j-1]+d) < (array[i-1][j-1]+find_cost(x[i-1], y[j-1],vc, cc))):
            #insertion
            trace.append((i, j-1))
            j=j-1

    while i>0:
        i=i-1
        trace.append((i,0))
        
    while j>0:
        j=j-1
        trace.append((0, j))

    trace.reverse()
    #print output
    string = "Start!\t\t\t\t"+x
    xIn = 0
    yIn = 0
    overX = False
    for w in range(len(trace)):       
        if xIn > len(x)-1:
            xIn=len(x)-1
            overX = True
        if yIn > len(y)-1:
            yIn=len(y)-1
            overY=True
        if w != len(trace)-1:
            string=string+"\n"
            m = trace[w]
            n=trace[w+1]
            if n[0]-m[0] == 1 and n[1]-m[1]==1:
                #substitution or ignore
                if x[xIn] == y[yIn]:
                    string += "Ignore "+x[xIn]+"\t\t\t"
                    string += x
                    xIn += 1
                    yIn += 1
                else:
                    string += "Change "+ x[xIn]+" to "+ y[yIn]+ "\t\t\t"
                    x = x[:xIn]+y[yIn]+x[xIn+1:]
                    string += x
                    xIn += 1
                    yIn += 1
                    
            elif n[0]-m[0] == 1 and n[1]-m[1]==0:
                #deletion
                string = string + "Delete "+x[xIn]+"\t\t\t"
                if xIn == 0:
                    x = x[xIn+1:]
                    string += x
                elif xIn == len(x)-1:
                    x = x[:xIn]
                    string += x
                else:
                    x = x[:xIn]+x[xIn+1:]
                    string+=x
                
            elif n[0]-m[0] == 0 and n[1]-m[1]==1:
                #insertion
                string = string + "Insert "+y[yIn]+"\t\t\t"
                if xIn == 0:
                    x = y[yIn]+x
                    string = string+x
                elif xIn == len(x)-1 and overX == True:
                    x = x[:xIn+1]+ y[yIn] + x[xIn+1:]
                    string += x
                else:
                    x = x[:xIn]+ y[yIn] + x[xIn:]
                    string += x
                yIn += 1
                xIn +=1


    return string, array[row][col]

#take in information from the input file and return edit distance
def edit_dist(strings, costs):
    words= strings.split()
    x = words[0]
    y = words[1]
    values = costs.split()
    d = int(costs[0])
    vc = int(costs[2])
    cc = int(costs[4])
    string, val = calculate_distance(x, y, d, vc, cc)
    sol = "\n"+x+" "+y+"\n"+str(d)+" "+str(vc)+ " "+str(cc)+ "\n"+string+ "\nEdit Distance: "+str(val)+"\n"
    sol = sol+ "\n---------------------------------------\n"
    return sol

#main function
#reads from input.txt and writes to outputfile.txt
def program(txt):
    inputfile = open(txt, "r")
    data = inputfile.readlines()
    outputfile = open("outputfile.txt", "w")
    for i in range(len(data)):
        if data[i] == "\n":
            outputfile.write( edit_dist(data[i+1], data[i+2]))

#calling function here
program("input.txt")

