def namelist(names):
    if not names:
        return ''
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return ' & '.join(names)
    else:
        return ', '.join(names[:-1]) + ' & ' + names[-1]