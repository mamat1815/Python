# sisi kubus
sisi_1 = 4
sisi_2 = 5
sisi_3 = 7

#fungsi menghitung dan print luas
def luas(sisi):
    return 6*sisi**2

def printLuas(sisi):
    print("Luas kubus dengan sisi ",sisi,"yaitu: ",luas(sisi))

#fungsi menghitung dan print volume
def volume(sisi):
    return sisi*sisi*sisi

def printVolume(sisi):
    print("Volume kubus dengan sisi ",sisi,"yaitu: ",volume(sisi))
    
printLuas(sisi_1)
printLuas(sisi_2)
printLuas(sisi_3)
print("")
printVolume(sisi_1)
printVolume(sisi_2)
printVolume(sisi_3)

