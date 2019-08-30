from pygame import *
import random
#Kuna mängus on õppimised võitluste moodi ja sisaldab RPG mängu elemente, tuleks teha enne väike RPG mäng koos võitlustega, et harjutada.
#Eesmärk on näidata tervise ja vaimse punkte, teha võitlusi ja panna sisse levelid.
#Plaan: Panna ekraanile kolm vaenlast. Pärast nende võitlust on mängija level 2 peal ja saab võidelda bossiga. Juures on skaalad, mis näitavad mängija tervist.

icon = image.load("test.png") #Laen sisse programmiikooni.
sina = image.load("Kuju.png") #Laen sisse tegelaste spraidid.
vaenlane = image.load("Vaenlane.png")
bosss = image.load("Boss.png") #Et muutujad ei läheks segamini, lõppeb see muutuja kolme S-tähega.
õpetuss = image.load("opetus.png") #Laen sisse õpetuse pildi. Sama probleem nagu eelmises reas, sama lahendus.
tegu = 0 #Sean sisse muutuja, mida kasutatakse klassis Vaenlane, et saada juhusliku arvuga rünnaku tulemust and tugevust.
text = '' #Et ruumi muutujatega kokku hoida, on siin üks teksti muutuja, mis saab lause sõnena ja paneb selle ekraanile.
aktiivne = 0 #Näitab ära, kellega võitlus käib. On 0 kui ei käi kellegagiga.
maxhp = 200 #Sätin ära maksimum HP väärtuse.
yourhp = maxhp #Sätin praeguse HP väärtuse maksimaalseks.
maxmp = 100 #Sätin ära maksimum MP väärtuse.
yourmp = maxmp #Sätin praeguse MP väärtuse maksimaalseks.
maxxp = 330 #Sätin ära maksimaalse XP väärtuse ära (kui palju XP punkte on vaja, et tõsta tegelase taset).
yourxp = 0 #Sätin praeguse XP väärtuse nulliks.
yourlevel = 1 #Sätin praeguse leveli ühe peale.
yourturn = 1 #Sätin korra mängijale. Kui väärtus on 1, siis on mängija kord rünnata. Kui väärtus on 0, on vaenlase kord.
õpetus = True #Sätin õpetus väärtuse tõeseks, et mängu alguses näida õpetust.

