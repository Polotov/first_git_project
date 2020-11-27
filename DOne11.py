with open("database.txt") as file1:
    ban = "ban_word"+"\n"
    check_ban = ""
    streamer_words = file1.readlines()
    i = 0
    while i < len(streamer_words):
        if streamer_words[i] == ban:
            check_ban = streamer_words[i]
            print(streamer_words[i],streamer_words.index(streamer_words[i])+1)
        i += 1
    if check_ban in streamer_words:
        print("naideno")
    else:
        print("ok")