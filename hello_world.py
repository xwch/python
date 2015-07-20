#coding:utf-8

print ("hello world")


#定义&初始化数组
movies =["one","two","three"]

print (movies[0]+movies[1]+movies[2])


#打印整个数组
print(movies)

#数组长度
print(len(movies))

#末尾增加一个数组元素
movies.append("four")
print(movies)


#删除最后一个元素
movies.pop()
print(movies)

#在列表中找到并删除指定项
movies.remove("one")
print(movies)

#在指定位置插入一个数据
movies.insert(0,"five")
print(movies)


#在python中可以混合存储任意类型的数据，如字符串+数字

movies_2 = "\"我是谢伟昌\""
print (movies_2)
#print (movies_2.decode('utf-8'))









