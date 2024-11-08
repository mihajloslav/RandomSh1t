
A : list[int] = [236, 214, 156, 116, -284, 66, 12, -184, 50, 162, 250, 88, -288, 208, 154, -64, 190, -280, -188, -32, 168, 296, 58, -284, -232, 274, 120, 212, -104, 204, -170, 230, 166, 74, 244, -236, -206, -288, 224, -242, -86, 74, 210, 278, -114, -244, 270, -10, 2, -40, -134, 78, -170, -152, 74, 142, 158, 288, -128, -154, -228, 44, 282, -80, -142, 100, -82, -158, -288, -42, -80, -38, 260, -236, -286, -4, -164, -268, -240, 292, -210, 170, -66, 48, -198, 24, -260, 218, -94, -110, -256, 194, 54, -34, 126, -262, -292, 72, 108, -98, 104, 30, -74, -80, 76, 284, 192, -184, -180, -92, -284, 66, 176, 150, 198, -266, -110, 18, -286, -258, 22, -144, 246, 80, 152, -234, 148, 198, 274, 220, -158, -76, 40, 136, 142, 18, 170, -144, -56, -112, 208, -200, -126, -4, -106, 14, -94, -28, 196, 178, 70, -204, 202, 288, 240, 52, -270, -236, -58, -226, 48, 142, 266, 90, -286, -190, -72, 204, 194, 112, 20, 54, -60, -176, -146, -242, -134, 294, 86, -108, 228, -138, -78, -88, -188, -54, -46, 164, 58, -250, 136, 32, -90, -38, 288, -102, 280, 278, -214, -232, -166, 40, 142, -294, -72, -290, -4, -82, 84, 4, 208, 154, 146, -28, 62, -194, -68, -282, -66, 154, -224, -96, 150, 64, -86, 226, 260, -26, 44, 264, -180, -70, 128, 240, 234, -96, -254, -208, 20, 28, -114, 64, 180, -6, 16, -234, -222, 292, 38, -182, 96, 242, 132, 96, 284, -80, -52, 160, 262, -112, 16, -116, 26, -220, 42, 230, -60, -64, -24, 274, -32, -248, 268, 118, -62, 258, -24, -118, 232, -284, -10, 268, -168, -250, -286, 22, -76, -200, -72, 178, 216, 252, -278, -220, 122, 222, -146, 184, -160, -248, 248, 246, 66, 98, -160, 174, 60, 272, 198, 256, 174, -140, -158, -130, 276, 168, 240, -148, -192, 28, 6, 38, -44, -90, -150, 204, 284, 114, 188, 286, 182, 50, 94, -124, 246, -88, 248, -162, 262, -140, 218, -222, 82, 66, -270, 36, -64, 112, 152, -70, 138, -262, -116, 8, -290, -236, -156, -164, 56, -100, -120, -274, 264, -130, 110, -230, -68, 256, 102, -56, -178, -76, -224, -240, 138, 100, 222, -234, -136, 92, 200, -146, -186, -82, 208, 254, -46, 268, 68, 92, -22, -260, 162, 106, -132, -288, -74, -2, 126, 46, -252, 44, 278, 10, -126, -44, -128, -280, -292, -174, -264, -234, -126, 42, -14, -276, -118, 190, -298, 110, -240, -280, 34, 186, -196, 178, -224, -84, -296, 216, 226, -144, -172, -172, -16, 226, -218, -164, -278, -266, -202, -292, 232, 182, 64, -144, 6, -36, -248, -220, 158, -194, -272, 276, 226, -274, -216, 140, 188, 202, -92, -118, -268, -82, 134, 132, 0, -8, 238, 90, -242, 26, 144, -32, -136, 134, 26, 290, 28, -178, -212, 26, 130, -118, -66, 26, 120, 230, 158, -122, 172, 258, 160, -242, 140, -88, -32, 12, -10, 258, 190, 54, -168, -100, -36, 68, -238, -42, -196, -30, 78, 280, -252, -20, -272, 206, 236, -218, 102, -120, -18, 144, -6, 14, -48, -60, 176, 152, -232, 244, 124, -230, 222, -50, 116, 280, -214, -126, 232, 276, -246, -246, -16, -190, 0, 138, 126, -268, 166, 282, 198, -12, 176, 222]
#----------------------------------------------------------
def postoji(niz : list[int], element : int) -> bool:
    brojac : int = 0
    for i in niz:
        if i == element:
            brojac += 1
    return True if brojac > 1 else False

def jedinstveniElementi(niz : list[int]) -> None:
    brojac : int = 0
    for i in niz:
        if not postoji(niz , i):
            #print(i)
            brojac += 1
    print("Jedinstveni broj elemenata u nizu A:", brojac)
#----------------------------------------------------------

#----------------------------------------------------------
def jedinstveniElementi2(niz: list[int]) -> None:
    jedinstveni : set = set(niz) 
    brojac : int = 0
    for i in jedinstveni:
        if niz.count(i) == 1:
            #print(element)
            brojac += 1
    print("Jedinstveni broj elemenata u nizu A:", brojac)
#----------------------------------------------------------

#----------------------------------------------------------
print("--------------------------------------")
print("Ukupno ima", len(A), "elemenata.")
jedinstveniElementi(A)
jedinstveniElementi2(A)
print("--------------------------------------")
#----------------------------------------------------------