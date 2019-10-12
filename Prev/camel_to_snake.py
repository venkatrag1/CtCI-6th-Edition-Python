

def camel_to_snake(s):
    res = [s[0].lower()]
    for c in s[1:]:
        if c.isupper():
            res.append('_')
            c = c.lower()
        res.append(c)
    return ''.join(res)

print(camel_to_snake("helloWorld"))
print(camel_to_snake("BlueBox"))