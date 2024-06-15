def presenteer(invoer_dict, totaal):
    for key, value in invoer_dict.items():
        print(f"{key}-totaal: {value} euro")
    print(f"Totaal: {totaal} euro")

mijn_dict = {'Aardbeien-ijs-totaal' : 1000, 'Vanille-ijs-totaal' : 2000, 'Chocolade-ijs-totaal' : 1500, 'Waterijsjes-totaal' : 750}

inkomsten_totaal = 5250