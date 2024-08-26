import time 
import os

#data set siswa 
data_siswa = [
    [
        {'A':[
            {'laki-laki':[
                'Hasan Sanusi','Robi Ahmad','Robet Kusmana','Tatang Banzeer','Yasmin Tabilah','Nur Rahman Saqila','Tanjuniaga'
            ]},
            {'perempuan':[
                'Siti Aminah Sari','Susanti','Ratna Sari','Kusuma Putri','Angelia Cecil','Xavier Sanchez','Shakira','Sabania'
            ]}
        ]}
    ],
    [
        {'B':[
            {'laki-laki':[
                'Muhamad Akmal','Rifqi Sakil','Ivan Mintara','Aldo Rahim','Saep Nur Hasan','Fahreza Mulana','Samsul'
            ]},
            {'perempuan':[
                'Nunung Permana','Sabila','Nabila Putri','Tri Dewi','Mutia Siti Rahma','Salina Sari'
            ]}
        ]}
    ],
    [
        {'C':[
            {'laki-laki':[
                'Juhari','Samsir alim','Maulana','Satria','Nabil','Hasbi Nalia','Suhadat Musila','Lukman Maulana'
            ]},
            {'perempuan':[
                'Rahma Sari','Ananda Oktiana','Oktavia Sari','Indah Dewi','Salmania Asri','Sari Hasanah','Maulida Asnawi'
            ]}
        ]}
    ],
]


# function to clear any content on terminal
def clear_command():
    os.system('clear')


# function for list of class
def daftar_kelas():
    list_kelas = []
    for i in data_siswa:
        for x in i:
            for j in x:
                list_kelas.append(j)
    
    list_kelas.sort()
    print('Daftar Kelas Tersedia:')
    for i in list_kelas:
        print(f'Kelas {i}')



# function for call all students list in every class
def all_students(all_name_students):
    list_of_women = []
    list_of_man = []
    list_of_all = []
    for i in data_siswa:
        for x in i:
            for j in x:
                for all in x[j]:
                    for gender in all:
                        if(all_name_students == 1):
                            for all_gender in all[gender]:
                                list_of_all.append(all_gender)
                        elif(all_name_students == 2 and gender == 'perempuan'):
                            for women in all[gender]:
                                list_of_women.append(women)
                        elif(all_name_students == 3 and gender == 'laki-laki'):
                            for man in all[gender]:
                                list_of_man.append(man)
                        else:
                            break
    
    if(all_name_students == 1):
        list_of_all.sort()
        print('\nDaftar Semua Murid:')
        for index, name in enumerate(list_of_all):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(list_of_all)} Murid ')
    elif(all_name_students ==2):
        list_of_women.sort()
        print('\nDaftar Semua Siswi:')
        for index, name in enumerate(list_of_women):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(list_of_women)} Siswi')
    elif(all_name_students ==3):
        list_of_man.sort()
        print('\nDaftar Semua Siswa')
        for index, name in enumerate(list_of_man):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(list_of_man)} Siswa')




# Function for list of Student in A Class
def kelas_A(validation_A):
    semua_murid = []
    siswi_A = []
    siswa_A = []
    
    for i in data_siswa:
        for x in i:
            for j in x:
                if (j == 'A'):
                    for all_A in x[j]:
                        for gender in all_A:

                            if (validation_A == 1):
                                for all_gender in all_A[gender]:
                                    semua_murid.append(all_gender)
                            elif(validation_A == 2 and gender== 'perempuan'):
                                for women in all_A[gender]:
                                    siswi_A.append(women)
                            elif(validation_A == 3 and gender =='laki-laki'):
                                for man in all_A[gender]:
                                    siswa_A.append(man)
                            else:
                                break
    

    if(validation_A == 1):
        semua_murid.sort()
        print('\nDaftar Semua Murid Kelas A:')
        for index, name in enumerate(semua_murid):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(semua_murid)} Murid')
    elif(validation_A == 2):
        siswi_A.sort()
        print('\nDaftar Siswi Kelas A:')
        for index, name in enumerate(siswi_A):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswi_A)} Siswi')
    elif(validation_A == 3):
        siswa_A.sort()
        print('\nDaftar Siswa Kelas A:')
        for index, name in enumerate(siswa_A):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswa_A)} Siswa')
    else:
        exit()




# Function for list of Student in B Class
def kelas_B(validation_B):
    semua_murid = []
    siswi_B = []
    siswa_B = []
    
    for i in data_siswa:
        for x in i:
            for j in x:
                if (j == 'B'):
                    for all_B in x[j]:
                        for gender in all_B:

                            if (validation_B == 1):
                                for all_gender in all_B[gender]:
                                    semua_murid.append(all_gender)
                            elif(validation_B == 2 and gender== 'perempuan'):
                                for women in all_B[gender]:
                                    siswi_B.append(women)
                            elif(validation_B == 3 and gender =='laki-laki'):
                                for man in all_B[gender]:
                                    siswa_B.append(man)
                            else:
                                break
    

    if(validation_B == 1):
        semua_murid.sort()
        print('\nDaftar Semua Murid Kelas B:')
        for index, name in enumerate(semua_murid):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(semua_murid)} Murid')
    elif(validation_B == 2):
        siswi_B.sort()
        print('\nDaftar Siswi Kelas B:')
        for index, name in enumerate(siswi_B):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswi_B)} Siswi')
    elif(validation_B == 3):
        siswa_B.sort()
        print('\nDaftar Siswa Kelas B:')
        for index, name in enumerate(siswa_B):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswa_B)} Siswa')
    else:
        exit()




