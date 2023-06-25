origR1 = 'Res1=1k'
origC1 = 'Cap1=0.1u'
origR2 = 'Res2=1k'
origC2 = 'Cap2=0.1u'

listR1 = ['Res1=1k', 'Res1=10k']
listC1 = ['Cap1=0.1u', 'Cap1=1u']
listR2 = ['Res2=1k', 'Res2=10k']
listC2 = ['Cap2=0.1u','Cap2=1u']
listALL = []

for x in range(len(listR1)):
    for y in range(len(listC1)):
        for z in range(len(listR2)):
            for a in range(len(listC2)):
                listALL.append(listR1[x] + '_' + listC1[y] + '_' + listR2[z] + '_' + listC2[a])

import os
cwd = os.getcwd()

try:
    os.mkdir('PastaSimulacao')
except:
    print("A pasta já existe!")

orig = "VideoAulaPythonLTspice"
origTxt = orig + '.txt'

import time
start = time.time()
print("Início...")

dir_XVIIx64 = "c:\\Program Files\\ADI\\LTspice"

import subprocess

iter = 0
listALL = []
for r1 in listR1:
    for c1 in listC1:
        for r2 in listR2:
            for c2 in listC2:
                newFileName = r1+'_'+c1+'_'+r2+'_'+c2
                newFileTxt = newFileName + '.txt'
                listALL.append(newFileName)
                with open(origTxt, 'rb') as file:
                    origData = file.read()
                    tempData = origData.replace(origR1.encode('ascii'), r1.encode('ascii'))\
                    .replace(origC1.encode('ascii'), c1.encode('ascii'))\
                    .replace(origR2.encode('ascii'), r2.encode('ascii'))\
                    .replace(origC2.encode('ascii'), c2.encode('ascii'))
                with open('PastaSimulacao/' + newFileTxt, 'wb') as file:
                    file.write(tempData)
                iter += 1
                print('Rodando arquivo de texto #: ', iter, ' de um total de 16, nomeado: ', newFileName)

                subprocess.call(dir_XVIIx64 + '/LTspice.exe -b ' + 'PastaSimulacao/' + newFileTxt)

end = time.time()
print("Finalizado!")
print('~~~~~~~~Tempo despendido: ', end - start, '~~~~~~')

import ltspy3
import matplotlib.pyplot as plt

try:
    os.mkdir('PastaFiguras')
except:
    print("A pasta já existe!")

start = time.time()

print("Início...")

iter = 0
for eachFile in listALL:
    if '' in eachFile:
        print(eachFile)
        sd = ltspy3.SimData('PastaSimulacao/' + eachFile + '.raw')
        name = sd.variables
        time_trace = sd.values
        time_Axis = sd.values[0]
        trace_Axis = sd.values[1:3]

        plt.figure(1)
        plt.plot(time_Axis, trace_Axis[0], 'r-', linewidth=2, label = 'V(in)')
        plt.plot(time_Axis, trace_Axis[1], 'b-', linewidth=2, label = 'V(out)')
        plt.legend(loc='upper right', shadow=True, fontsize = '10')
        plt.xlabel('Tempo (sec)', fontsize=12, color='black')
        plt.ylabel('Tensão (V)', fontsize=12, color='black')
        plt.xlim()
        plt.ylim()
        plt.grid(True)
        plt.suptitle(eachFile,fontsize=14, color='black')
        plt.savefig('PastaFiguras/' + eachFile + '.png', dpi=150)

        plt.close("all")
        iter += 1
        print('Rodando figura #: ', iter, ' de um total de 16, nomeado: ', newFileName)

end = time.time()
print("Finalizado!")
print('~~~~~~~~Tempo despendido: ', end - start, '~~~~~~')