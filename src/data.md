# Data Storage Hierarchy

Each instance is implemented with an xml file.
Python scripts parse these xml files and generate appropriate scripts for programs such as Pointwise or Fluent.

## Master
This is the highest level in the hierarchy it contains the most basic elements of a design.

Examples of elements:

* the working fluid
* the inlet and outlet temperatures of that fluid
* the total incident heat flux

Example xml file

	<master>
		<fluid>carbon_dioxide</fluid>
		<T_in>773</T_in>
	</master>

## Design
The shape and dimensions of a particular device

## Geometry
A representation of a *Design* for use in CFD simulations

## Simulation
A single CFD simulation

