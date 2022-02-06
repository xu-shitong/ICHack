def text_to_filepaths(speech):
    speech = speech.replace('.',' pause')
    list_of_filepaths = speech.split()
    for word in list_of_filepaths:
        if word != "pause":
            word = word+".wav"
        print(word)
    return list_of_filepaths

def main():
    text_to_filepaths("I declare that history is deeply incredible.")

if __name__ == "__main__":
    main()