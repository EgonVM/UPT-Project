from pygame import *
#Kuna mängus saab ringi liikuda, tuleb määrata ära alad, kuhu tegelane ei saa minna.
#Eesmärk on määrata ära ala, kuhu liikuda ei saa. Nendesse aladesse kuuluvad ääred ja ruut ekraani keskel.
#Plaan: Panna programm vaatama, kus tegelane on, ja takistada liikumist kui tegelane on ääres.

char = image.load("Kuju.png") #Laen sisse tegelase pildi.
char_x = 300 #Sätin ära tegelase asukoha.
char_y = 300
kiirus_x = 0 #Panen sisse kiiruse muutujad.
kiirus_y = 0
saabup = True #Sätin ära tõeväärused, mis määravad ära, kas kindlas suunas saab liikuda.
saabdown = True
saableft = True
saabright = True

aken = display.set_mode([1000, 1000]) #Avan akna suurustega 1000x1000.
mäng = True
while mäng:
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
    if saabup == False: #Kui ei saa üles minna, siis y-telje kiirus muudetakse nulliks kui see on negatiivne.
        if kiirus_y < 0:
            kiirus_y = 0
    if saabdown == False: #Kui ei saa alla minna, siis y-telje kiirus muudetakse nulliks kui see on positiivne.
        if kiirus_y > 0:
            kiirus_y = 0
    if saableft == False: #Kui ei saa vasakule minna, siis x-telje kiirus muudetakse nulliks kui see on negatiivne.
        if kiirus_x < 0:
            kiirus_x = 0
    if saabright == False: #Kui ei saa paremale minna, siis y-telje kiirus muudetakse nulliks kui see on positiivne.
        if kiirus_x > 0:
            kiirus_x = 0
    char_x = char_x + kiirus_x #X-telje asukoht muutub, kui parem või vasak nooleklahv on alla vajutatud.
    char_y = char_y + kiirus_y #Y-telje asukoht muutub, kui ülemine või alumine nooleklahv on alla vajutatud.
    if char_x <= 200 or char_x >= 800 or char_y <= 200 or char_y >= 800: #sätin ära äärte piirid, kust üle ei tohi astuda.
        if char_x <= 200: #Kui on vasakul piiril, ei saa enam vasakule liikuda.
            saableft = False
        else:
            saableft = True
        if char_x >= 800: #Kui on paremal piiril, ei saa tegalane enam paremale liikuda.
            char_x -= 1
        if char_x == 799:
            saabright = False
        else:
            saabright = True
        if char_y <= 200: #Kui on ülemisel piiril, ei saa enam üles liikuda. Siin tuleb kasutada if tingimust selleks, et tegelane kindlasti ei saaks üle ääre liikuda.
            saabup = False
        else:
            saabup = True
        if char_y >= 800: #Kui on alumisel piiril, ei saa enam alla liikuda. Siin tuleb kasutada if tingimust selleks, et tegelane kindlasti ei saaks üle ääre liikuda.
            saabdown = False
        else:
            saabdown = True
    
    elif char_x >= 400 - 55 and char_x <= 600 and char_y >= 400 - 84 and char_y <= 600:#See kontrollib, kas kuju on ruudu sees või mitte, lükkab ta välja ja takistab sisse liikumist.
        if char_x >= 400 - 55 and char_x < 500: #Välja lükkamine.
            char_x -= 1
        if char_x == 400 - 56: #Takistamine
            saabright = False
        if char_x <= 600 and char_x >= 500: #Välja lükkamine
            char_x += 1
        if char_x == 600 + 1: #Takistamine
            saableft = False
        if char_y >= 400 - 84 and char_y < 500: #Välja lükkamine
            char_y -= 1
        if char_y == 400 - 84 - 1: #Takistamine
            saabdown = False
        if char_y <= 600 and char_y >= 500: #Välja lükkamine
            char_y += 1
        if char_y == 600 + 1: #Takistamine
            saabup = False
    else: #Kui tegelane ei puuduta ühtegi piiri, saab ta vabalt liikuda.
        saabup = True
        saabdown = True
        saableft = True
        saabright = True
    aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
    draw.rect(aken, [150,150,150], [400, 400, 200, 200]) #Joonistan keskele halli ruudu, mille pikkus on 200 ja laius 200.
    aken.blit(char, [char_x, char_y]) #Panen tegelase aknale.
    display.flip() #Uuendan ekraani.

quit() #Kui vajutatakse ristist kinni, läheb ekraan kinni.