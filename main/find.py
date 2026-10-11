
def find(product_id:str)->dict:
    
    """پیدا کردن یک محصول 
    با پروداکت آی دی 

    Returns:
        dict: دیکشنری محصول 
    """
    
    while True:
        store={"1":{"name":"iphone","price":1000}}
        store_=store.get(product_id)
        if store_:
            return store[product_id]
                            
                        
           
        else:
            return ("not found")
            
            
            
            
            