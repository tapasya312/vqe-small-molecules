from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper

driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735", basis="sto3g")
problem = driver.run()

hamiltonian = problem.hamiltonian.second_q_op()

mapper = JordanWignerMapper()
qubit_ham = mapper.map(hamiltonian)

print("qubits:", qubit_ham.num_qubits)
print("pauli terms:", len(qubit_ham))