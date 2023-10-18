def extraire_mots(phrase):
    mots = phrase.split()
    return mots

phrase = input("Entrez une phrase : ")
mots = extraire_mots(phrase)
print("Les mots de la phrase sont :", mots)
