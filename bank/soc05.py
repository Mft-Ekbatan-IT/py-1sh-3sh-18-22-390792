bank={}
while True:
    menu=input("1.add 2.find 3.charge 4.delete 5.exit")
    while True:
        match menu:
            case"1":
                kode_meli=input("kodev mweli ro vared kon:")
                name=input("namet ro vared kon:")
                shomare_hesab=input("shomare hesab bede:")
                mojody=int(input("mojady:"))
                bank[kode_meli]={"name":name,"shomare hesab":shomare_hesab,"mojody":mojody}
                print(bank)
                break
            case "2":
                kode_meli=input("kodev mweli ro vared kon:")
                bank_=bank.get(kode_meli)
                if bank_:
                    print(bank[kode_meli])
                    print(bank[name])
                    print(bank[shomare_hesab])
                else:
                    print("not found")
                    break
            case"3":
                kode_meli=input("shomare hesab bede:")
                bank_=bank.get(kode_meli)
                if bank_:
                    bank.pop(kode_meli)
                else:
                    print("not found")
                break
            case"4":
                kode_meli=input("shomare hesab bede:")
                bank_=bank.get(kode_meli)
                if bank_:
                    sharj=int(input("sharj:")) 
                    mojody+=sharj
                    bank[kode_meli]={"name":name,"shomare hesab":shomare_hesab,"mojody":mojody}
                else:
                    print("not found")
                break
