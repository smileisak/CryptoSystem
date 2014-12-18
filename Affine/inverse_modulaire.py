#!/usr/bin/env python2.7
# -*- coding: cp1252 *-
     
def pgcd(a,modulo,pgcd):
    c,d=max(a,modulo),min(a,modulo)   # détermination du Dividende et du diviseur
    while d>0:
        c,d=d,c%d
    pgcd = c
    return pgcd
     


def inverse_mod(a,modulo):
    #a,modulo=1572,5441
    npgcd=pgcd(a,modulo,1)
     
    if npgcd != 1:
        print "Désolé, votre nombre et le modulo ne sont pas premiers entre eux."
        print "Sélectionner un autre couple de valeurs."
    else:
        k=int(modulo/a)+1
        mo=1
        while mo != 0:
            k += 1
            mo = (1 + modulo * k) % a
        res = ((1+modulo*k)/a)%modulo
        print "L'inverse de",a,"modulo",modulo,"est :", res
        return res


