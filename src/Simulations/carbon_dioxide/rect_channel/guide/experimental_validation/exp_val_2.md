[Simulations](../../../../index.html)

&&&

# Experimental Validation 2

simulations 43, 44

## Goal

Simulate experimental conditions in order to separatly predict loss from insulated surfaces and from irradiated surface.

## Losses From Insulated Surfaces

Use temperature profile dirichlet condition on insulated surfaces based experimental measurement.

## Steps


- temperature profile
    - setup geometry
    - apply constant temperature boundary at edge of irradiated surface
    - make source to enforce point measurement of temperature
- grid
- simulations
    - materials (properties in spreadsheet)
    - boundary conditions
        - solar flux: constant prfile generated by my program (vary power to match outlet temperature)
        - temperature profile
        - mass flow inlet
            - mass flow rate
            - temperature
    - check for energy balance
    - record solar heat input

## Calibrating based on experiment

- first, look at how the six thermocouple measurements vary between runs



