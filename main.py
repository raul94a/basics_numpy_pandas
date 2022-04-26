
def sumar(a, b):
    # if type(a) is not number or type(b) is not number: return
    try:
        return a+b
    except:
        Exception('An error has ocurred')
print(sumar('5.5',6))
    