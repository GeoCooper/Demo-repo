#####################   SÄNKA FARTYG    ###########################

# Denna klass har hand om spelplan, skepp, skapar dem, sparar dem, hanterar om de träffas och om de sänks
class Spelplan:
    def __init__(self):
        #self.plan = [[" "," "," "],[" "," "," "],[" "," "," "]]
        #self.plan = [["A","A","A"],["B","B","B"],["C","C","C"]]
        self.plan = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]] # liten plan
        self.flotta = []
        self.ABC = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10} # OBS!!!
        self.onetwothree = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K"}
                                                # ABC ska användas för at kunna slå in rätt kordinater(y,x) i framtiden
    def visa_plan(self):
# Visar upp spelplanen med eventuella båtar och tidigare skjutningar 
        rad_numrering = 1 
        print("  ",end="")
        for rad in range(len(self.plan)):
            print(f'{self.onetwothree[rad]}', end=" ")  # skriver ut kolumnbokstav, se upp för offseten!  
        print("")
        for rad in self.plan:
            print(rad_numrering, end ="")               # skriver ut radnumrering
            rad_numrering += 1
            print("", end="|")
            for place in rad: 
                print(place, end="|")
            print("")

    def skapa_båt(self,längd,plats, höger = True):
# tar in :
#   - längd på båt
#   - coordinat för första position
#   - riktning på fartyget (True = höger, False = ner)
# kontrollerar om båtens önskade position är utanför spelplanen eller gå på en annan befintlig båt
# lägger in båtens hitbox i self.flotta
# lägger in "O" på self.plan för att repressentera var fartyget ligger på slagfältet
# 
        ner = not(höger)
        båt = []
        längd -= 1
        # kollar om båten får plats på spelplanen
        print(f'längd -1 på båten är {längd}')
        print(f'längden på planen är {len(self.plan)}')
        if plats[0]+längd*ner < len(self.plan) and plats[1]+längd*höger < len(self.plan[0]):
            while längd >= 0:
                if self.plan[plats[0]+längd*ner][plats[1]+längd*höger] == " ":
                    print("Du har kommit till rätt ställe för att bygga en båt :) ")
                    båt = båt + [(plats[0]+längd*ner,plats[1]+längd*höger)]
                    längd -= 1 
                else:
                    print("båten är lagd på en annan båt")
                    print(self.plan[plats[0]+längd*ner][1])
                    print(self.plan)
                    return False
            for i in båt:
                self.plan[i[0]][i[1]] = "O"
        else:
            print("båten får inte plats på spelplanen")
            return False
        
        self.flotta.append(båt)
        # print(båt)
        return True

    def skjut(self,plats): # OBS! hade gärna hjälpt idioter som skjuter på samma ställe
# tar in :
#   -   positionsdata y och x position 
# Träffar på båtar ersätter "O" med "X"
#  Missar av båtar ersätter " " med "x" 
# Skott på tidigare position ger meddelande om att användaren redan skjutit där
# Förbätring: Kan ge användaren en chans till om man skjuter på samma ställer
# (kan vara bra för datorn)
        # tanken är att skott ska ge "X" och en miss ska ge "x"
        if self.plan[plats[0]][plats[1]] == "-" or self.plan[plats[0]][plats[1]] == "X":
            print("Du har redan skjutit här")
        if self.plan[plats[0]][plats[1]] == "O":
            self.plan[plats[0]][plats[1]] = "X"
            # OBS!!!! jag hade velat kalla på sänkcheck här men det verkar inte gå i 
        if self.plan[plats[0]][plats[1]] == " ":
            self.plan[plats[0]][plats[1]] = "-"
        Spelplan.sänk_check(self)
        
    def sänk_check(self):# är skeppet sänkt? OM ja, ta bort båt och returnera True

#       self.flotta = []
        number_of_ships = -1
        for status in self.flotta:
            båt_längd = len(status)
            träffar = 0
            number_of_ships += 1
            print(len(status))
            for test in status:
                if self.plan[test[0]][test[1]] != "X":
                    break
                träffar += 1
                if träffar == båt_längd:
                    print(self.flotta)
                    del self.flotta[number_of_ships]
                    print("BOOOM Sänkt båt!")
                    print(self.flotta)
                    return True
    #def win_check(self):
        #   check if self flotta är tom och avsluta då spel med pompa och ståt
        #   OBS! får inte köras innan flotan är tillagd 

    
        
spelare1 = Spelplan()
spelare1.visa_plan()
spelare1.skapa_båt(2,(1,0),False)
spelare1.skapa_båt(2,(1,0),False)
spelare1.visa_plan()
spelare1.skapa_båt(2,(2,1),False)
spelare1.visa_plan()
spelare1.skjut((0,0)) 
spelare1.visa_plan()
spelare1.skjut((1,0))
spelare1.visa_plan()
spelare1.skjut((2,0))
spelare1.visa_plan()
spelare1.visa_plan()
###################################       hur går en omgång till      ####################################