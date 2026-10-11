


def delet(product_id:str)->dict:
    """
    حذف از ویشلیست 
    Args:
        product_id (str): شناسه محصول 

    Returns:
        dict: محصول و شناسه محصول 
    """
    
    while True:
        store={"1":{"name":"iphone","price":1000}}
        store_=store.get(product_id)
        if store_:
            return (store.pop(product_id))
        else:
            return("not found")
            