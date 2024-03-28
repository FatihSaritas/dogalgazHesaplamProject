#Ayların gün miktarını belirtin.
ocak = mart = mayıs = temmuz = agustos = ekim = aralık = 31
haziran = nisan = kasım = eylül = 30 
şubat = 28

#metre küp birim fiyatı 
birimfiyat = 1.251652

#aylık kaç metre küp doğalgaz kullanıdınız

aylikMetrekupKullanım = input('Aylık kaç metreküp doğalgaz kullandınız ? : ')

#Ay belirtme 

donem = input('Handi aya,a ait dönem faturası hesaplamak isityorsunuz ? : ')

#python anlayacağı şekil

ay = eval(donem)

#günlük dogalgaz kullanımı 

gunluk_Kullanım = int(aylikMetrekupKullanım) / ay

#Fatura tutarı oluşturma 

fatura = birimfiyat * gunluk_Kullanım * ay

print('Günlük Kullanım : \t',gunluk_Kullanım, 'metreküp \n','Tahmini fatura tutarı : \t',fatura,'TL')
