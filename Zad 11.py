def compare(array1,array2):
    if len(array1)==len(array2):
        for index in range(len(array1)):
                if not array1[index]== array2[index]:
                    return False
                
        return True
    else:
        return False
arrayA1 = ["water","book","sky"]   
arrayA2 = ["water","book","sky"]
print(f"Array1: {arrayA1}")
print(f"Array2: {arrayA2}")
comparison = compare(arrayA1,arrayA2)