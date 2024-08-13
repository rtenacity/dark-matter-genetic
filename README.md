# Searching for Dark Photon Production Using Genetic Algorithms

Dark matter has been a key area of research in physics for over ninety years. The dark photon is a proposed model of dark matter that extends the Standard Model to add a new force mediator to interact with the dark sector. The focus of this paper was to investigate the plausibility of using modern computational techniques, most prominently genetic algorithms, to simulate and detect production of dark photons via meson decay. To simulate dark photon production, the Pythia8.3 library was used to create a dataset of 500,000 points. Then, a genetic algorithm was used to find an optimized AdaBoost model with the highest accuracy on the dataset. The algorithm changed the number of estimators and the learning rate for the model and assigned a fitness based on the accuracy on the testing dataset. The optimized AdaBoost model was evaluated to have a 99.995% accuracy on the testing dataset, with 80% accuracy on instances where a dark photon was produced. These statistics make genetic algorithms a viable solution to optimize decision tree models in the field of particle physics.