import numpy as np
import stk

import stko

bb1 = stk.BuildingBlock("C1CCCCC1")
# Fake rotation of new molecule.
bb2 = stk.BuildingBlock("C1CCCCC1").with_rotation_about_axis(
    1.34,
    np.array((0, 0, 1)),
    np.array((0, 0, 0)),
)

# Get RMSD without alignment.
calculator = stko.RmsdMappedCalculator(bb1)
results = calculator.get_results(bb2)
rmsd = results.get_rmsd()
print(rmsd)