class Vaenlane: #Seekord proovin teha vaenlaste klassi, mis sisaldab vaenlast väärtuse.
    def __init__(self, nimi, hp, xp, raskus, x, y):  #Määran ära väärtused.
        self.nimi = nimi #Vaenlase nimi.
        self.hp = hp #Vaenlase HP hulk.
        self.xp = xp #Kui palju XP punkte annab vaenlane võidu korral.
        self.raskus = raskus #Missugune raskusaste vaenlasel on.
        self.x = x #Vaenlase asukoht liikumisefaasis.
        self.y = y
    
    def bedone(self, meetod): #Funktsioon, mis määrab ära mängija mõju vaenlasele.
        tegu = random.randint(1,100) #Muutuja tegu väärtus on juhuslikult üks kuni sada.
        global text #Toon muutuja text sisse globaalse väärtusena, et muutuks tekst võitluse ajal.
        if meetod == 'attack': #Kui mängija ründab.
            if self.raskus == "kerge": #Kui raskusaste on kerge, siis...
                if tegu >= 70: #On nii suur võimalus vaenlasele palju kahju teha.
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text #ja tagastatakse see.
                elif tegu <= 10: #On nii suur võimalus kõrvale hüpata.
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else: #Muidu on tavaline rünnak.
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "keskmine":
                if tegu >= 80:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 20:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "raske":
                if tegu >= 90:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 30:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "boss":
                if tegu >= 95:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 45:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
        if meetod == 'magic': #Kui mängija kasutab maagijat.
            global yourmp #Toon sisse mängija MP väärtuse.
            if yourmp > 0: #Kui mängija MP punktid pole otsas, toimub rünnak.
                tegu = random.randint(1,100) #Muutuja tegu määrab ära, kui suure kahju maagia teeb.
                yourmp -= 20
                if tegu <= 20:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi vähe kahju.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 50:
                    self.hp -= 30 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi piisavat kahju.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 90:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi palju kahju.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 50 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi väga palju kahju.' #Muudetakse ekraaniteksti
                    return text
            else: #Kui mängijal pole MP punkte, on käik ära raisatud.
                text = 'Sul pole piisavalt mp\'d. Maagia ei tulnud üldse välja.' #Muudetakse ekraaniteksti.
        if meetod == 'run': #Kui mängija jookseb ära...
            global sa_x #Toon sisse mängija koordinaatide muutujad, et panna mängija sinna (et võitlus kohe ei taaskäivituks).
            global sa_y
            global aktiivne #Toos sisse muutuja aktiivne, mille väärtus sätitakse õnnestumise korral nulliks.
            tegu = random.randint(1,100) #Muudan muutujat tegu, et ära määrata, kas ära jooksmine õnnestus või mitte.
            if self.raskus == 'kerge': #Väärtused sõltuvad vaenlase raskusastmest.
                if tegu <= 60:
                    text = 'Sul õnnestus ära joosta. Võitlus on lõppenud.' #Muudetakse ekraaniteksti
                    aktiivne = 0
                    sa_x = 424 #Sätin ära tegelase asukoha.
                    sa_y = 766
                    aktiivne = 0
                    return text
                else:
                    text = 'Sul ebaõnnestus ära joosta. Võitlus kestab edasi.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == 'keskmine':
                if tegu <= 40:
                    text = 'Sul õnnestus ära joosta. Võitlus on lõppenud.' #Muudetakse ekraaniteksti
                    aktiivne = 0
                    sa_x = 424 #Sätin ära tegelase asukoha.
                    sa_y = 766
                    aktiivne = 0
                    return text
                else:
                    text = 'Sul ebaõnnestus ära joosta. Võitlus kestab edasi.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == 'raske':
                if tegu <= 20:
                    text = 'Sul õnnestus ära joosta. Võitlus on lõppenud.' #Muudetakse ekraaniteksti
                    aktiivne = 0
                    sa_x = 424 #Sätin ära tegelase asukoha.
                    sa_y = 766
                    aktiivne = 0
                    return text
                else:
                    text = 'Sul ebaõnnestus ära joosta. Võitlus kestab edasi.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == 'boss':
                text = 'Bossi eest on võimatu ära joosta. Sa pead võitlema!' #Muudetakse ekraaniteksti
                return text
        if meetod == 'heal': #Kui mängija võtab aega, et terveneda...
            tegu = random.randint(1,100) #Muudan muutuja tegu väärtust, et ära määrata, kui palju mängija paraneb.
            text = 'Sa võtsid aega, et terveneda.' #Muudetakse ekraaniteksti.
            global yourhp
            if tegu <= 25:
                yourhp += 20
            elif tegu <= 50:
                yourhp += 40
            elif tegu <= 75:
                yourhp += 60
            else:
                yourhp += 80
            return text #Tagastan ekraaniteksti.
    
    def attack(self):
        tegu = random.randint(1,100)
        global text
        global yourhp
        if self.raskus == 'kerge':
            if tegu <= 45:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 95:
                yourhp -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                yourhp -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'keskmine':
            if tegu <= 30:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 90:
                yourhp -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                yourhp -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'raske':
            if tegu <= 20:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 80:
                yourhp -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                yourhp -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'boss':
            if tegu <= 10:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 70:
                yourhp -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                yourhp -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
def näitastaatust(statistika):
    draw.rect(aken, [44,0,0], [5, 5, 200, 15])
    draw.rect(aken, [0,0,36], [5, 21, 200, 15])
    draw.rect(aken, [153,255,153], [5, 37, 200, 15])
    draw.rect(aken, [255,0,0], [5, 5, int(yourhp*200/maxhp), 15])
    draw.rect(aken, [0,0,255], [5, 21, int(yourmp*200/maxmp), 15])
    draw.rect(aken, [4, 129, 114], [5, 37, int(yourxp*200/maxxp), 15])
    aken.blit(fontl.render('Level '+str(yourlevel), 1, [0, 0, 0]), [8, 55])
    if statistika == 1:
        aken.blit(fonts.render('HP: '+str(yourhp)+'/'+str(maxhp), 1, [0, 0, 0]), [210, 5])
        aken.blit(fonts.render('MP: '+str(yourmp)+'/'+str(maxmp), 1, [0, 0, 0]), [210, 28])

