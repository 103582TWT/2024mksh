# p09_list_for
names = ['Ratri', 'Jane', 'Tim'] #list陣列
for name in names:
    print(name)
background(10, 10, 100)
size(300, 300)
for i in range(len(names)):
    text(names[i], i*100, 100)
