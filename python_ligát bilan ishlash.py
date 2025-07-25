# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 08:08:12 2025

@author: User
"""

#car_o={'model':'ferrari', 'color': 'red'}

#en_uz={'apple':'olma', 'peach':'shaftoli','banana':'banan'}
#print(en_uz['apple'])

#mevalar={'olma':'10000','shaftoli':'20000'}
#print(f"Olma narxi {mevalar['olma']} som")

talaba_0={'ism':'Nasiba','yosh':'26','kurs':'4'}
print(f"{talaba_0['ism']},{talaba_0['yosh']}da")

#talaba_0['kurs']=5
#talaba_0['fakultet']='informatika'

#print(talaba_0)

#talaba_1={}
#talaba_1['ism']='sharifa'
#talaba_1['familiya']='toshboltayeva'
#talaba_1['kurs']=2
#rint(f"{talaba_1['ism'].title()} {talaba_1['familiya']} {talaba_1['kurs']}da oqiydi")

#del talaba_0['yosh']
#print(talaba_0)

  #get metodi
#telefonlar={
   # 'Ali':'iphonex',
   # 'vali':'edme',
   # 'nasiba':'iphone 11',
   # }
#print(telefonlar)

#otam={'ism':'Gulomjon','t_yil':'1970','yosh':'55'}
#print(f"Otam {otam['ism']}, {otam['t_yil']} da tugilgan, {otam['yosh']}da")

python_izohli_lugati={
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}

kalit=input('Iltimos kalit soz kiriting')
print(python_izohli_lugati.get(kalit, 'bunday kalit soz mavjud emas'))






























