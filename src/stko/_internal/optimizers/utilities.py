import shutil
from collections import abc
from itertools import chain
from pathlib import Path

import rdkit.Chem.AllChem as rdkit  # noqa: N813
import stk

# This dictionary gives easy access to the rdkit bond types.
bond_dict = {
    "1": rdkit.rdchem.BondType.SINGLE,
    "am": rdkit.rdchem.BondType.SINGLE,
    "2": rdkit.rdchem.BondType.DOUBLE,
    "3": rdkit.rdchem.BondType.TRIPLE,
    "ar": rdkit.rdchem.BondType.AROMATIC,
}


def move_generated_macromodel_files(
    basename: str, output_dir: Path | str
) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for filename in Path().glob(f"{basename}*"):
        # Do not move the output_dir.
        if filename == output_dir:
            continue
        shutil.move(filename, output_dir / filename)


def has_h_atom(bond: stk.Bond) -> bool:
    """Check if a bond has a H atom.

    Parameters:
        bond:
            Bond to test if it has a H atom.

    Returns:
        Returns `True` if bond has H atom.

    """
    if bond.get_atom1().get_atomic_number() == 1:
        return True
    return bond.get_atom2().get_atomic_number() == 1


def has_metal_atom(bond: stk.Bond, metal_atoms: list[stk.Atom]) -> bool:
    """Check if a bond has a metal atom.

    Parameters:
        bond:
            Bond to test if it has a metal atom.

        metal_atoms:
            List of metal atoms.

    Returns:
        Returns `True` if bond has metal atom.

    """
    if bond.get_atom1() in metal_atoms:
        return True
    return bond.get_atom2() in metal_atoms


def metal_atomic_numbers() -> abc.Iterable:
    return chain(range(21, 31), range(39, 49), range(72, 81))


def get_metal_atoms(mol: stk.Molecule) -> list[stk.Atom]:
    """Return a list of metal atoms in molecule."""
    metals = set(metal_atomic_numbers())
    return [
        atom for atom in mol.get_atoms() if atom.get_atomic_number() in metals
    ]


def get_metal_bonds(
    mol: stk.Molecule,
    metal_atoms: list[stk.Atom],
) -> tuple[list, list]:
    """Return a list of bonds in molecule that contain metal atoms."""
    metal_bonds = []
    ids_to_metals = []
    for bond in mol.get_bonds():
        if bond.get_atom1() in metal_atoms:
            metal_bonds.append(bond)
            ids_to_metals.append(bond.get_atom2().get_id())
        elif bond.get_atom2() in metal_atoms:
            metal_bonds.append(bond)
            ids_to_metals.append(bond.get_atom1().get_id())

    return metal_bonds, ids_to_metals


def to_rdkit_mol_without_metals(
    mol: stk.Molecule,
    metal_atoms: list[stk.Atom],
    metal_bonds: list[stk.Bond],
) -> rdkit.Mol:
    """Create :class:`rdkit.Mol` with metals replaced by H atoms.

    Parameters:
        mol:
            The molecule to be optimized.

        metal_atoms:
            List of metal atoms.

        metal_bonds:
            List of bonds including metal atoms.

    Returns:
        RDKit molecule with metal atoms replaced with H atoms.

    """
    edit_mol = rdkit.EditableMol(rdkit.Mol())
    for atom in mol.get_atoms():
        if atom in metal_atoms:
            # In place of metals, add H's that will be constrained.
            # This allows the atom ids to not be changed.
            rdkit_atom = rdkit.Atom(1)
            rdkit_atom.SetFormalCharge(0)
        else:
            rdkit_atom = rdkit.Atom(atom.get_atomic_number())
            rdkit_atom.SetFormalCharge(atom.get_charge())
        edit_mol.AddAtom(rdkit_atom)

    for bond in mol.get_bonds():
        if bond in metal_bonds:
            # Do not add bonds to metal atoms (replaced with H's).
            continue
        edit_mol.AddBond(
            beginAtomIdx=bond.get_atom1().get_id(),
            endAtomIdx=bond.get_atom2().get_id(),
            order=rdkit.BondType(bond.get_order()),
        )

    edit_mol = edit_mol.GetMol()
    rdkit_conf = rdkit.Conformer(mol.get_num_atoms())
    for atom_id, atom_coord in enumerate(mol.get_position_matrix()):
        rdkit_conf.SetAtomPosition(atom_id, atom_coord)
        edit_mol.GetAtomWithIdx(atom_id).SetNoImplicit(True)  # noqa:FBT003
    edit_mol.AddConformer(rdkit_conf)

    return edit_mol


def get_long_bond_ids(
    mol: stk.ConstructedMolecule,
    reorder: bool = False,
) -> tuple[tuple[int, int], ...]:
    """Return tuple of long bond ids in a ConstructedMolecule."""
    long_bond_ids = []
    for bond_infos in mol.get_bond_infos():
        if bond_infos.get_building_block() is None:
            if reorder:
                ba1 = bond_infos.get_bond().get_atom1().get_id()
                ba2 = bond_infos.get_bond().get_atom2().get_id()
                if ba1 < ba2:
                    ids = (
                        bond_infos.get_bond().get_atom1().get_id(),
                        bond_infos.get_bond().get_atom2().get_id(),
                    )
                else:
                    ids = (
                        bond_infos.get_bond().get_atom2().get_id(),
                        bond_infos.get_bond().get_atom1().get_id(),
                    )
            else:
                ids = (
                    bond_infos.get_bond().get_atom1().get_id(),
                    bond_infos.get_bond().get_atom2().get_id(),
                )
            long_bond_ids.append(ids)

    return tuple(long_bond_ids)
