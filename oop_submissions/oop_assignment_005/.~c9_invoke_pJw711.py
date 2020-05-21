class Item:
    def __init__(self,name,price,category):
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.name=name
        self.price=price
        self.category=category
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
        if query.operation=='IN':
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
                    result.add_item(i)
        return result
    def exclude(self,query):
        r1=Store()
        filter_list=filter(query)
        #filter_list.append(r1.items)
        #print(filter_list)
        for i in self.li:
            if i not in filter_list:
                r1.Store
        '''r1=Store()
        if query.operation=='IN':
            for i in self.li:
                if i.name not in query.value and i.price not in query.value and i.category not in query.value:
                    r1.add_item(i)
        if query.operation=='EQ':
            if query.field=='name':
                for i in self.li:
                    x=i.name
                    if x!=query.value:
                        r1.add_item(i)
            elif query.field=='price':
                for i in self.li:
                    x=i.price
                    if x!=query.value:
                        r1.add_item(i)
            elif query.field=='category':
                for i in self.li:
                    x=i.category
                    if x!=query.value:
                        r1.add_item(i)
        if query.operation=='GT':
            for i in self.li:
                x=i.price
                if int(query.value)>=x:
                    r1.add_item(i)
        if query.operation=='GTE':
            for i in self.li:
                x=i.price
                if int(query.value)>x:
                    r1.add_item(i)
        if query.operation=='LT':
            for i in self.li:
                x=i.price
                if int(query.value)<=x:
                    r1.add_item(i)
        
        if query.operation=='LTE':
            for i in self.li:
                x=i.price
                if int(query.value)<x:
                    r1.add_item(i)
        if query.operation=='STARTS_WITH':
            if query.field=='name':
                for i in self.li:
                    x=i.name
                    if x.startswith(query.value):
                        pass
                    else:
                        r1.add_item(i)
            elif query.field=='category':
                for i in self.li:
                    x=i.category
                    if x.startswith(query.value):
                        pass
                    else:
                        r1.add_item(i)
        if query.operation=='ENDS_WITH':
            if query.field=='name':
                for i in self.li:
                    x=i.name
                    if x.endswith(query.value):
                        pass
                    else:
                        r1.add_item(i)
            elif query.field=='category':
                for i in self.li:
                    x=i.category
                    if x.endswith(query.value):
                        pass
                    else:
                        r1.add_item(i)
        if query.operation=='CONTAINS':
            for i in self.li:
                if (query.field=='name' and query.value not in i.name) or (query.field=='category' and query.value not in i.category):
                    r1.add_item(i)
        return r1'''
    def count(self):
        return len(self.li)
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.value=value
        if operation!='IN' and operation!='EQ' and operation!='LT' and operation!='LTE' and operation!='GTE' and operation!='GT' and operation!='STARTS_WITH' and operation!='ENDS_WITH' and operation!='CONTAINS':
            raise ValueError("Invalid value for operation, got random")
        else:
            self.operation=operation
    def __str__(self):
        return '{} {} {}'.format(self.field,self.operation,self.value)


store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item)  
query = Query(field="category", operation="STARTS_WITH", value="Boost")  
results = store.exclude(query)  # exclude all items whose price is greater than 15 
print(results) 


