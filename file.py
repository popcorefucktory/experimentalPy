fw = open('sample.txt', 'w')            # буква w говорит, что в файле надо написать текст
fw.write('Some text\n')                 # n - чтобы перейти на другую строку
fw.write('Second text\n')
fw.close()

fr = open('sample.txt', 'r')            # r значит, что мы хотим прочитать файл
text = fr.read()
print(text)
fr.close()
