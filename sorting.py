import os


def my_mean(values,n):
	return sum(values)/n

def print_list(l):
	for i in range(len(l)):
		print(l[i][0] + ' '+l[i][1]+' '+"{:.2f}".format(l[i][2]))

def readTxt(number_rows):
    with open('ApplicantsInfo.txt','r',encoding='utf-8') as f:
        line = f.readline().split()
        if( number_rows == 0):
            N = int(line[0])
        M = int(line[1])
        rows = []
        for _ in range(N):
            row = f.readline().split()
            row_mean = my_mean([int(x) for x in row[2:M+2]],M)
            rows.append([row[0],row[1],row_mean])
    return rows,N
