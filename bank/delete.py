




def delete(kode_meli,name,shomare_hesab):
    bank_dict={}
    bank_=bank_dict.get(kode_meli)
    if bank_:
        sharj=int(input("sharj:")) 
        mojody+=sharj
        bank_dict[kode_meli]={"name":name,"shomare hesab":shomare_hesab,"mojody":mojody}
    else:
        return("not found")