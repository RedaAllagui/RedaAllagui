def yoyo(M,T,t,F,p,q,r):
    
    k=transition(T,t,F)
    bat=[0]*len(k)
    for i in range(len(k)):
        if k[i]=='P':
            bat[i]=Nombre_sinistre(M,p)
        if k[i]=='N':
            bat[i]=Nombre_sinistre(M,q)
        if k[i]=='C':
            bat[i]=Nombre_sinistre(M,r)
    return bat
