

# 1.nation id 

# 2.name

# 3.shomare hesab 

# 4. phone 




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
                    print(store[product_id])
                    
                   
                    break
                else:
                    print("not found")
                    break
            case"3":
                product_id=input("product id:")
                store_=store.get(product_id)
                if store_:
                    store.pop(product_id)
                else:
                    print("not found")
                break
            case"4":
                product_id=input("product id:")
                store_=store.get(product_id)
                if store_:
                    
                    
                    print(store[product_id])
                    
                    
                    print(wishlist)
                    wishlist.append(store[product_id])
                    print(wishlist)
                    break
                else:
                    print("not found")
                    break