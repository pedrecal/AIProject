import csv

def load_cases():
    attributes = [] #Attributes Array
    results = [] #Cancer Results Array(Normal = 0 // Cancer = 1 // Benign = 2)

    datafile = open('data_reduced.csv', 'rb')
    reader = csv.reader(datafile)

    reader.next()

    for Case, Contraste, Correlacao, Variancia_Diferenca, Diagnostico in reader:

        data_attrib = [int(Case),float(Contraste),float(Correlacao),float(Variancia_Diferenca)]
        attributes.append(data_attrib)
        results.append(int(Diagnostico))

    return attributes, results
