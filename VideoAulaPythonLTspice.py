R1,R2,C1,C2 = 'Res1=1k','Res2=5k','Cap1=0.1u','Cap2=0.1u'

orig = "VideoAulaPythonLTspice"
origTxt = orig + '.txt'

import subprocess
subprocess.call('C:\Program Files\ADI\LTspice' + '/LTspice.exe -b ' + origTxt)

import ltspy3
import matplotlib.pyplot as plt

dados = ltspy3.SimData(orig + '.raw')

nome = dados.variables
tempo_curva = dados.values
eixo_tempo = dados.values[0]
eixo_curva = dados.values[1:]
print(eixo_tempo)
plt.figure(1)

plt.plot(eixo_tempo, eixo_curva[0], 'r-', linewidth=2, label = 'V(in)')
plt.plot(eixo_tempo, eixo_curva[1], 'b-', linewidth=2, label = 'V(out)')

plt.legend(loc = 'lower left', shadow=True, fontsize = '8')
plt.suptitle(R1 + '_' + R2 + '_' + C1 + '_' +C2, fontsize=14, color='black')
plt.xlabel('Tempo (seg)', fontsize = 12, color = 'black')
plt.ylabel('Tensão (V)', fontsize = 12, color = 'black')
plt.xlim(0,0.005)
plt.ylim(-7,7)
plt.grid(True)
plt.savefig(orig + '.png', dpi = 150)
