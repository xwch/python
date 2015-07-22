#coding:utf-8

#print ("hello world")

#定义一个数组, 存放电影信息 
movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]
print(movies)


#插入年份
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)

print (movies)


movies_2 = ["The Holy Grail",1975,
			"The Life of Brian",1979,
			"The Meaning of Life",1983]
	
print (movies_2)



#for循环，迭代输出每一个子都
fav_movies = ["The Holy Grail","The Life of Brian"]

for each_flick in fav_movies:
	print (each_flick)


#while循环
count = 0
while count < len(fav_movies):
	print (fav_movies[count])
	count = count + 1



count = 1
while count <= len(fav_movies):
	print(fav_movies[count-1])
	count = count + 1




'''
while循环有一个不好的地方在于，下界的判断容易错误。
'''

#列表的多层嵌套,打印Eric Idle
movies = [
	"The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
		["Graham Chapman",
			["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]
		]
			]

#print (movies[4][1][3])
#print movies[4][1][4]

for each_flick in movies:
	if isinstance(each_flick,list):
		for next_flick in each_flick:
			print(next_flick)
	else:
		print(each_flick)





#-------------------------------------------------
#2015-07-21   by xwch

#isinstance()函数，允许检查某个特定标识符是否包含某个特定类型的数据，例如列表中是否包含列表
demo_list = ["one","two"]
flag = isinstance(demo_list,list)
print(flag)   #结果为true



length_of_demo_list = len(demo_list)
print (length_of_demo_list)





#有3层列表list，所以需要3个for
for each_flick in movies:
	if isinstance(each_flick,list):
		for next_flick in each_flick:
			if isinstance(next_flick,list):
				for deeper_lick in next_flick:
					print (deeper_lick)
			else:
				print (next_flick)
			#print(next_flick)
	else:
		print(each_flick)





print ("\n")

#定义list输出的递归函数
def print_lol(the_list):
	for each_ietm in the_list:
		if isinstance(each_ietm,list):
			print_lol(each_ietm)
		else:
			print (each_ietm)

#调用函数
print_lol(movies)

