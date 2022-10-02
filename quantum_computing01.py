# SIMULAÇÃO DE CIRCUITO QUÂNTICO
from Neuraline.QuantumPhysics.quantum_computing import CircuitSimulator # importação da classe de simulação
# a velocidade de carregamento irá depender da capacidade da sua máquina local
# se a sua placa gráfica for muito fraca o carregamento poderá falhar da primeira vez
quantum_computing = CircuitSimulator() # instanciação do objeto da classe importada
result = quantum_computing.runQuantumCircuit( # chamada do método de execução do simulador
    nqubits=2, # número de trilhas de qubit (eixo y vertical)
    nmoments=10 # número de impulsos (momentum) elétricos receptíveis a portas quânticas (eixo x horizontal)
) # se a tela não carregar a simulação, feche e execute o código de novo até que o simulador seja carregado
if result: print('Simulador de circuito quântico carregado com sucesso.')
else: print('Erro no carregamento do simulador de circuito quântico.')