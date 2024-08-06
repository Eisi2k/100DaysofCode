def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    name1 = name1 + name2
    count_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
    count_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
    love = int(str(count_true) + str(count_love))
    print(f"{love}")
    
    
calculate_love_score("Kanye West", "Kim Kardashian")