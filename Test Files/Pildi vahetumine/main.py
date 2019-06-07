from pygame import * #Kui kirjutatakse "import pygame", peab iga PyGame käsu ette kirjutama pygame..
import random
import pickle
#Üks planeeritud mänguvõimalustest on tegelase loomine. Selleks, et mängija saaks seda tegema, peab olema mitu pilti, mis vahetuvad.
#Eesmärk on panna stringidest kokku pildi nimi ja laadida läbi selle pilt. Pärast seda muuta ühte osa stringist noolevajutusega nii, et pilt muutub.
#Plaan: Määrata ära kaks muutujat, mis koosneb mitmest stringist. Noolevajutusega muutub üks muutuja, arvuti näeb, et need kaks stringi pole sama, ja muudab pilti.

tag = 'hair_' #Pildi eessõna.
hair = 5 #Esimene arv.
if hair < 10:
    hair = '0'+str(hair) #Kui arv on ühekohaline, siis arvuti muudab arvu stringiks ja lisab numbri ette number 0.
clothing = 20 #Teine arv.
if clothing < 10:
    clothing = '0'+str(clothing) #Sama, mis esimene.
color = 10 #Kolmas arv.
uus = tag+str(hair)+str(clothing)+str(color)+'.png' #Panen kokku pildi eessõnast ja kolmest arvust kokku stringi, mis samastub pildi nimega, ja panen muutuja alla uus.
nimi = 0 #See on teine pildi string. Selle sätin nulliks.
print('nimi')

aken_laius = 500 #Sätin ära akna laiuse.
aken_pikkus = 500 #Sätin ära akna pikkuse.
pildi_x = aken_laius / 2 #Sätin pildi asukoha keskele.
pildi_y = aken_pikkus / 2 #Koordinaadid vastavad pildi vasaku ülemise äärega.
aken = display.set_mode([aken_laius, aken_pikkus]) #display.set_mode avab akna, kus tegevus toimub. Sulgudesse tuleb panna akna laiuse ja pikkuse.
aken.fill([255,255,255]) #Teen akna taustapildi valgeks. See funktsioon värvib ära taustavärvi. Sulgudesse tuleb panna nurksulgudes värvi RGB kood.
mäng = True #Sätin ära, et mäng käib. Senikaua kuni see väärtus on tõene, ei sulgu avanenud aken.
while mäng:
    for k in event.get(): #See sätib ära, mida nupu vajutused ja lahtilaskmised teevad.
        if k.type == QUIT:
            mäng = False #Kui vajutad ristist kinni, mängu käimise väärtus on väär ja mäng läheb kinni.
        if k.type == KEYDOWN: #Määran ära, mis juhtub, kui klaviatuuril vajutatakse klahvi alla.
            if k.key == K_RIGHT: #Kui vajutatakse paremat nooleklahvi, muudan color stringi ja panen kokku uue pildikoodi muutuja all "uus".
                if color == 10:
                    color = 15
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
                elif color == 15:
                    color = 10
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
            if k.key == K_LEFT: #Kui vajutatakse vasakut nooleklahvi, muudan color stringi ja panen kokku uue pildikoodi muutuja all "uus".
                if color == 10:
                    color = 15
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
                elif color == 15:
                    color = 10
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
            if k.key == K_UP: #See on kõrvaline. Plaan oli, et ülesse ja alla vajutades muutub akna suurus.
                aken_laius = aken_pikkus - 1
            if k.key == K_DOWN:
                aken_laius = aken_pikkus + 1
    if nimi != uus: #Kui muutuja "nimi" pole sama mis muutuja "uus", avab arvuti uue pildi.
        nimi = uus #Et arvuti kogu aeg pilti uuesti ei laeks, sätin mõlemad muutujad samaks.
        pilt = image.load(nimi) #See funktsioon paneb pildi muutuja "pilt" alla. See pilt, mis laetakse, kannab sama nime kui muutuja "nimi" string.
    aken.blit(pilt, [50, 50]) #See paneb pildi muutuja all "pilt" ekraanile. Selle ülemine vasak äär puudutab koordinaate (50;50) (programmides suureneb y-telg alla minnes).
    display.flip() #See funktsioon uuendab ekraanipilti.

quit() #Kui muutuja "mäng" on väär, siis see funktsioon sulgeb akna.
