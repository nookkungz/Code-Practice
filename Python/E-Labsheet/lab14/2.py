

def cloth_size(width_list):
    result = {'S': 0, 'M': 0, 'L': 0}
    for width in width_list:
        if width <= 36:
            result["S"] += 1
        elif width >= 37 and width <= 44 :
            result["M"] += 1
        else :
            result["L"] += 1
    return result

        
print(cloth_size([50, 44, 40, 48]))