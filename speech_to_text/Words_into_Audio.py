def text_to_filepaths(speech):
    speech = speech.replace('.',' pause')
    list_of_words = speech.split()
    list_of_filepaths = []
    for word in list_of_words:
        if word != "pause" :
            list_of_filepaths.append("./words/"+word+".wav")
        print(word)
    return list_of_filepaths

def main():
    text_to_filepaths("I declare that history is deeply incredible.")

if __name__ == "__main__":
    main()