# Function for list of Student in C Class
def kelas_C(validation_C):
    semua_murid = []
    siswi_C = []
    siswa_C = []
    
    for i in data_siswa:
        for x in i:
            for j in x:
                if (j == 'C'):
                    for all_C in x[j]:
                        for gender in all_C:

                            if (validation_C == 1):
                                for all_gender in all_C[gender]:
                                    semua_murid.append(all_gender)
                            elif(validation_C == 2 and gender== 'perempuan'):
                                for women in all_C[gender]:
                                    siswi_C.append(women)
                            elif(validation_C == 3 and gender =='laki-laki'):
                                for man in all_C[gender]:
                                    siswa_C.append(man)
                            else:
                                break
    

    if(validation_C == 1):
        semua_murid.sort()
        print('\nDaftar Semua Murid Kelas C:')
        for index, name in enumerate(semua_murid):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(semua_murid)} Murid')
    elif(validation_C == 2):
        siswi_C.sort()
        print('\nDaftar Siswi Kelas C:')
        for index, name in enumerate(siswi_C):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswi_C)} Siswi')
    elif(validation_C == 3):
        siswa_C.sort()
        print('\nDaftar Siswa Kelas C:')
        for index, name in enumerate(siswa_C):
            time.sleep(0.2)
            print(f'{index}. {name}')
        time.sleep(1)
        print(f'\nTotal: {len(siswa_C)} Siswa')
    else:
        exit()



# main function to print out the menu of list students
def main():
    while True:
        print('='*12 + ' Selamat Datang di Menu Daftar Siswa '+ '='*12)
        try:
            main_validation = int(input('\nSilakan pilih daftar menu di bawah ini:\n1. Daftar Kelas\n2. Daftar Semua Siswa\n3. Keluar\n\nEnter your input: '))  
            if (main_validation == 1):
                time.sleep(0.5)
                clear_command()
                daftar_kelas()
                time.sleep(1)
                validation_to_next_dk = input('\nApa kamu ingin melanjutkan[Y/n]: ')
                if (validation_to_next_dk.lower() == 'y'):
                    time.sleep(1)
                    clear_command()
                    next_to_each_class = int(input('Pilih Kelas:\n1. Kelas A\n2. Kelas B\n3. Kelas C\nKetik sembarang untuk keluar\n\nEnter your input: '))
                    if(next_to_each_class == 1):
                        time.sleep(1)
                        clear_command()
                        validation_A = int(input('Pilih daftar nama berdasarkan gender:\n1. Semua Murid Kelas A\n2. Perempuan\n3. Laki-laki\nKetik sembarang untuk keluar\n\nEnter your input: '))
                        time.sleep(1)
                        clear_command()
                        kelas_A(validation_A)
                        time.sleep(1)
                        validation_to_next = input('Apa kamu ingin keluar[Y/n]: ')
                        if (validation_to_next.lower() == 'y'):
                            print('Kamu akan keluar...')
                            time.sleep(2)
                            clear_command()
                            exit()
                        else:
                            print('Anda akan di alihkan ke menu utama...')
                            time.sleep(2)
                            clear_command()
                            continue
                    elif(next_to_each_class ==2):
                        time.sleep(1)
                        clear_command()
                        validation_B = int(input('Pilih daftar nama berdasarkan gender:\n1. Semua Murid Kelas B\n2. Perempuan\n3. Laki-laki\nKetik sembarang untuk keluar\n\nEnter your input: '))
                        time.sleep(1)
                        clear_command()
                        kelas_B(validation_B)
                        validation_to_next = input('Apa kamu ingin keluar[Y/n]: ')
                        if (validation_to_next.lower() == 'y'):
                            print('Kamu akan keluar...')
                            time.sleep(2)
                            clear_command()
                            exit()
                        else:
                            print('Anda akan di alihkan ke menu utama...')
                            time.sleep(2)
                            clear_command()
                            continue
                    elif(next_to_each_class == 3):
                        time.sleep(1)
                        clear_command()
                        validation_C = int(input('Pilih daftar nama berdasarkan gender:\n1. Semua Murid Kelas C\n2. Perempuan\n3. Laki-laki\nKetik sembarang untuk keluar\n\nEnter your input: '))
                        time.sleep(1)
                        clear_command()
                        kelas_C(validation_C)
                        validation_to_next = input('Apa kamu ingin keluar[Y/n]: ')
                        if (validation_to_next.lower() == 'y'):
                            print('Kamu akan keluar...')
                            time.sleep(2)
                            clear_command()
                            exit()
                        else:
                            print('Anda akan di alihkan ke menu utama...')
                            time.sleep(2)
                            clear_command()
                            continue
                    else:
                        print('Kamu akan keluar...')
                        time.sleep(2)
                        clear_command()
                        exit()
                else:
                    print('Kamu akan keluar...')
                    time.sleep(2)
                    clear_command()
                    exit()
            elif(main_validation == 2):
                time.sleep(1)
                clear_command()
                all_name_students = int(input('Pilih daftar nama berdasakan gender:\n1. Semua Murid\n2. Perempuan\n3. Laki-laki\nKetik sembarang untuk keluar\n\nEnter your input: '))
                time.sleep(1)
                clear_command()
                all_students(all_name_students)
                time.sleep(1)
                next_all_students = input('Apa kamu ingin keluar[Y/n]: ')
                if (next_all_students.lower() == 'y'):
                    print('Kamu akan keluar...')
                    time.sleep(2)
                    clear_command()
                    exit()
                else:
                    print('Anda akan di alihkan ke menu utama...')
                    time.sleep(2)
                    clear_command()
                    continue
            else:
                print('Kamu akan keluar...')
                time.sleep(2)
                clear_command()
                exit()
        except:
            print('Kamu akan keluar..')
            time.sleep(2)
            clear_command()
            exit()
            
            
            
            
            
            

            
if __name__ == "__main__":
    main()
