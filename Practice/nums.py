nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [1,3,5,7,9]
print([x for x in nums if x % 2 != 0])

# [1,4,9,16,25]
print([x**2 for x in nums if x <= 5])

# [1,4,3,16,5,36,7,64,9]
print([x**2 if x % 2 == 0 else x for x in nums])


results = [{
    "name": "pardis",
    "score": 10
}, {
    "name": "mahdi",
    "score": 20
}, {
    "name": "ali",
    "score": 5
}, {
    "name": "reza",
    "score": 15
}]


# [{
#   "name":"mahdi",
#     "score":20
#     },{
#       "name":"reza",
#     "score":15
#     }]

print([x for x in results if x["score"] > 10])

print("**************************")

# [{
#     "name":"pardis",
#     "passed":True
# },{
#     "name":"mahdi",
#     "passed":True
# },{
#     "name":"ali",
#     "passed":False
# },{
#     "name":"reza",
#     "passed":True
# }]


print([{"name ": x["name"], "passed": x["score"] >= 10} for x in results])
