India={
    "Rajasthan": ['Jaipur', 'Jodhpur', 'Ajmer'],
    "West_Bengal" : ['Calcutta', 'Midnapur', 'Siliguri']
}

    
for key,value in India.items():
    print(f"\nCities in {key} are:")
    for v in value:
        print(v)