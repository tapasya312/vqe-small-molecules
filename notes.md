Notes

H2 VQE

COBYLA converges pretty fast. Energy comes out close to -1.137 Ha

SPSA is a lot noisier Default settings didn't get close Need to figure out 
how to set the gains properly

The first time I ran VQE the energy was basically zero. Turned out I was 
missing the nuclear repulsion term. GroundStateEigensolver handles it 
automatically

Next up: add shot noise and see which optimizer breaks first