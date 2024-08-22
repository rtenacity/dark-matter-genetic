---
theme: ./
colorSchema: light
author: Rohan Arni
date: 2023/01/01
transition: slide-left
---

# Searching for Dark Photon Production Using Genetic Algorithms



<div>
Rohan Arni
</div>
High Technology High School, Lincroft NJ 07738, USA<br>
roarni@ctemc.org

---
section: Introduction
---

# The Dark Photon

- Dark matter makes up 27% of the energy density and 85% of the matter density of the universe.
- The Standard Model does not account for dark matter, a separate dark sector is proposed
- The dark photon is a force carrier for the dark sector, similar to the photon
- New particle can be introduced to the standard model by extending SM gauge group with new $U(1)$ gauge symmetry
- The dark photon interacts with the SM photon via kinetic mixing.


<Item title="Extended Standard Model">
  <div className="flex justify-center items-center">
  <img src="./images/smdiagram.png" width="650" height="auto" alt="AdaBoost Diagram" className="mx-auto" />
  </div>
</Item>

---

# The Dark Photon, cont'd

This U(1) gauge symmetry is associated with a new dark photon field, denoted as $A'_{\mu}$. The Lagrangian that includes kinetic mixing between the photon and the dark photon is given by:

<Item title="Kinetic Mixing Lagrangian"> 

$$\mathcal{L}=-\frac{1}{4}F_{\mu \nu}F^{\mu \nu} -\frac{1}{4}F'_{\mu \nu}F'^{\mu \nu} + \frac{\epsilon}{2}F_{\mu \nu}F'^{\mu \nu}+\frac{1}{2}m^2_{A'}A'_\mu A'^\mu$$


</Item>

Where:
- $F_{\mu \nu} = \partial_\mu A_\nu-\partial_\nu A_\mu$ is the electromagnetic field strength tensor, where $A_\mu$ is the SM photon field.
- $F'_{\mu \nu} = \partial_\mu A'_\nu-\partial_\nu A'_\mu$ is the dark photon field strength tensor, where $A'_\mu$ is the dark photon field.
- $\epsilon$ is the dimensionless kinetic mixing parameter.


---

# Diagonalizing Kinetic Terms

