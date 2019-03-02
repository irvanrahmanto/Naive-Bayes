import csv
import math
import sys

# Pendeklarasian sebuah Array pada program
Arrtrain = []
Arrtest = [] 

# Pemanggilan training set pada file nya

# pendeklarasian readme sebagai variabel mewakilkan csv yang dikenali sebagai readme_train
with open("TrainsetTugas1ML.csv") as readme_train:

    # pendeklarasian readtrain sebagai variabel mewakilkan file
    readtrain = csv.reader(readme_train, delimiter=',')

    #Agar me-next baris/record paling atas ke baris selanjutnya 
    next(readtrain)

    # masuk pada perulangan variabel i pada file readtrain dan pemasukan variabel i ditiap label index nya pada array
    for i in readtrain:
        Arrtrain.append((i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])) #maksud append memasukan dia ke dalam 

# Function perhitungan jumlah kelas yes atau no yang akan dibanding dan tau jumlah nya berapa banyak Yes & No
def kelasProbabilitas():
    # inisialisasi 0 pada variabel yes, nope
    yes,nope=0,0

    # Perulangan akses variabel i ke dalam array train (Arrtrain)
    for i in Arrtrain:

        # Pengcekan kondisi dimana i yang sudah diakses pada Array train (Arrytrain) 
        if (i[7] == ">50K"):
            # dimana jika label income atau i[7] >50 maka Yes ditambah 1 / yes++
            yes += 1
        else:
            # dimana jika label income atau i[7] >50 maka no ditambah 1 / no++
            nope += 1
    # Perhitungan jumlah Yes pada variabel y , dimana y didapatkan dari yes / yes + no
    y = yes/(yes+nope)
    # Perhitungan jumlah no pada variabel n , dimana y didapatkan dari no / yes + no
    n = nope/(yes+nope)
    return y,n,yes,nope

# Function perhitungan label income yang >50K / Yes ditiap label pertama dari age / i[0] hingga label terakhir pada hourperweek / i[6]
def attributProbabilitasBsr50(i1,i2,i3,i4,i5,i6,i7):
    # inisialisasi tiap label atribut dengan angka 0, karena array nya harus start from zero
    age,workclass,education,marital,occupation,relationship,hoursperweek=0,0,0,0,0,0,0
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut age/pertama dengan i pada array index 0 dengan label income yang >50K
        if(i1 == i[0]) and (i[7]== ">50K"):
            age+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut workclass/kedua dengan i pada array index 1 dengan label income yang >50K
        if(i2 == i[1]) and (i[7]== ">50K"):
            workclass+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut education/ketiga dengan i pada array index 2 dengan label income yang >50K
        if(i3 == i[2]) and (i[7]== ">50K"):
            education+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut marital/keempat dengan i pada array index 3 dengan label income yang >50K
        if(i4 == i[3]) and (i[7]== ">50K"):
            marital+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut occupation/kelima dengan i pada array index 4 dengan label income yang >50K
        if(i5 == i[4]) and (i[7]== ">50K"):
            occupation+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut relationship/keenam dengan i pada array index 5 dengan label income yang >50K
        if(i6 == i[5]) and (i[7]== ">50K"):
            relationship+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut hoursperweek/ketujuh dengan i pada array index 6 dengan label income yang >50K
        if(i7 == i[6]) and (i[7]== ">50K"):
            hoursperweek+=1
    # Pengembalian nilai pada tiap atribut pada index masing-masing dikali kan dengan function kelasprobabilitas sebelum nya
    return ((age/kelasProbabilitas()[2]) * (workclass/kelasProbabilitas()[2]) * (education/kelasProbabilitas()[2]) * (marital/kelasProbabilitas()[2]) * (occupation/kelasProbabilitas()[2]) * (relationship/kelasProbabilitas()[2]) * (hoursperweek/kelasProbabilitas()[2]) * kelasProbabilitas()[0])

# Function perhitungan label income yang <=50K / Yes ditiap label pertama dari age / i[0] hingga label terakhir pada hourperweek / i[6]
def attributProbabilitasKcl50(i1,i2,i3,i4,i5,i6,i7):
    # inisialisasi tiap label atribut dengan angka 0, karena array nya harus start from zero
    age,workclass,education,marital,occupation,relationship,hoursperweek=0,0,0,0,0,0,0
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut age/pertama dengan i pada array index 0 dengan label income yang <=50K
        if(i1 == i[0]) and (i[7]== "<=50K"):
            age+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut workclass/kedua dengan i pada array index 1 dengan label income yang <=50K
        if(i2 == i[1]) and (i[7]== "<=50K"):
            workclass+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut education/ketiga dengan i pada array index 2 dengan label income yang <=50K
        if(i3 == i[2]) and (i[7]== "<=50K"):
            education+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut marital/keempat dengan i pada array index 3 dengan label income yang <=50K
        if(i4 == i[3]) and (i[7]== "<=50K"):
            marital+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut occupation/kelima dengan i pada array index 4 dengan label income yang <=50K
        if(i5 == i[4]) and (i[7]== "<=50K"):
            occupation+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut relationship/keenam dengan i pada array index 5 dengan label income yang <=50K
        if(i6 == i[5]) and (i[7]== "<=50K"):
            relationship+=1
    for i in Arrtrain:
        # Pengecekan kondisi variabel i di atiribut hoursperweek/ketujuh dengan i pada array index 6 dengan label income yang <=50K
        if(i7 == i[6]) and (i[7]== "<=50K"):
            hoursperweek+=1
    # Pengembalian nilai pada tiap atribut pada index masing-masing dikali kan dengan function kelasprobabilitas sebelum nya
    return ((age/kelasProbabilitas()[3]) * (workclass/kelasProbabilitas()[3]) * (education/kelasProbabilitas()[3]) * (marital/kelasProbabilitas()[3]) * (occupation/kelasProbabilitas()[3]) * (relationship/kelasProbabilitas()[3]) * (hoursperweek/kelasProbabilitas()[3]) * kelasProbabilitas()[1])

# Penulisan hasil output dari TestsetTugas1ML.csv ke dalam TebakanTugas1ML.csv
with open("TebakanTugas1ML.csv",'w') as f:
    writer = csv.writer(f)
    # Pemanggilan / import file TestsetTugas1ML.csv yang di kenali sebagai readme_tes
    with open("TestsetTugas1ML.csv") as readme_tes:

        # pendeklarasian readtrain sebagai variabel mewakilkan file
        readtrain = csv.reader(readme_tes, delimiter=',')

        #Agar menskip/enter baris/record paling atas ke baris selanjutnya 
        next(readtrain)

        # masuk pada perulangan variabel i pada file readtrain dan pembuatan array pada variabel Arrtrain
        for i in readtrain :
            # Pengecekan kondisi dimana jikalau function attributProbabilitasBsr50 > function attributProbabilitasKcl50 maka
            if (attributProbabilitasBsr50(i[1],i[2],i[3],i[4],i[5],i[6],i[7]) > attributProbabilitasKcl50(i[1],i[2],i[3],i[4],i[5],i[6],i[7])):
                #tuliskan >50
                f.write(">50K\n")
            else:
                #Tuliskan <=50
                f.write("<=50K\n")