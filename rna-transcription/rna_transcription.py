def to_rna(text):
    new=''
    for char in text:
        if char == 'G':
            new+='C'
        elif char =='C':
            new+='G'
        elif char =='T':
            new +='A'
        elif char =='A':
            new +='U'
    return (new)