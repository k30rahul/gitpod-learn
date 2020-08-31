from model import Items

def display(items):
    for item in items:
        print('[name:{},price:{},qty:{}]'.format(item.name,item.price,item.qty))