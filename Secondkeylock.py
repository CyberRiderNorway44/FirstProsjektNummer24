# My super secret program

cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vow = ['a', 'e', 'i', 'o', 'u']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

TheKeyPart2 = cons[15] + cons[5] + num[1] + cons[13] + cons[2]
TheKeyPart4 = num[1] + cons[14]
TheKeyPart1 = cons[15] + cons[5] + num[3]
TheKeyPart5 = cons[14] + num[3] + cons[16] + num[3] + cons[10]
TheKeyPart3 = cons[10] + vow[4] + cons[9] + cons[0] + num[3] + cons[13]

spacey = " "

KeyNumber = TheKeyPart1 + spacey + TheKeyPart2 + spacey + TheKeyPart3 + spacey + TheKeyPart4 + spacey + TheKeyPart5

