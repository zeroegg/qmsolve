import numpy as np
from qmsolve import Hamiltonian, SingleParticle, init_visualization


#interaction potential
def di_coulomb_potential(particle):
	k_c = 14.39964547842567 # (e*e / (4 * np.pi * epsilon_0))  # measured in eV / Å

	R = 1.06 # measured in Å

	r1 = np.sqrt((particle.x - R/2)**2 + (particle.y)**2 + (particle.z)**2)
	r1 = np.where(r1 < 0.0001, 0.0001, r1) 

	r2 = np.sqrt((particle.x + R/2)**2 + (particle.y)**2 + (particle.z)**2)
	r2 = np.where(r2 < 0.0001, 0.0001, r2) 


	return - k_c/ r1 - k_c/ r2 + k_c/R + 0.0000001*particle.y



H = Hamiltonian(particles = SingleParticle(), 
				potential = di_coulomb_potential, 
				spatial_ndim = 3, N = 150, extent = 9)


eigenstates = H.solve(max_states = 5, N0 = 30, method ='lobpcg-cupy')
print(eigenstates.energies)

visualization = init_visualization(eigenstates)
visualization.plot_eigenstate(0, contrast_vals = [0.01, 0.761])
visualization.animate(contrast_vals = [0.01, 0.761])