#encoding:utf-8


'''
递归模块
'''


#定义list输出的递归函数
def print_lol(the_list):
	'''
	递归输出所有嵌套列表元素
	'''
	for each_ietm in the_list:
		if isinstance(each_ietm,list):
			print_lol(each_ietm)
		else:
			print (each_ietm)