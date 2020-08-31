class Items:
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty

    @staticmethod
    def update(items):
        for item in items:
            if item.name=='milk':
                item.name='Sugar'
                break



    @staticmethod
    def get_items():
        my_items = [{'name': 'bread', 'price': 0.5, 'quantity': 20},{'name': 'milk', 'price': 1.0, 'quantity': 10},\
        {'name': 'wine', 'price': 10.0, 'quantity': 5}]
        res=[]
        for item in my_items:
            item_obj=Items(item['name'],item['price'],item['quantity'])
            res.append(item_obj)
        return res


    