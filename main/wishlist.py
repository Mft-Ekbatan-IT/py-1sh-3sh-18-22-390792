

def wishlist(product_id:str)->dict:
    """_summary_

    Args:
        product_id (str): _description_

    Returns:
        dict: _description_
    """
    while True:
        store={"1":{"name":"iphone","price":1000}}
        wishlist=[]
        store_=store.get(product_id)
        if store_:
                            
                           
            return(store[product_id],wishlist.append(store[product_id]) )
                            
        else:
            return("not found")
            