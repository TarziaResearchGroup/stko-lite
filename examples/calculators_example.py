# ruff: noqa: T201

import stk

import stko


def main() -> None:
    """Run the example."""
    bb1 = stk.BuildingBlock("NCCNCCN", [stk.PrimaryAminoFactory()])

    # Run calculations.
    calculations = []
    uff = stko.UFFEnergy()
    calculations.append(uff.calculate(bb1))
    uff_results = uff.get_results(bb1)
    mmff = stko.MMFFEnergy()
    calculations.append(mmff.calculate(bb1))
    mmff_results = mmff.get_results(bb1)

    print(
        uff_results,
        # Get energy from results.
        uff_results.get_energy(),
        uff_results.get_unit_string(),
        # Get energy directly through Calculator.
        uff.get_energy(bb1),
    )
    print(
        mmff_results,
        # Get energy from results.
        mmff_results.get_energy(),
        mmff_results.get_unit_string(),
        # Get energy directly through Calculator.
        mmff.get_energy(bb1),
    )

    # Run through yield statements using the `.calculate` method
    # all in once.
    for i in calculations:
        print(f"{i}: xtb will not output anything as you need a new Results.")
        ey = stko.EnergyResults(i, "kcal mol-1")
        print(ey.get_energy(), ey.get_unit_string())

    # Zipping calculations together.
    mols = [
        stk.BuildingBlock("C1CCC1"),
        stk.BuildingBlock("C1CCCC1"),
        stk.BuildingBlock("C1CCCCC1"),
    ]
    for mol in mols:
        print(
            mol,
            stko.EnergyResults(mmff.calculate(mol), "kcal mol-1").get_energy(),
        )


if __name__ == "__main__":
    main()
