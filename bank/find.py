





def find(kode_meli:str,name,shomare_hesab):
    bank_dict={}
    bank_=bank_dict.get(kode_meli)
    if bank_:
        return bank_dict[kode_meli] (bank_dict[name])(bank_dict[shomare_hesab])
    else:
        return("not found")
        