# Lagrangian stuff

This U(1) gauge symmetry is associated with a new dark photon field, denoted as $A'_{\mu}$. The Lagrangian that includes kinetic mixing between the photon and the dark photon is given by:

$$\mathcal{L}=-\frac{1}{4}F_{\mu \nu}F^{\mu \nu} -\frac{1}{4}F'_{\mu \nu}F'^{\mu \nu} + \frac{\epsilon}{2}F_{\mu \nu}F'^{\mu \nu}+\frac{1}{2}m^2_{A'}A'_\mu A'^\mu$$

In this expression:
- $F_{\mu \nu} = \partial_\mu A_\nu-\partial_\nu A_\mu$ is the electromagnetic field strength tensor, where $A_\mu$ is the SM photon field.
- $F'_{\mu \nu} = \partial_\mu A'_\nu-\partial_\nu A'_\mu$ is the dark photon field strength tensor, where $A'_\mu$ is the SM photon field.
- $\epsilon$ is the dimensionless kinetic mixing parameter.

The first term represents kinetic term for the standard electromagnetic field

The second term is analogous to the first term but applies to the dark photon field

The third term introduces kinetic mixing between the photon and the dark photon fields

The fourth term is a mass term for the dark photon field. However, since the we are assuming the mass is 0, we can just cancel it out. 

To ensure that the kinetic terms only consist of terms from one field ("diagonalize" the Lagrangian), we need to eliminate the third term. We can do this by ensuring that the product $F_{\mu \nu}F'^{\mu \nu}$ vanishes. We can do this with a field redefinition:

$$\tilde{A}_\mu=A_\mu+\epsilon A'_\mu$$
$$\tilde{A'}_\mu=\sqrt{1-\epsilon^2}A'_\mu$$

Substituting this, we get:

$$\mathcal{L}=-\frac{1}{4}\tilde{F}_{\mu \nu}\tilde{F}^{\mu \nu} -\frac{1}{4}\tilde{F}'_{\mu \nu}\tilde{F}'^{\mu \nu} $$

There is now no more kinetic mixing between the terms. 

We have successfuly isolated the two fields. An interesting property arises when we do this.

The interaction of the photon field with charged particles is described with an interaction term:

$$\mathcal{L}_\text{int}=eA_\mu J^\mu _{\text{em}}$$

Where $e$ is the coupling constant (the charge of the electron) and $J^\mu _{\text{em}}$ is the electromagnetic current. 

Using our new definition of $\tilde{A}_\mu$, we can substitute:

$$\mathcal{L}_\text{int}=e\tilde{A}_\mu J^\mu _{\text{em}}$$
$$\mathcal{L}_\text{int}=e (A_\mu + \epsilon A'_\mu) J^\mu _{\text{em}}$$
$$\mathcal{L}_\text{int}=eA_\mu J^\mu _{\text{em}} + e\epsilon A'_\mu J^\mu _{\text{em}}$$

The significance of that equation is that the dark photon can interact with the same particles as a regular photon can, with a suppression factor $\epsilon$. 

This coupling opens up new interaction channels, such as the potential production of dark photons in processes involving electromagnetic interactions. For instance, in meson decays, a neutral pion $\pi^0$ can decay into a photon and a dark photon:

$$\pi^0 \rightarrow \gamma + \tilde{A}'_\mu$$

The rate of such a process is proportional to $\epsilon^2$. The massless dark photon would contribute to missing energy signatures in experiments.

According to the NA48 experiment, the upper limit of $\epsilon^2$ was calculated to be around $10^{-6}$. 