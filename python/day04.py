from hashlib import md5

key     = "bgvyzdsv"
hashKey = ""
number  = 0

while not hashKey.startswith("000000"):

    number += 1

    numberKey = key + str(number)
    
    function = md5()
    function.update(numberKey.encode("utf-8"))
    hashKey = function.hexdigest()

print("Number: {0}".format(number))
