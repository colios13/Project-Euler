triangle = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

# First try i don't understand the probleme well and find a fast but an approximation solution
# as this problem is ofr sure :') not NP-hard we should find the exact solution
ans = 0
lastPosition = 0

for j, i in enumerate(triangle):
    memo = max(i[lastPosition:lastPosition+2])
    ans += memo
    lastPosition = triangle[j].index(memo)
    #print(max(i[lastPosition:lastPosition+1]), i[lastPosition:lastPosition+2], i, triangle[j].index(memo))

print(ans)

# Tried reversed array but lead not an non optimal solution because i go on the side of triangle
# and so have only one possibility to stay on the side of the triangle
'''ans = 0
lastPosition = 0
for j, i in enumerate(triangle[::-1]):
    if j == 0:
        memo = max(i)
    else:
        memo = max(i[lastPosition-1:lastPosition+1])
    print(j, memo, i[lastPosition-1:lastPosition+1])
    ans += memo
    lastPosition = triangle[::-1][j].index(memo)
    #print(max(i[lastPosition:lastPosition+1]), i[lastPosition:lastPosition+2], i, triangle[j].index(memo))

print(ans)'''

# Decided to find a dynamic programming approach
# And thinked about to find all the path (brute-force) but with memoization
# like a clever brute force ^^

# Was working on the way to do the brute force and how to store path re-use them...
# many things, interesting problem i think about brute-force and dynamic programming

visitedPath = [[0 for j in i] for i in triangle]
sumPath = []

currSumPath = 0
# first path
for i, level in enumerate(triangle):
    n = 0
    currSumPath += level[n]
    visitedPath[i][n] = 1

sumPath.append(currSumPath)

while not all(visitedPath):
    #do the brute force
    # think about visited path are not only 1 but are maxLevel - currLevel
    # easier way to manage the brute force part but less faster need to rewrite 
    # an equivalent function to all 