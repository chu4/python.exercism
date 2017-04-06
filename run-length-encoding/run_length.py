def encode(txt):
    n=1
    i=0
    outp = ""
    while i < len(txt):
        if txt[i]==" ":
            outp += " "
        elif i+1 ==len(txt):
            if txt[i]==txt[i-1]:
                outp += str(n) + txt[i]
            elif txt[i]!=txt[i-1]:
                outp += txt[i]
        elif txt[i]==txt[i+1]:
            n+=1
        elif txt[i]!=txt[i+1]:
            if n==1:
                outp+=txt[i]
            elif n!=1:
                outp+=str(n)+txt[i]
                n=1
        i+=1
    return outp

def decode(txt):
    outp = ""
    i = 0
    while i <len(txt):
        if txt[i].isdigit():
            if txt[i+1].isdigit():
                z = int(txt[i]+txt[i+1])
                outp+=txt[i+2]*z
                i+=3
            else:
                outp+=txt[i+1]*int(txt[i])
                i+=2
        else:
            outp+=txt[i]
            i+=1
    return outp

print(encode('hello00000 7777'))
print(decode('he2lo5047'))
