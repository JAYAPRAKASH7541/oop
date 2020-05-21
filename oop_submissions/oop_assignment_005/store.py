class Item:
    def __init__(self,name,price,category):
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self._name=name
        self._price=price
        self._category=category
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def category(self):
        return self._category
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
class Store:
    def __init__(self):
        self.s=""
        self.li=[]
        self.items=''
    def add_item(self,item):
        self.items=self.items+str(item)+"\n"
        self.li.append(item)
    def __str__(self):
        if len(self.items)>0:
            return self.items[:-1]
        else:
            return "No items"
    def filter(self,query):
        result=Store()
        for i in self.li:
            k=getattr(i,query.field)
            #print(query.value)
            if query.operation=='IN' and k in query.value:
                result.add_item(i)
            if query.operation=='EQ' and k==query.value:
                result.add_item(i)
            if query.operation=='GT' and k>query.value:
                result.add_item(i)
            if query.operation=='LT' and k<query.value:
                result.add_item(i)
            if query.operation=='GTE' and k>=query.value:
                result.add_item(i)
            if query.operation=='LTE' and k<=query.value:
                result.add_item(i)
            if query.operation=='STARTS_WITH' and k.startswith(query.value):
                result.add_item(i)
            if query.operation=='ENDS_WITH' and k.endswith(query.value):
                result.add_item(i)
            if query.operation=='CONTAINS' and query.value in k:
                result.add_item(i)
        '''if query.operation=='IN':
            for i in self.li:
                if i.name in query.value or i.price in query.value or i.category in query.value:
                    result.add_item(i)
        if query.operation=='EQ':
            if query.field=='name':
                for i in self.li:
                    x=i.name
                    if x==query.value:
                        result.add_item(i)
            elif query.field=='price':
                for i in self.li:
                    x=i.price
                    if x==query.value:
                        result.add_item(i)
            elif query.field=='category':
                for i in self.li:
                    x=i.category
                    if x==query.value:
                        result.add_item(i)
        if query.operation=='GT':
            for i in self.li:
                x=i.price
                if int(query.value)<x:
                    result.add_item(i)
    
        if query.operation=='GTE':
            for i in self.li:
                x=i.price
                if int(query.value)<=x:
                    result.add_item(i)
        if query.operation=='LT':
            for i in self.li:
                x=i.price
                if int(query.value)>x:
                    result.add_item(i)
        
        if query.operation=='LTE':
            for i in self.li:
                x=i.price
                if int(query.value)>=x:
                    result.add_item(i)
        if query.operation=='STARTS_WITH':
            for i in self.li:
                if (i.name).startswith(query.value) or (i.category).startswith(query.value):
                    result.add_item(i)
        if query.operation=='ENDS_WITH':
            for i in self.li:
                if (i.name).endswith(query.value) or (i.category).endswith(query.value):
                    result.add_item(i)
        if query.operation=='CONTAINS':
            for i in self.li:
                if (query.field=='name' and query.value in i.name) or (query.field=='category' and query.value in i.category):
                    result.add_item(i)'''
        return result
    def exclude(self,query):
        r1=Store()
        self.filter_list=self.filter(query)
        for i in self.li:
            if str(i) not in self.filter_list.items:
                r1.add_item(i)
        return r1
    def count(self):
        return len(self.li)
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.value=value
        if operation!='IN' and operation!='EQ' and operation!='LT' and operation!='LTE' and operation!='GTE' and operation!='GT' and operation!='STARTS_WITH' and operation!='ENDS_WITH' and operation!='CONTAINS':
            raise ValueError("Invalid value for operation, got random")
        self.operation=operation
    def __str__(self):
        return '{} {} {}'.format(self.field,self.operation,self.value)
'''store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item)  
query = Query(field="price", operation="IN", value="20")  
results = store.filter(query)'''
#print(results)