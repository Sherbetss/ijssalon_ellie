from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):

  return prijs * (1 - korting)
  korting_bedrag = prijs * korting
  prijs_met_korting = prijs - korting_bedrag
  return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_met_korting:.2f} euro."

print(aanbieding_1("aardbei", 4, 0.1))
def inkomsten_totaal(inkomsten, btw=0):

  totaal = sum(inkomsten)
  bedrag = totaal * btw
  return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):

  return [min(mijn_lijst), max(mijn_lijst)]

# Voorbeeldgebruik
print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):

  totaal = sum(mijn_lijst)
  gemiddelde_inkomsten = totaal / len(mijn_lijst)
  return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."

def meervoudig(invoer_lijst):
 
  hoogste_waarde = max(invoer_lijst)
  laagste_waarde = min(invoer_lijst)
  return [hoogste_waarde, laagste_waarde]

def combinatie(invoer_lijst_2):

  from algemene_functies import mijn_functie_2
  korte_lijst = meervoudig(invoer_lijst_2)
  return mijn_functie_2(korte_lijst)