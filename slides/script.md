Hello everyone, thank you all for coming. My name is Rohan Arni, and I’m a junior at High Technology High School. Today, I’d like to present my research on searching for dark photon production using genetic algorithms. 

Slide 1:
Let's start with some background. Dark matter makes up about 27% of the energy density and 85% of the matter density of the universe. However, it remains one of the biggest mysteries in physics. The standard model describes all known particles and their interactions, but contains no explanation of dark matter. 

This is where the concept of a 'dark sector' comes in. Scientists have proposed that there might be an entire sector of particles and forces that interact very weakly with ordinary matter, explaining why we haven't directly detected dark matter yet. 

One of the key players in this proposed dark sector is the 'dark photon’, which operates similarly to the standard model photon.  The dark photon is theorized to interact with the SM photon via kinetic mixing, an effect where the dark photon and the standard photon can weakly interact with each other.

To introduce the dark photon interactions to the standard model, we can extend the Standard Model's gauge group by adding a new U(1) gauge symmetry, similar to the photon.

(indicate at slide)

Slide 2:

The Lagrangians tells us how the photon and the dark photon will interact through kinetic mixing and with currents. 
Here are the Lagrangians:

Let’s define a few things. The F term is the electromagnetic tensor which describes the photon field in spacetime.

The photon field is represented by the A term. 

The F’ term is similar to the electromagnetic tensor, but describes the dark photon field (denoted by A’).

Epsilon is the kinetic mixing parameter. 

In the first lagrangian, the first term is the kinetic term for the electromagnetic field, which is a part of the standard model. The second term is the kinetic term for the dark photon field, which is an extension of the standard model.  This term tells us that the dark photon behaves in a way similar to the photon.

The third term is the kinetic mixing term. It connects the standard photon field with the dark photon field. The parameter $\epsilon$ determines the strength of this mixing. If $\epsilon$ is non-zero, even if it's very small, it allows for interaction between the two sectors

The second Lagrangian describes the interaction between the respective fields and their currents. Right now, the dark photon can only interact with the dark current.


Slide 3:

Now that we've introduced the Lagrangian, we need to diagonalize the kinetic terms. 

When we have mixing terms in our Lagrangian, it suggests that our original fields don't correspond to physical particles. Instead, they're kind of 'mixed up' versions of the real particles.

Diagonalization is the mathematical process that helps us find the true, physical particles.

We can diagonalize the kinetic terms by rotating the fields like so:

And after some (quite painful) math, we find that if the dark photon has mass, then the interaction Lagrangian contains the following term:

This term connects the dark photon to the standard electromagnetic current.

Slide 5:

Let’s discuss the consequences of this theory. Our equations reveal something interesting: the dark photon can interact with the same particles as a regular photon, suppressed by a factor epsilon. 

This suppressed interaction is called the 'dark photon portal.' The existence of this portal opens up new interaction and production channels. Here’s an example:

