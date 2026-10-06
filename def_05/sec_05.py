

# 1.nation id 

# 2.name

# 3.shomare hesab 

# 4. phone 

#

def store_wishlist():
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
                    store[product_id]={"name":name,"price":price}
                    print(store)
                    break
                case "2":
                    product_id=input("product id ro vared kon:")
                    store_=store.get(product_id)
                    if store_:
                        return(store[product_id])
                        
                    
                        break
                    else:
                        return("not found")
                        break
                case"3":
                    product_id=input("product id:")
                    store_=store.get(product_id)
                    if store_:
                        store.pop(product_id)
                    else:
                        return("not found")
                    break
                case"4":
                    product_id=input("product id:")
                    store_=store.get(product_id)
                    if store_:
                        
                        
                        
                        
                        wishlist.append(store[product_id])
                        return(wishlist)
                        
                        return(wishlist)
                        break
                    else:
                        return("not found")
                        break



store_wishlist()

# function

# def 
#from typing import int,float 
#def jam (a:int|float,b:int|float)->int|float:
#    """ جمع دو عدد با هم و نمایش حاصل جمع آنها باهم دیگر 
#
#    Args:
#        a (_type_): int|float
#        b (_type_): int|float
#    """
#    
#    c= a+b
#    print(c)
#x=int(input("adad 1 ra bezan:"))
#y=int(input("adad 2 ra bezan:"))
#jam(x,y)




