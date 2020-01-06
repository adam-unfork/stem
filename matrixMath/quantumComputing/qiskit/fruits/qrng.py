
######################################

from qiskit import \
    QuantumCircuit, QuantumRegister, \
    ClassicalRegister, execute, Aer, \
    IBMQ, BasicAer

import numpy as np


################################################

# set up the quantum register with one wire
quantumRegister = QuantumRegister(1, name='quantum register')

# set up the classical register with one wire
classicalRegister = ClassicalRegister(1, name='classical register')

# set up the quantum circuit
qc = QuantumCircuit(quantumRegister, classicalRegister)

######################################################


# write the value to 0
qc.reset(quantumRegister)

# place it in a superposition of 1 and 0
qc.h(quantumRegister)
print(qc)

qc.measure(quantumRegister, classicalRegister)


#######################################################


backend = BasicAer.get_backend ('statevector_simulator')
job = execute(qc, backend)
result = job.result()


####################################################

x = np.array([[0, 1], [1, 0]])
h = np.array([[1,1], [1,-1]])

outputState = result.get_statevector(qc, decimals=3)
outputStateNumpy = np.array(outputState)
outputStateNumpy = [int(x) for x in outputStateNumpy]
print("\n the random bit value: ", outputStateNumpy)

def matrixGen(outputStateNumpy):
    if outputStateNumpy == [1,0]:
        return x
    elif outputStateNumpy == [0,1]:
        return h

matrix = matrixGen(outputStateNumpy)
print(matrix)


################################################


# draw the circuit
# qc.draw()


#####################################################
