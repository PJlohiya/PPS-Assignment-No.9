def casecounter(a):
    caps=0
    smalls=0
    for i in a:
               if i.isupper():
                              caps=caps+1
               elif i.islower():
                              smalls=smalls+1

    print("Caps:"+str(caps))
    print("Smalls:"+str(smalls))

print("Input string:")
a=input()
casecounter(a)