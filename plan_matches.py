import sys

with open(sys.argv[1]) as f:
    data = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [i for i in line]
            data.append(line)
result=[]

while(len(data)>0):

    #Append each result entry with the first combination from data
    res=[list(data[0])]

    #Remove the entry from data after we have used it
    data.remove(res[0])

    #Append the result entry with unique combinations until we cannot find one
    for l in data:

      #Check whether the combination already exists in result
        if len(set(l) & set().union(*res))==0:
            #if the combination is not already present in res, add it to res
            #and remove it from data
            res.append(l)
            data.remove(l)

    #The repetition a.k.a day is over, so add whatever we have found to a new entry (day) in result
    result.append(res)
i=0

#and sort pairs internally using sorted()
sortedResult=[]
for l in result:
  for j in l:
   sortedResult.append([sorted(j),i])
  i+=1

#Perform nested list sorting in sortedResult, to assure that results will appear
#in perfect alphabetical ordering
sortedResult.sort(key=lambda e: (e[0][0],e[0][1]))

#Print the list by removing brackets []
for s in sortedResult:
  print("("+", ".join(map(str, s[0])) + ") " + str(s[1]))
