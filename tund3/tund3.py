


print("Tere! Olen sinu uus sõber - Python!")
nimi=str(input("Utle sinu nimi  "))
print (f"{nimi}" , "oi kui ilus nimi!")  #nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>
choose=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah >"))
if choose ==1:
    try:
        pikkus=int(input("Sisesta oma pikkus  "))
        while pikkus<0:
            print("Pikkus on negatiine!! Kirjuta õigesti  ")
            pikkus=int(input("Sisesta oma pikkus  "))
        else:
            pass
    except:
        print("error")
    try:
        mass= float(input("Sisesta oma kaal  "))
    except:
        print("error")
    index= round((mass/(0.01*pikkus)**2),1)
    print("Sinu keha indeks on:",index)
    if index < 16:
        ans="Tervisele ohtlik alakaal"
    elif 16< index <=19:
            ans="Alakaal "
    elif 19< index <=25:
             ans="Normaalkaal"
    elif 25< index <=30:
             ans="Ülekaal"
    elif 30< index <=35:
            ans="Rasvumine"
    elif 35< index <=40:
            ans="Tugev rasvumine"
    print(ans)
else:
    print("Kahju! See on väga kasulik info!")
    print()
