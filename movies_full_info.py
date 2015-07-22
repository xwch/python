#encoding:utf-8

import nester

#列表的多层嵌套,打印Eric Idle
movies = [
	"The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
		["Graham Chapman",
			["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]
		]
			]

nester.print_lol(movies)


	

