from collections import defaultdict
#from collections import Counter
#нужно в выводе убрать символ перевода строки
# функция проверяет порядок индексов, создает словарь с повторяющимися блоками, пока только по 2 фразы
def repeatFunc (dictionary, indexes, phrase):
    followingStrings = defaultdict(list)
    for checkedPhrase in dictionary.keys():
        checkedIndexes = dictionary[checkedPhrase]
        for checkedIndex in checkedIndexes:
            if checkedIndex-1 in indexes:
                paragraph = phrase + " " + checkedPhrase
                followingStrings[paragraph].append(paragraph)
        repeatings = dict((k,v) for k,v in followingStrings.items() if len(v) >1)
    return repeatings

dictOfIndexes = defaultdict(list)
filename = 'v.txt'
fileDict = {}
i=0
#зачитываем файл в список
with open(filename) as file_object:
    fileList = file_object.readlines()
#создаем словарь из списка строк и номеров строк
for line in fileList:
# вывод любых дублирующихся строк
#    if line in fileDict.values():
#       print ("Duplicate: " + line)
    fileDict[i]=line
    i=i+1
# вывод всех упорядоченных строк и их номеров
for keyDict in sorted(fileDict.keys()):
    print (keyDict, fileDict[keyDict])
print ("----")
#создаем словарь, в котором ключи - это фразы, а соотв. значения - это номера строк
for index in range (0,i):
    key, value = fileDict[index], index
    dictOfIndexes[key].append(value)
#вызов функции repeatFunc для словаря dictOfIndexes
for index in dictOfIndexes.keys():
    if len(dictOfIndexes[index])>1:
        a=dictOfIndexes[index]
        b=index
        result = repeatFunc(dictOfIndexes,a,b)
        print (result)


