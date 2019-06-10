from pygame import *
#Kuna mängus saab tegelastele eraldi osasid panna, tuleb nendest eraldi piltidest kokku panna tegelane.
#Eesmärk on panna neljast erinevast pildist kokku tegelane, kes liikudes tõmbab kõik need pildid endaga kaasa.
#Plaan: Tuua sisse 4 pilti, panna tegelase algkoordinaadiks tema jala pildi alumine vasak nurk ja panna nendele otsa keha, pea ja juuksed, mis liiguvad koos jalgadega.

all = image.load("Bottom_Placeholder.png") #Toon kõik need neli pilti mängu.
pluus = image.load("Top_Placeholder.png")
pea = image.load("Face_Placeholder.png")
juuksed = image.load("Hair_Placeholder.png")
asukoht_x = 250 #Määran ära jalgade asukoha x ja y teljel.
asukoht_y = 750
kiirus_x = 0 #Need muutujad on liikumisel vajalik.
kiirus_y = 0 #Need muutujad tagavad, et pilt liiguks senikaua, kuni nooleklahvist lahti lastakse. Lisaks see võimaldab diagonaalset liikumist.

aken = display.set_mode([1000, 1000]) #Sätin akna suuruse.

mäng = True #Et see uus aken ei sulguks kohe, sätin mängu tõeseks.
while mäng: #Senikaua kuni mäng on tõene, mäng käib.
    for k in event.get():
        if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
            mäng = False
        if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
            if k.key == K_RIGHT: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                kiirus_x = 1 #Suureneb x-telje asukoht, et paremale minna.
            if k.key == K_LEFT: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                kiirus_x = -1 #Väheneb x-telje asukoht, et vasakule minna.
            if k.key == K_UP: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                kiirus_y = -1 #Väheneb y-telje asukoht, et ülesse minna.
            if k.key == K_DOWN: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                kiirus_y = 1 #Suureneb y-telje asukoht, et alla minna.
        if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
            if k.key == K_RIGHT:
                kiirus_x = 0
            if k.key == K_LEFT:
                kiirus_x = 0
            if k.key == K_UP:
                kiirus_y = 0
            if k.key == K_DOWN:
                kiirus_y = 0 
    asukoht_x = asukoht_x + kiirus_x #X-telje asukoht muutub, kui parem või vasak nooleklahv on alla vajutatud.
    asukoht_y = asukoht_y + kiirus_y #Y-telje asukoht muutub, kui ülemine või alumine nooleklahv on alla vajutatud.
    aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
    aken.blit(all, [asukoht_x, asukoht_y - 176]) #Panen ekraanile jalad. Muudan y-telje asukohta, et pildi alumine vasak nurk puudutaks asukoha koordinaate.
    aken.blit(pluus, [asukoht_x, asukoht_y - 307]) #Panen ekraanile keha. Muudan y-telje asukohta, et keha kinnituks jalgadele.
    aken.blit(pea, [asukoht_x, asukoht_y - 456]) #Panen ekraanile pea. Muudan y-telja asukohta, et pea asuks kaela otsas.
    aken.blit(juuksed, [asukoht_x - 11, asukoht_y - 460]) #Panen ekraanile juuksed. Muudan x ja y-telje asukohta, et need kinnituksid pähe.
    display.flip() #Pärast kokkupanekut uuendame ekraani.

quit() #Kui vajutatakse ristist kinni, läheb ekraan kinni.