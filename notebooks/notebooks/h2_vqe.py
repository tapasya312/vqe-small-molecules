from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.circuit.library import UCCSD
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorEstimator

driver = PySCFDriver(atom="H 0 0 0; H 0 0 0.735", basis="sto3g")
problem = driver.run()
hamiltonian = problem.hamiltonian.second_q_op()
mapper = JordanWignerMapper()
qubit_ham = mapper.map(hamiltonian)

estimator = StatevectorEstimator()
ansatz = UCCSD(
    num_spatial_orbitals=problem.num_spatial_orbitals,
    num_particles=problem.num_particles,
    qubit_mapper=mapper,
)

optimizer = COBYLA(maxiter=200)
vqe = VQE(estimator, ansatz, optimizer)
solver = GroundStateEigensolver(mapper, vqe)
result = solver.solve(problem)

print("total energy:", result.total_energies[0])