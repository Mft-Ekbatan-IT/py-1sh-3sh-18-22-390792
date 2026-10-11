


def add(name:str,product_id:str,price:int):
    """تابع اضافه کردن به فروشگاه قسمت ادد ویشلیست یا لیست علاقه مندی 

    Args:
        name (str): نام محصول مورد علاقه 
        product_id (str): آی دی محصول ما در لیست علاقه مندی
        price (int): قیمت 

    Returns:
        dict: شامل اسم محصول و قیمت  بر اساس کلید ما که پروداکت آی دی 
    """

    while True:
        store={"1":{"name":"iphone","price":1000}}
        
        
        store[product_id]={"name":name,"price":price}
        return store
        