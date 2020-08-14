from qiskit.visualization import plot_bloch_multivector
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator, random_statevector
import random
import numpy as np

class State:
    operators = ['X', 'Y', 'Z', 'H', 'T', 'S']	

    def __init__(self):
        self.state = Statevector.from_label('0')
        self.operations = []
        self.original = Statevector.from_label('0')
        
    def reset(self):
        self.state = self.original
        self.operations = []
        
    def apply_gate(self, gate):
        self.state = self.state.evolve(Operator.from_label(gate))
        self.operations.append(gate)
    
    def get_gates(self):
        return " ".join(self.operations)
    
    def is_equal(self, other_state):
        return self.state.equiv(other_state.get_state())
   
    def new_state(self, n=5):
        for i in range(n):
            self.state = self.state.evolve(Operator.from_label(State.operators[random.randint(0, len(State.operators)-1)]))
        self.original = self.state
    
    def random_state(self):
        self.state = random_statevector(self.state.dim)
        self.original = self.state
        
    def print_bloch(self, name=''):
        return plot_bloch_multivector(self.state.data, title=name, figsize=(500,500))

    def get_state_string(self):
        return " + ".join([str(np.around(j,3))+"|"+str(i)+">" for i,j in enumerate(self.state.data)])
        
    def get_state_data(self):
        return self.state.data
    
    def get_state(self):
        return self.state
