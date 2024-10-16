def extract_atom(formula) :
    result = {}
    st , num = "" , ""
    st = formula[0]
    for i in range(1 , len(formula)) :
        ch = formula[i]
        if ch.isalpha():
            if ch.isupper() :
                if num == "" :
                    num = "1"
                result[st] = num
                st , num == ch, ""
                
            else :
                st += ch
        else :
            num += "1"
    if num = '' :
        num = "1"
    result[st] = num
    return result



formula = input()
atom = input()
atoms = extract_atom(formula)
print(atoms.get(atom, 0))