sentence=input('ingrese una oracion')
handlervocals=0
for words in sentence:
    match words:
      case 'a':
        handlervocals+=1
for words in sentence:
    match words:
      case 'e':
        handlervocals+=1
for words in sentence:
    match words:
     case 'i':
        handlervocals+=1
for words in sentence:
    match words:
     case 'o':
        handlervocals+=1
for words in sentence:
    match words:
     case 'u':
        handlervocals+=1
        print('la cantidad de vocales es ', handlervocals)
    