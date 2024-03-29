# Program to generate dark photon simulation data

import pythia8

pythia = pythia8.Pythia()

# Soft QCD non-diffractive events for inclusive meson production (idk random stuff i found on google)
pythia.readString("SoftQCD:nonDiffractive = on")

# Define a new particle for the dark photon
pythia.readString("9900022:new = gamma_dark DarkPhoton")
pythia.readString("9900022:spinType = 1")
pythia.readString("9900022:chargeType = 0")
pythia.readString("9900022:colType = 0")
pythia.readString("9900022:m0 = 0.1")  # Dark photon mass in GeV
pythia.readString("9900022:isResonance = false")  # Set dark photon as stable

# pi0 decay with branching ratio of 10^-6
pythia.readString("111:addChannel = 1 0.000001 101 22 9900022")
# Initialize Pythia
pythia.init()

events = 10000

events_with_dark_photon = []

for i_event in range(events):
    if not pythia.next():
        continue

    HT = 0.0
    MET_x = 0.0
    MET_y = 0.0
    dark_photon_produced = False

    for i in range(pythia.event.size()):
        particle = pythia.event[i]

        # Sum HT using all final-state particles except neutrinos and dark photons
        if particle.isFinal() and particle.idAbs() not in [12, 14, 16, 9900022]:
            HT += particle.pT()

        # For MET, consider only invisible particles (neutrinos and stable dark photons)
        if particle.isFinal() and particle.idAbs() in [12, 14, 16, 9900022]:
            MET_x += particle.px()
            MET_y += particle.py()

        # Check if a dark photon is produced in the event
        if particle.id() == 9900022:
            dark_photon_produced = True

    MET = (MET_x**2 + MET_y**2) ** 0.5

    if dark_photon_produced:
        events_with_dark_photon.append((i_event, HT, MET, dark_photon_produced))

pythia.stat()

# Print the event number, HT, MET, and confirm dark photon production for stored events
for data_point in events_with_dark_photon:
    event_number, HT, MET, dark_photon_produced = data_point
    print(
        f"Event: {event_number}, HT: {HT:.2f} GeV, MET: {MET:.2f} GeV, Dark Photon Produced: {dark_photon_produced}"
    )
