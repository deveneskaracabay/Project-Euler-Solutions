# Problem 22
# Names scores
# Using names.txt, 
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
import urllib.request
url = "https://projecteuler.net/project/resources/p022_names.txt"
file = urllib.request.urlopen(url)
data22 = file.readlines()[0].decode("utf-8")
data22 = data22.strip("\n").strip().split(",")
for index in range(len(data22)):
    data22[index] = data22[index].strip('"')
print("get data with urllib.request")
chars = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8,'I':9, 'J':10, 
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 
        'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
def problem22(data):
    data = sorted(data)
    totalProduct = 0
    i = 0
    while i<len(data):
        product = 0
        for l in data[i]:
            product += chars[l]
        product *= (i+1)
        totalProduct += product
        i+=1
    return totalProduct
print("result : ",problem22(data22))
# answer = 871198282
