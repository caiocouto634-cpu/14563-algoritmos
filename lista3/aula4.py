pal=input("agora digite uma palavra: ")
pal2=input("agora digite a segunda palavra: ")
if len(pal)>len(pal2):
    print("a primeira palavra tem mais caracteres com um total de ", len(pal), "caracteres")
if len(pal)<=len(pal2):
    print("a segunda palavra tem mais caracteres com um total de ", len(pal2), "caracteres")
else:
    print("as duas palavras são iguais om um total de ", len(pal), "caracteres")