sa_x = 424 #Sätin ära tegelase asukoha.
sa_y = 766
kiirus_x = 0 #Panen sisse kiiruse muutujad.
kiirus_y = 0
init()
aken = display.set_mode([900, 900]) #Avan akna suurustega 1000x1000.
display.set_caption('UPT: RPG mängu mehanismide test.') #Sätin ära akna peal oleva teksti.
display.set_icon(icon)
fontl = font.Font(None, 80)
fonts = font.Font(None, 40)

lihtne = Vaenlane('Lihtsu', 100, 110, 'kerge', 294, 559)
keskmine = Vaenlane('Kurir\'a', 100, 120, 'keskmine', 507, 389)
raske = Vaenlane('Rukus', 100, 130, 'raske', 397, 195)
boss = Vaenlane('Boss', 300, 140, 'boss', 900/2-168/2, 5)

mäng = True
while mäng:
    while õpetus and mäng:
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                näitastaatust(0)
                display.flip()
                time.delay(2000)
                õpetus = False
        aken.fill([255,255,255])
        aken.blit(fontl.render('Tere! Aita mul vaenlasi peletada.', 1, [0, 0, 0]), [10, 150])
        aken.blit(fonts.render('Rahu on rikutud. Vaenlased ei anna võitluseta alla!', 1, [0, 0, 0]), [80, 250])
        aken.blit(fonts.render('Vajuta iga klahvi peale, et mängu alustada. Soovin sulle edu!', 1, [0, 0, 0]), [30, 300])
        aken.blit(õpetuss, [100, 400])
        display.flip()
        
    while yourhp > 0 and aktiivne == 0 and mäng:
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                if k.key == K_RIGHT or k.key == K_d: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                    kiirus_x = 1 #Suureneb x-telje asukoht, et paremale minna.
                if k.key == K_LEFT or k.key == K_a: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                    kiirus_x = -1 #Väheneb x-telje asukoht, et vasakule minna.
                if k.key == K_UP or k.key == K_w: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                    kiirus_y = -1 #Väheneb y-telje asukoht, et ülesse minna.
                if k.key == K_DOWN or k.key == K_s: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                    kiirus_y = 1 #Suureneb y-telje asukoht, et alla minna.
            if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
                if k.key == K_RIGHT or k.key == K_d:
                    kiirus_x = 0
                if k.key == K_LEFT or k.key == K_a:
                    kiirus_x = 0
                if k.key == K_UP or k.key == K_w:
                    kiirus_y = 0
                if k.key == K_DOWN or k.key == K_s:
                    kiirus_y = 0
        sa_x = sa_x + kiirus_x #X-telje asukoht muutub, kui parem või vasak nooleklahv on alla vajutatud.
        sa_y = sa_y + kiirus_y #Y-telje asukoht muutub, kui ülemine või alumine nooleklahv on alla vajutatud.
        if sa_x < 1:
            sa_x = 1
        elif sa_x > 899 - 55:
            sa_x = 899 - 55
        if sa_y < 1:
            sa_y = 1
        elif sa_y > 899 - 84:
            sa_y = 899 - 84
        aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
        aken.blit(sina, [sa_x, sa_y]) #Panen tegelase aknale.
        if lihtne.hp > 0:
            aken.blit(vaenlane, [lihtne.x, lihtne.y])
            if sa_x < lihtne.x + 110 and sa_x > lihtne.x - 55 and sa_y < lihtne.y + 168 and sa_y > lihtne.y - 84:
                aktiivne = lihtne
                text = lihtne.nimi+' algatas võitluse.'
        if keskmine.hp > 0:
            aken.blit(vaenlane, [keskmine.x, keskmine.y])
            if sa_x < keskmine.x + 110 and sa_x > keskmine.x - 55 and sa_y < keskmine.y + 168 and sa_y > keskmine.y - 84:
                aktiivne = keskmine
                text = keskmine.nimi+' algatas võitluse.'
        if raske.hp > 0:
            aken.blit(vaenlane, [raske.x, raske.y])
            if sa_x < raske.x + 110 and sa_x > raske.x - 55 and sa_y < raske.y + 168 and sa_y > raske.y - 84:
                aktiivne = raske
                text = raske.nimi+' algatas võitluse.'
        if yourlevel > 1:
            aken.blit(bosss, [boss.x, boss.y])
            if sa_y < boss.y + 168:
                aktiivne = boss
                text = boss.nimi+' algatas viimase võitluse.'
        näitastaatust(0)
        display.flip() #Uuendan ekraani.
        
    kiirus_x = 0 #Panen sisse kiiruse muutujad.
    kiirus_y = 0
    
    while yourhp > 0 and aktiivne != 0 and mäng:
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                if k.key == K_RIGHT or k.key == K_d: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                    if yourturn == 1:
                        aktiivne.bedone('heal')
                if k.key == K_LEFT or k.key == K_a: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                    if yourturn == 1:
                        aktiivne.bedone('magic')
                if k.key == K_UP or k.key == K_w: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                    if yourturn == 1:
                        aktiivne.bedone('attack')
                if k.key == K_DOWN or k.key == K_s: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                    if yourturn == 1:
                        aktiivne.bedone('run')
            if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
                if k.key == K_RIGHT or k.key == K_d:
                    yourturn = 0
                if k.key == K_LEFT or k.key == K_a:
                    yourturn = 0
                if k.key == K_UP or k.key == K_w:
                    yourturn = 0
                if k.key == K_DOWN or k.key == K_s:
                    yourturn = 0
        if aktiivne == 0:
            aken.blit(fonts.render(text, 1, [0, 0, 0]), [10, 750])
            display.flip()
            time.delay(3000)
            continue
        if aktiivne.hp <= 0:
            text = 'Sa võitsid võitluse! Sa said '+str(aktiivne.xp)+' kogemust juurde.'
        aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
        if aktiivne.hp > 0:
            if aktiivne.raskus == 'boss':
                aken.blit(bosss, [int(900/2-110/2), int(900/2-168/2)])
            else:
                aken.blit(vaenlane, [int(900/2-55/2), int(900/2-84/2)])
        aken.blit(fonts.render(text, 1, [0, 0, 0]), [10, 700])
        if yourhp > maxhp:
            yourhp = maxhp
        näitastaatust(1)
        display.flip() #Uuendan ekraani.
        if aktiivne.hp <= 0:
            yourxp += aktiivne.xp
            time.delay(3000)
            if yourxp >= maxxp:
                text = 'Su level tõusis! Su level on nüüd '+str(yourlevel + 1)+'!'
                aken.blit(fonts.render(text, 1, [0, 0, 0]), [10, 750])
                display.flip() #Uuendan ekraani.
                time.delay(3000)
            yourturn = 1
            aktiivne = 0
        if yourturn == 0:
            time.delay(3000)
            aktiivne.attack()
            yourturn = 1
    if yourxp >= maxxp:
        yourlevel += 1
        maxhp += 100
        yourhp = maxhp
        maxmp += 100
        yourmp += int(maxmp/2)
        if yourmp > maxmp:
            yourmp = maxmp
        yourxp -= maxxp
        
    if yourhp <= 0 or boss.hp <= 0:
        pilt_x = 500
        if yourhp <= 0:
            yourhp = 0
    while yourhp <= 0 and mäng:
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                mäng = False
        aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
        aken.blit(fontl.render('Sa kaotasid võitluse. Mäng läbi.', 1, [0, 0, 0]), [20, 150])
        aken.blit(fonts.render('Su HP sai otsa. Tagane korraks, välju mängust ja proovi uuesti.', 1, [0, 0, 0]), [18, 250])
        aken.blit(fonts.render('Vajuta iga klahvi peale, et mängust väljuda. Edu järgmisel korral!', 1, [0, 0, 0]), [10, 300])
        aken.blit(vaenlane, [pilt_x, 600])
        pilt_x -= 1
        if pilt_x < 0-55:
            pilt_x = 900+55
        näitastaatust(1)
        display.flip() #Uuendan ekraani.
    while boss.hp <= 0 and mäng:
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                mäng = False
        aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
        aken.blit(fontl.render('Palju õnne! Sa võitsid mängu!', 1, [0, 0, 0]), [37, 150])
        aken.blit(fonts.render('Suur kuri boss on lõpuks läinud ja rahu on saabunud ekraanile.', 1, [0, 0, 0]), [18, 250])
        aken.blit(fonts.render('Vajuta iga klahvi peale, et mängust väljuda. Tule varsti tagasi!', 1, [0, 0, 0]), [30, 300])
        aken.blit(sina, [pilt_x, 600])
        pilt_x -= 1
        if pilt_x < 0-55:
            pilt_x = 900+55
        näitastaatust(1)
        display.flip() #Uuendan ekraani.

            
quit() #Kui vajutatakse ristist kinni, läheb ekraan kinni.