#Industreis of diffrent sectors
Industries = [
    ["Mining", "Timber", "Agriculture"],
    ["Construction", "Steel plant", "Rice mill"],
    ["Telecom centre", "Malls", "Stock Market"]
]

#headings for each sector
headings = ["Primary industries", "Secondary Industries","Tertiary Industries" ]
for headings, sector in zip(headings,Industries):
    print(headings + ":")
    for item in sector:
        print(item)
    print()    
   