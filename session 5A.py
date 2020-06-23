from builtins import type

state1 = {
    "active": 881,
	"confirmed": 3497,
	"deaths": 78,
	"recovered": 2538,
	"state": "Punjab",
}

state2 = {
    "active": 51922,
	"confirmed": "116752",
	"deaths": 5651,
	"recovered": 59166,
	"state": "Maharashtra",
}

state3 = {
	"active": 21993,
	"confirmed": 50193,
	"deaths": 576,
	"recovered": 27624,
	"state": "Tamil Nadu",
}

state4 = {
	"active": 27741,
	"confirmed": 47102,
	"deaths": 1904,
	"recovered": 17457,
	"state": "Delhi",
}


state5 = {
	"active": 6149,
	"confirmed": 25148,
	"deaths": 1561,
	"recovered": 17438,
	"state": "Gujarat",
}

state6 = {
	"active": 5659,
	"confirmed": 15785,
	"deaths": 488,
	"recovered": 9638,
	"state": "Uttar Pradesh",
}

state7 = {
	"active": 2721,
	"confirmed": 13626,
	"deaths": 323,
	"recovered": 10582,
	"state": "Rajasthan",
}

state8 = {
	"active": 2308,
	"confirmed": 11426,
	"deaths": 486,
	"recovered": 8632,
	"state": "Madhya Pradesh",
}

state9 = {
	"active": 4528,
	"confirmed": 7944,
	"deaths": 134,
	"recovered": 4983,
	"state": "Haryana",
}

state10 = {
	"active": 2842,
	"confirmed": 3615,
	"deaths": 115,
	"recovered": 2570,
	"state": "Karnataka",
}


states = [state1,state2,state3,state4,state5,state6,state7,state8,state9,state10]
print("states is ",len(states),type(states))
