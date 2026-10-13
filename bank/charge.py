





def charge(kode_meli):
    bank_dict={}
    bank_=bank_dict.get(kode_meli)
    if bank_:
        bank_dict.pop(kode_meli)
    else:
        return"not found"