This equation represents a decay process where a neutral pion ($\pi^0$) decays into a regular photon ($\gamma$) and a dark photon ($\gamma'$). In the Standard Model, pions typically decay into two photons. But with the dark photon portal, there's now a small chance that one of those photons could be a dark photon instead
The rate at which this process occurs is proportional to $\epsilon^2$, which was calculated to be around 10 to the negative 6th.
One of the key ways we might detect the presence of dark photons is through missing or anomalous energy signatures in experiments, due to the fact that the dark photon would not be accounted for in readings.


Slide 6:

Our goal is to design an model that can search for dark photon production by identifying missing or abnormal energy signatures in particle collisions. We can frame this as a binary classification problem. For each collision, we want our model to classify it into one of two categories:
	•	Dark photon produced
	•	No dark photon produced
However, we face a significant challenge: class imbalance. Remember, we expect dark photon production to be a rare event. In machine learning terms, this means our dataset will be highly imbalanced, with the vast majority of our data points belonging to the 'no dark photon' class.
This is where AdaBoost comes in. AdaBoost, short for Adaptive Boosting, is a machine learning algorithm that works well for dealing with imbalanced datasets. AdaBoost is an ensemble method, meaning it combines multiple 'weak' classifiers to create a single, strong classifier. Each new classifier is trained to focus on the examples that the previous classifiers got wrong. Each weak classifier is also assigned a weight based on its accuracy. More accurate classifiers have a greater influence on the final prediction.

Slide 7:

We can make our model more efficient through hyperparameter optimization. An Adaboost model has two hyperparameters: the number of estimators (the number of weak learners) and the learning rate (scaling the contribution of each classifier). Tuning these hyperparameters manually is time-consuming and often inefficient. Genetic algorithms use the power of natural selection and evolution to find optimal solutions to a problem.
	1	The genetic algorithm starts by defining a random population with different characteristics. 
	2	We then define a fitness function that evaluates each individual and assigns it a fitness based on a certain set of criteria. 
	3	We select the most fit individuals to be the “parents” for the next generation. 
	4	These parents cross over their “genetic” data” to create offspring in the next generation.
	5	Then, each individual has a chance to be mutated and have their genetic data slightly tweaked to maintain diversity. 
	6	The worst individuals are dropped, forming the next generation. 
	7	This repeats for the number of generations specified. 
This process allows genetic algorithms to experiment and evaluate different solutions to the initial problem to find better solutions. 

Slide 8:

I decided that simulating the data would be much easier as I could keep track of all particles produced in each event. I used Pythia 8.3, a C++ and Python library for particle simulations, to simulate proton-proton collisions at 14 TeV. This energy was chosen to match the energy of the Large Hadron Collider (LHC). To incorporate the dark photon hypothesis, I modified the simulation to include the decay channel I mentioned previously. I set the branching ratio for this decay to $10^{-6}$.

In our simulation, I defined the dark photon as a stable particle that is color neutral, chargeless, and has a spin of 1 and a mass of 10 to the negative 20th eV. This was calculated to be the lower bound for the dark photon mass. 

Now, let's discuss the key variables from our simulated data.
HT (Scalar sum of jet momenta): This is calculated by summing the total visible energy in the event. It gives us a measure of the overall energy scale of the collision.

MET (Missing Transverse Energy): This is calculated by summing the energy produced by neutrinos and dark photons. These particles don't interact with our detectors, so their presence is inferred from an imbalance in the total momentum of the event.
The MR variable gives us a sense of the mass scale of the particles involved in the collision. 
R² quantifies the balance of energy and momentum in the event. It's sensitive to events where there might be significant invisible particles produced, like our dark photons. 
Dark Photon Flag: This is a boolean value indicating whether a dark photon was produced in the event.


To calculate MR, I used the formula shown above:Where
E1​ and E2 are the energies of the two leading jets (the most energetic particles resulting from a high-energy collision) in the event.
P1 and p2​ are the momenta of the same jets along the beam axis (the z-axis)

To calculate R^2, I used this formula:

With
MT being the transverse mass. This is a measure of the mass of a system in the transverse plane (perpendicular to the beam direction). 
	•	P visible is The sum of the transverse momenta of all visible particles 
	•	MET The missing transverse energy
	•	Phi is the angle between the visible system's momentum vector and the MET vector. 
The R2 variable is dimensionless and gives a measure of how well the event's visible transverse momentum aligns with the MET. Events with significant imbalances (low R2) might indicate new physics.

The algorithm began by running the simulation to create 500,000 data points. I then imported the dataset into a pandas DataFrame, which is a python library for handling data. The data was then split into a training and testing dataset, with the training dataset being used for training the adaboost model and the testing dataset being used for evaluating the model for accuracy. 

Now, I created the initial population for our algorithm. Each individual in the population is assigned two random parameters: the number of estimators (between 50 and 400) and the learning rate (between 0.1 and 1). This forms our initial, random population.

Then, I defined our fitness function. This took in an individual and created a new AdaBoost model based on its parameters. It trained the AdaBoost model and returned its accuracy on the testing dataset as its fitness. 

Now, I created the genetic algorithm. To do this, I used the distributed evolutionary algorithms package to create the mutation and selection functions, along with setting the parameters of the genetic algorithm. 

Finally, I ran the genetic algorithm. It cycled through 10 generations of individuals through the process described before, and created the most optimal AdaBoost model. 

So here’s a snapshot of the data that the simulator generated. You can see each event has a number attached to it, along with the five values we talked about earlier. In the total data set, only 25 out of the 500,000 data points indicated that a dark photon was produced, proving why having a model that can handle an imbalance is necessary. 

This slide shows the output of the genetic algorithm while it was running. As you can see, the minimum fitness and the average fitness increase for each generation. 
After the genetic algorithm was done, it created a model with a fitness of 0.99995, which means it had an accuracy of 99.995% on the testing data.
The final model had 319 estimators and a learning rate of 0.1. Having 319 estimators means the model is quite complex and has had many opportunities to learn from its mistakes. Our small learning rate slows down the learning process but allows the model to understand the complexities of the data. 
The accuracy of the model where a dark photon was produced was 80%. However, there were no false positives. This means that when the model if a dark photon was produced, there was actually a dark photon produced in that event. 
- The GA was successful in finding a model with a high accuracy, as shown by a model accuracy of 99.995% on the testing dataset.
- However, the accuracy for instances where a dark photon was produced stood at 80%.
- This dataset had an extreme imbalance, explaining the 80% accuracy on data points where a dark photon was produced in the testing set.
- This can be countered with using more advanced classification techniques like reinforcement learning or XGBoost or more training power. 
- However, there were no false positives, meaning that this algorithm could be used in beam experiments to find data to support the idea that dark photons are produced in these proton-proton experiments.

I would like to thank:
- Dr. Richard Oppenheim and Dr. Bruce Cortez (ex-AT&T Research) for their feedback and guidance for this project. When I started this project, I went in blind with no prior knowledge or experience with this specific subject matter, and Dr. Oppenheim and Dr. Cortez provided me with a way to get feedback as I developed the project more.
I would also like to thank the University of Chicago and the organizers of the TeVPA conference for giving me an opportunity to share my research.
Any questions?




