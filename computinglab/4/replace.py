code = """ 
sum = 0

for i in range(0,21):
    sum = sum + i


print(sum)

"""


with open("sum1to10.py","w") as override:
    override.write(code)

exec(open("sum1to10.py").read())