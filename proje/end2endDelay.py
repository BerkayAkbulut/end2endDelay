import os
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

mylist=np.array([])
file=open('iz.txt',"r")
lines=file.readlines()
file.close()


elements = []
print("Veri Hazırlanıyor")
for i in tqdm(range(len(lines))):
    satir=lines[i]
    satir=satir.replace(" ",",")
    values=satir.split(",")
    elements.append([])
    #print(len(values))
    for index in range(len(values)):
        elements[i].append(values[index])



seq_num=list()
added_num=list()
send_time=list()
received_time=list()

for i in range(len(elements)):
    if(elements[i][0]=='r' and elements[i][4]=='tcp'):
        if(elements[i][10] in seq_num):
            continue
        else:
            seq_num.append(elements[i][10])
            send_time.append(elements[i][1])
            print(f"{bcolors.FAIL}Gönderildi..: {elements[i]}{bcolors.ENDC}")
            time.sleep(0.00001)
            #time.sleep(0.5)
    elif(elements[i][0]=='r' and elements[i][4]=='ack'):
        if(len(send_time)==len(received_time)):
            continue
        elif(elements[i][10] in added_num):
            continue
        elif(elements[i][10] in seq_num):
            received_time.append(elements[i][1])
            added_num.append(elements[i][10])
            print(f"{bcolors.WARNING}Alındı!.....: {elements[i]}{bcolors.ENDC}")
            time.sleep(0.00001)
            #time.sleep(1.3)
    #print("Uygun değil: ", elements[i])


print(f"seq_num:{len(seq_num)}",len('seq_num')*'-',
      f"add_num:{len(added_num)}",len('added_num')*'-',
      f"send_time:{len(send_time)}",len('send_time')*'-',
      f"received_time:{len(received_time)}",len('received_time')*'-',sep='\n')

## 2. ve 3. saniyeler arasındaki veri

sonuc_2_3=0
sonuc_4_5=0
sonuc_6_7=0
sonuc_8_9=0


for i in range(len(send_time)):
    if(float(send_time[i])>2.0 and float(received_time[i])<3.0):
        sonuc_2_3=sonuc_2_3+(float(received_time[i])-float(send_time[i]))
        print(f"{bcolors.OKBLUE}İstenen aralıkta!..: {float(send_time[i])} -- {float(received_time[i])}{bcolors.ENDC}")
        time.sleep(0.01)
    elif(float(send_time[i])>4.0 and float(received_time[i])<5.0):
        sonuc_4_5 = sonuc_4_5 + (float(received_time[i]) - float(send_time[i]))
        print(f"{bcolors.OKGREEN}İstenen aralıkta!..: {float(send_time[i])} -- {float(received_time[i])}{bcolors.ENDC}")
        time.sleep(0.01)
    elif(float(send_time[i])>6.0 and float(received_time[i])<7.0):
        sonuc_6_7 = sonuc_6_7 + (float(received_time[i]) - float(send_time[i]))
        print(f"{bcolors.HEADER}İstenen aralıkta!..: {float(send_time[i])} -- {float(received_time[i])}{bcolors.ENDC}")
        time.sleep(0.01)
    elif (float(send_time[i]) > 8.0 and float(received_time[i]) <9.0):
        sonuc_8_9 = sonuc_8_9 + (float(received_time[i]) - float(send_time[i]))
        print(f"{bcolors.FAIL}İstenen aralıkta!..: {float(send_time[i])} -- {float(received_time[i])}{bcolors.ENDC}")
        time.sleep(0.01)
    else:
      #print(float(send_time[i]), " - ", float(received_time[i]))
        continue


info1=f"2 ve 3. saniyeler arası: {sonuc_2_3} saniye gecikme"
info2=f"4 ve 5. saniyeler arası: {sonuc_4_5} saniye gecikme"
info3=f"6 ve 7. saniyeler arası: {sonuc_6_7} saniye gecikme"
info4=f"8 ve 9. saniyeler arası: {sonuc_8_9} saniye gecikme"

print(info1,len(info1)*'-',info2,len(info2)*'-',info3,len(info3)*'-',info4,len(info4)*'-',sep='\n')


gecikme_sureleri=list()
gecikme_sureleri.append(sonuc_2_3)
gecikme_sureleri.append(sonuc_4_5)
gecikme_sureleri.append(sonuc_6_7)
gecikme_sureleri.append(sonuc_8_9)

x_eksen_isimleri=list()
x_eksen_isimleri.append("2-3")
x_eksen_isimleri.append("4-5")
x_eksen_isimleri.append("6-7")
x_eksen_isimleri.append("8-9")


plt.plot(x_eksen_isimleri,gecikme_sureleri,'r')
plt.title('End 2 End Delay Ölçümü')
plt.xlabel('saniye aralığı')
plt.ylabel('Toplam gecikme süresi')

plt.show()