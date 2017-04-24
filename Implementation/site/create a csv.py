import csv





##somedict = dict{NextDay=forecast_set[0],3rdDay=forecast_set[1],5thDay=forecast_set[2]}

somedict = dict(NextDay='red',ThirdDay='bl',FifthDay='gg')


##somedict = dict(raymond='red', rachel='blue', matthew='green')
with open('mycsvfile.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(somedict.items())




##keys = toCSV[0].keys()



##toCSV = [{'name':'bob','age':25,'weight':200},
##         {'name':'jim','age':31,'weight':180}]
##with open('people.csv', 'wb') as output_file:
##    dict_writer = csv.DictWriter(output_file, keys)
##    dict_writer.writeheader()
##    dict_writer.writerows(toCSV)
##
##toCSV = {'phy':50,'che':60,'maths':70}
