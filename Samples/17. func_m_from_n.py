def factoriel(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def m_from_n(m,n):
    p=factoriel(n)/(factoriel(m)*factoriel(n-m))
    return p
