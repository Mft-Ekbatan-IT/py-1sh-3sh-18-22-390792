


from add import *
from find import *
from delet import *
from wishlist import *


store={"1":{"name":"iphone","price":1000}}
wishlist=[]
while True:
    menu=input("1.add 2.find 3.delete from wish list 4.wishlist  5.exit")
    while True:
        match menu:
            case"1":
                product_id=input("product id ro vared kon:")
                name=input("namet ro vared kon:")
                        
                price=int(input("price:"))
                add(name,product_id,price)
                break
            case "2":
                product_id=input("product id ro vared kon:")
                find(product_id)
                break
                
            case"3":
                product_id=input("product id:")
                store_=store.get(product_id)
                delet(product_id)
                break
            case"4":
                product_id=input("product id:")
                store_=store.get(product_id)
            
            case"5":
                break    
                