<!-- the gauge fields correspond to physically independent particles -->
- Need to remove the mixing term so the kinetic terms only consist of parameters from one field.  
- Product $F_{\mu \nu}F'^{\mu \nu}$ should vanish to cancel $(\frac{\epsilon}{2}F_{\mu \nu}F'^{\mu \nu})$
- We can do this with a field redefinition ($\tilde{A}_\mu$ and $\tilde{A'}_\mu$).  
- Redefinition must ensure the mixing term is eliminated and the fields are normalized.


<Item title = "Field Redefinition">

$$\tilde{A}_\mu=A_\mu+\epsilon A'_\mu$$
$$\tilde{A'}_\mu=\sqrt{1-\epsilon^2}A'_\mu$$

$$\mathcal{L}=-\frac{1}{4}\tilde{F}_{\mu \nu}\tilde{F}^{\mu \nu} -\frac{1}{4}\tilde{F}'_{\mu \nu}\tilde{F}'^{\mu \nu} $$


</Item>

---

# Interactions

<Item title="Interaction Between Photon and Charged Particle">

$$\mathcal{L}_\text{int}[\psi, \bar{\psi}, A_\mu] = e A_\mu \bar{\psi} \gamma^\mu \psi=eA_\mu J^\mu _{\text{em}}$$

</Item>

Where $e$ is the coupling constant (the charge of the particle) and $J^\mu _{\text{em}}$ is the fermion current ($\bar{\psi} \gamma^\mu \psi$). Using our new definition of $\tilde{A}_\mu$, we can substitute:

<Item title ="Substitution">

$$\mathcal{L}_\text{int}=e\tilde{A}_\mu J^\mu _{\text{em}}$$
$$\mathcal{L}_\text{int}=e (A_\mu + \epsilon A'_\mu) J^\mu _{\text{em}}$$
$$\mathcal{L}_\text{int}=eA_\mu J^\mu _{\text{em}} + e\epsilon A'_\mu J^\mu _{\text{em}}$$
</Item>

---

# Consequences

- Based on the equation, the dark photon can interact with the same particles as a photon (suppressed by a factor $\epsilon$)

- This interaction is called the dark photon portal

- This portal opens up new interaction/production channels. 
- For instance, in meson decays, a neutral pion $\pi^0$ can decay into a photon and a dark photon:

<Item title = "Production of Dark Photon">

$$\pi^0 \rightarrow \gamma + \gamma'$$
</Item>

- The rate of such a process is proportional to $\epsilon^2$ $(\approx 10^{-6})$. 

- The dark photon would contribute to missing energy signatures in experiments.

--- 

# Machine Learning Approach


- The goal is to design an algorithm that can search for dark photons via missing/abnormal energy signatures. 
- A binary classification model can be used to evaluate a data point if a dark photon is produced or not. 
- Due to the nature of dark photon production, the resulting dataset will be imbalanced, with a majority of interaction not producing a dark photon.
- This imbalance can be accounted for with an AdaBoost model. 

<Item title="AdaBoost Diagram">
  <div className="flex justify-center items-center">
  <img src="./images/AdaBoost.png" width="300" height="auto" alt="AdaBoost Diagram" className="mx-auto" />
  </div>
</Item>


---

# Why Genetic Algorithms?

- The AdaBoost model has a set of hyperparameters (the number of estimators and the learning rate).
- Tuning the hyperparameters manually can take a lot of time to approach an optimal solution.
- An optimal solution to this problem can be reached with a genetic algorithm.


<Item title="Genetic Algorithm Flowchart">
```mermaid 
graph LR
    A[Initialize Population] --> B[Evaluate Fitness]
    B --> C{Termination Condition Met?}
    C -->|No| D[Selection]
    D --> E[Crossover]
    E --> F[Mutation]
    F --> G[Replace Least Fit]
    G --> B
    C -->|Yes| H[Return Best Solution]
    %% A1[Create initial set of random solutions] --> A
    %% B1[Assess how close each solution is to optimum] --> B
    %% D1[Select individuals based on fitness] --> D
    %%D2[Higher fitness = Higher chance of selection] --> D
    %%E1[Combine parent chromosomes to create offspring] --> E
    %%F1[Alter gene values with certain probability] --> F
    %%G1[New offspring replace least fit individuals] --> G
    %%G2[Form new generation] --> G
```
</Item>

---
section: Methods
---

# Data Simulation

- Simulated proton-proton collisions at 14 TeV using ```Pythia3.8```
- The simulation was modified to add a decay channel $(\pi^0 \rightarrow \gamma + \gamma')$ with a branching ratio of $10^{-6}$
- The dark photon was defined as a stable massless particle that is color neutral, chargeless, and has a spin of 1
- To gather data from the simulation, the program calculated:
  - the scalar sum of jet transverse momenta $(HT)$ by summing the total visible energy
  - the missing transverse energy $(MET)$ by summing total energy produced by neutrinos and dark photons
  - the razor variable of mass scale $(MR)$
  - the razor variable $(R^2)$, which quantifies the balance of energy and momentum. 
  - boolean flag that checked if a dark photon was produced.

---

# Data Calculations


<!-- $(MR)$ was calculated via: -->
More in-depth calculations:
<Item title="MR Formula">

$$MR = \sqrt{(E_{1} + E_{2})^2 - (p^z_{1} + p^z_{2})^2}$$
</Item>
  <!-- - where $E_{1}$ and $E_{2}$ are the energies of the two leading jets and $p^z_{1}$ and $p^z_{2}$ are their momenta along the beam axis (z-axis) -->

<!-- The razor variable $(R^2)$, which quantifies the balance of energy and momentum was calculated via: -->

<Item title="R2 Formula">

$$R^2 = \left(\frac{M_T}{MR}\right)^2$$
<!-- with $MT$ being defined as  -->
  $$M_T = \sqrt{2 |\vec{p}_T^{vis}| |\vec{MET}| (1 - \cos(\Delta\phi))}$$


<!-- MT measure of the mass of a system in the transverse plane -->
<!-- and $\Delta\phi$ being the angle between the visible system's momentum and the MET vector.  -->
</Item>

---

# Algorithm, Pt. 1


<div style="display: flex; align-items: center; justify-content: center; min-height: 50vh;">
<div className="w-full p-4">
<Item title = "Initialization">
```mermaid
  flowchart LR
      A[Start] --> B[Create dataset\n500,000 data points]
      B --> C[Import dataset\ninto Pandas DataFrame]
      C --> D[Split data\nTraining:Testing 4:1]
      D --> E[Create initial population]
      E --> E1[Set number of estimators: 50-400]
      E --> E2[Set learning rate: 1-10]
```

</Item>
</div>
</div>

---

# Algorithm, Pt. 2

<div style="display: flex; align-items: center; justify-content: center; min-height: 50vh;">
<div className="w-full p-4">
<Item title = "Genetic Algorithm Creation">
```mermaid
  flowchart LR
        F[Define fitness function] --> G["Define mutation function (DEAP)"]
        G --> H["Define selection function (DEAP)"]
        H --> I[Set genetic algorithm parameters]
        I --> I1[Population size: 50]
        I --> I2[Crossover probability: 0.5]
        I --> I3[Mutation probability: 0.2]
```

</Item>
</div>
</div>


---

# Algorithm, Pt. 3

<div style="display: flex; align-items: center; justify-content: center; min-height: 50vh;">
<div className="w-full p-4">
<Item title = "GA Execution">
```mermaid
  flowchart LR
        J[Run genetic algorithm\nfor 10 generations] --> L{Is number of\n generations met?}
        L -->|Yes| M[End]
        L -->|No| K[Evaluate fitness\nof each model]        
        K --> N[Select individuals\nfor next generation]
        N --> O[Apply crossover]
        O --> P[Apply mutation]
        P -.-> J
```

</Item>
</div>
</div>

---
section: Results
---

# Data Snapshot
- In the data set, only 25 out of 500,000 data points indicated that a dark photon was produced.

<Item title = "Snapshot of Simulation Data">

| Event Number | $HT$ | $MET$ | $MR$ | $R^2$ | Dark Photon Produced? |
|--------------|-----|-----|-----|-----|----------|
| 352806 | 94.775 | 0.000 | 14000.000 | 0.000000 | False |
| 417824 | 48.964 | 0.000 | 14000.000 | 0.000000 | False |
| 469847 | 196.721 | 0.000 | 14000.000 | 0.000000 | False |
| 407746 | 118.227 | 1.069 | 13983.157 | 2.585e-06 | False |
| 469848 | 105.605 | 0.000 | 14000.000 | 0.000000 | False |
</Item>

---

# Genetic Algorithm Output Data

<Item title = "Genetic Algorithm Data">

| Generation | Num. Evals | Avg. Fitness | Std. Dev Of Fitness | Min Fitness | Max Fitness |
|-----|-----------|--------------|---------------------|-------------|-------------|
| 1   | 33        | 0.999929     | 1.91844e-05         | 0.99988     | 0.99995     |
| 3   | 27        | 0.999949     | 6.00333e-06         | 0.99992     | 0.99995     |
| 5   | 28        | 0.99995      | 1.11022e-16         | 0.99995     | 0.99995     |
| 7   | 34        | 0.999949     | 4.58258e-06         | 0.99992     | 0.99995     |
| 9   | 28        | 0.999949     | 4.58258e-06         | 0.99992     | 0.99995     |
| 10  | 40        | 0.99995      | 1.4e-06             | 0.99994     | 0.99995     |
</Item>

---

# Final Model Results

- After algorithm execution, the algorithm converged on a solution with a fitness of 0.99995. 
- The hyperparameters of the model are:

<Item title="Final Model Hyperparameters">

| Number of Estimators | Learning Rate |
|----------------------|---------------|
| 319 | 0.1 |

</Item>

- Evaluating the model on the testing dataset resulted in an accuracy of 99.995%. 
- However, the accuracy for instances where a dark photon was produced stood at 80%.
- Model had no false positives. 

---
section: Conclusions
---

# Conclusions

- The GA was successful in finding a model with a high accuracy, as shown by a model accuracy of 99.995% on the testing dataset.
- However, the accuracy for instances where a dark photon was produced stood at 80%.
- This dataset had an extreme imbalance, explaining the 80% accuracy on data points where a dark photon was produced in the testing set.
- This can be countered with using more advanced classification techniques (RL, XGBoost, etc.)
- However, there were no false positives, meaning that this algorithm could be used in beam experiments to find data to support the idea that dark photons are produced in these proton-proton experiments.

--- 
section: Acknowledgements
---

# Acknowledgements

<div style="display: flex; align-items: center; justify-content: center; min-height: 50vh;">
<div className="w-full p-4">
<Item title = "Acknowledgements">
I would like to thank:

- Dr. Richard Oppenheim and Dr. Bruce Cortez (ex-AT&T Research) for their feedback and guidance for this project. 
- The University of Chicago and the organizers of the TeVPA conference for giving me an opportunity to share my research.

</Item>
</div>
</div>

---
section: Citations
---

# Citations

<div style="font-size: 11px;">
    <ul>
        <li>Aguilar-Arevalo, A.A.: Search for Dark Matter in the Beam-Dump of a Proton Beam with MiniBooNE. Journal of Physics: Conference Series <strong>912</strong>, 012017 (2017). <a href="https://doi.org/10.1088/1742-6596/912/1/012017">https://doi.org/10.1088/1742-6596/912/1/012017</a></li>
        <li>Batley, J., et al.: Search for the dark photon in decays. Physics Letters B <strong>746</strong>, 178–185 (2015). <a href="https://doi.org/10.1016/j.physletb.2015.04.068">https://doi.org/10.1016/j.physletb.2015.04.068</a></li>
        <li>Battaglieri, M., et al.: Dark Matter Search in a Beam-Dump EXperiment (BDX) at Jefferson Lab an Update on PR12-16-001 the BDX Collaboration. (2018).</li>
        <li>Berkane, A., Boussahel, M.: Dark Photon as an Extra U(1) Extension to the Standard Model with General Rotation in Kinetic Mixing. (2021).</li>
        <li>Celentano, A., et al.: New Production Channels for Light Dark Matter in Hadronic Showers. Physical Review D <strong>102</strong>(7), 075026 (2020). <a href="https://doi.org/10.1103/physrevd.102.075026">https://doi.org/10.1103/physrevd.102.075026</a></li>
        <li>Chatrchyan, S., et al.: Search for Supersymmetry with Razor Variables In PP Collisions Ats=7 TeV. Physical Review D <strong>90</strong>(11), 112001 (2014). <a href="https://doi.org/10.1103/physrevd.90.112001">https://doi.org/10.1103/physrevd.90.112001</a></li>
        <li>Cushman, P., et al.: Snowmass CF1 Summary: WIMP Dark Matter Direct Detection. (2013). <a href="https://doi.org/10.48550/arxiv.1310.8327">https://doi.org/10.48550/arxiv.1310.8327</a></li>
        <li>De Napoli, M.: Production and Detection of Light Dark Matter at Jefferson Lab: The BDX Experiment. Universe <strong>5</strong>(5), 120 (2019). <a href="https://doi.org/10.3390/universe5050120">https://doi.org/10.3390/universe5050120</a></li>
        <li>Deb, K.: Genetic Algorithm in Search and Optimization: The Technique and Applications. (1998). <a href="http://repository.ias.ac.in/82743/">http://repository.ias.ac.in/82743/</a></li>
        <li>Dutra, M., et al.: MeV Dark Matter Complementarity and the Dark Photon Portal. Journal of Cosmology and Astroparticle Physics <strong>2018</strong>(03), 037–037 (2018). <a href="https://doi.org/10.1088/1475-7516/2018/03/037">https://doi.org/10.1088/1475-7516/2018/03/037</a></li>
        <li>Fabbrichesi, M., et al.: The Dark Photon. (2020).</li>
        <li>Leung, Y., et al.: Degree of Population Diversity - a Perspective on Premature Convergence in Genetic Algorithms and Its Markov Chain Analysis. IEEE Transactions on Neural Networks <strong>8</strong>(5), 1165–1176 (1997). <a href="https://doi.org/10.1109/72.623217">https://doi.org/10.1109/72.623217</a></li>
        <li>Novaes, S.: Standard Model: An Introduction. (2000). <a href="https://arxiv.org/pdf/hep-ph/0001283v1.pdf">https://arxiv.org/pdf/hep-ph/0001283v1.pdf</a></li>
        <li>Tong, D.: Gauge Theory.</li>
    </ul>
</div>
