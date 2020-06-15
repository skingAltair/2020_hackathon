import datetime

def main():
    #get current day
    d = datetime.datetime.now()
    d = str(d)

    #parse to get month and day
    day = (d.split(" ")[0]).split("-", 1)[1]
    month = day.split("-")[0]
    
    #create dictionary from file of holidays and emoji's
    emojiDict = {"06-17":{"\U0001F966" : "Eat Your Vegetables Day"}, "06-18":{"\U0001F363" : "International Sushi Day"}}

    #create dictionary of months with corresponding season
    seasonDict = {"01":"\U00002744","02":"\U00002744","12":"\U00002744", "03":"\U0001F33B", "04":"\U0001F33B", "05":"\U0001F33B", "06":"\U0001F3D6", "07":"\U0001F3D6", "08":"\U0001F3D6", "09":"\U0001F342", "10":"\U0001F342", "11":"\U0001F342"} 


    #Check to see if day in in the dictionary. if so, return emoji and corresponding description. 
    # if not, search season dictionary and assign seasonal emoji
    if day in emojiDict.keys():
        e = emojiDict[day]
        for i,j in e.items():
            emoji = i
            description = j
    elif month in seasonDict.keys():
        emoji = seasonDict[month]
        description = ""
    print(emoji,description)
    return (emoji)

if __name__ == '__main__':
    main()