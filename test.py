def generatorNumber(count):
    arr = [];
    
    for i in range(1, count + 1):
        arr.append(i);
        
    return arr;

print(generatorNumber(5))