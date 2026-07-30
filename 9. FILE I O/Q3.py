def table(a):

    with open(f"table/table_{a}.txt","w")  as f:
        for i in range(1,11):
            f.write(f"{a} * {i} = {a*i}")
# pre build folder named table is need in order to run this program also try and except can solve this just not taught till now
        



for i in range (2,21):
    table(i)