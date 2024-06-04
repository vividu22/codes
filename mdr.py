import flask
def i():
    i=5
    while i<=1000:
        i+=5
    return i 

print(i())