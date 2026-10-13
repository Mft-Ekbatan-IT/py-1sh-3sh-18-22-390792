




from add import *
from find import *
from charge import *




def bank():
    while True:
        bank_dict={}
       

        menu=input("1.add 2.find 3.charge 4.delete 5.exit---->")
        while True:
            match menu:

                case"1":
                    
                    name=input("namet ro vared kon:")
                    shomare_hesab=input("shomare hesab bede:")
                    mojody=int(input("mojady:"))
                    kode_meli=input("kodev meli ro vared kon:")

                    add(kode_meli=kode_meli,name=name,shomare_hesab=shomare_hesab,mojody=mojody)
                
                    
                    break    
                
                case "2":
                    name=input("namet ro vared kon:")
                    kode_meli=input("kodev meli ro vared kon:")
                    shomare_hesab=input("shomare hesab bede:")
                    kode_meli=input("shomare hesab bede:")
                    mojody=int(input("mojody:"))
                    find(kode_meli,name,shomare_hesab)
                    print (bank_dict)
                case "3":
                    
                    mojody=int(input("mojody:"))
                    cahrge(kode_meli)
                    return bank_dict







bank()


