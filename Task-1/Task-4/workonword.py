# Task 1-4

Name_list = []

# dynamic programming algorithm

def min_distance(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    row , col  = len(word1) , len(word2)
    dp = [[0] * (col+1) for _ in range(row+1)] # create 2D list of 0 (we can create this with np.zeros())

    for i in range(row + 1): # placement
        dp[i][0] = i
    for j in range(col + 1): # placement
        dp[0][j] = j
    for i in range(1, row + 1):
        for j in range(1, col + 1):

            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:                  #replace         # insert      #delete
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    if dp[row][col] == 1 :
        Name_list.append(word1.rstrip('\n')+" , "+word2.rstrip('\n'))

    return dp[row][col]

# read file from below url:

url = "words_input.txt"
file = open(url, "r")
Lst = []
line1 = file.readline()

# read data and send couple word to min_distance method
while line1:
    line2 = file.readline()
    dis = min_distance(line1,line2)
    Lst.append(dis)
    line1 = line2

file.close # close file after operations

Lst = Lst[:-1]

print("List of Distances : ",Lst)
print("Count of words have distance 1 : ",Lst.count(1))
print("Count of words have distance 2 : ",Lst.count(2))
print("Count of words have distance 3 : ",Lst.count(3))
print("List of couple name have distance 1 : ",Name_list)
