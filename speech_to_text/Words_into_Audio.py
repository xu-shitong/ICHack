def text_to_filepaths(speech):
    speech = speech.replace('.',' pause')
<<<<<<< HEAD
    list_of_words = speech.split()
    list_of_filepaths = []
    for word in list_of_words:
        if word != "pause" :
            list_of_filepaths.append("./words/"+word+".wav")
=======
    list_of_filepaths = speech.split()
    for word in list_of_filepaths:
        if word != "pause":
            word = word+".wav"
>>>>>>> f7c2d77a99c9b1bb2c1ff7c617d01c1508e7457c
        print(word)
    return list_of_filepaths

def main():
    text_to_filepaths("I declare that history is deeply incredible.")

if __name__ == "__main__":
    main()