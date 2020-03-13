# Amino Acid Feature Extraction

[![pypi](https://img.shields.io/pypi/v/amino_acid_feature_extraction.svg)](https://pypi.python.org/pypi/amino_acid_feature_extraction)
[![python](https://img.shields.io/pypi/pyversions/amino_acid_feature_extraction.svg)](https://pypi.org/project/amino_acid_feature_extraction)
[![Build Status](https://img.shields.io/travis/simonholmes001/amino_acid_feature_extraction.svg)](https://travis-ci.com/simonholmes001/amino_acid_feature_extraction)
NO[![slack](https://img.shields.io/badge/cookiecutter-Join%20on%20Slack-green?style=flat&logo=slack)](https://join.slack.com/t/cookie-cutter/shared_invite/enQtNzI0Mzg5NjE5Nzk5LTRlYWI2YTZhYmQ4YmU1Y2Q2NmE1ZjkwOGM0NDQyNTIwY2M4ZTgyNDVkNjMxMDdhZGI5ZGE5YmJjM2M3ODJlY2U)
[![docs](https://readthedocs.org/projects/amino-acid-feature-extraction/badge/?version=latest)](https://amino-acid-feature-extraction.readthedocs.io/en/latest/?badge=latest)
NO[![Code Qaulity](https://img.shields.io/scrutinizer/g/cookiecutter/cookiecutter.svg)](https://scrutinizer-ci.com/g/cookiecutter/cookiecutter/?branch=master)
[![Commits Since](https://img.shields.io/github/commits-since/simonholmes001/amino_acid_feature_extraction/v0.0.1.svg)](https://github.com/simonholmes001/amino_acid_feature_extraction/compare/v0.0.1...master)
[![Supported Implementations](https://img.shields.io/pypi/implementation/amino_acid_feature_extraction.svg)](https://pypi.org/project/amino_acid_feature_extraction)
[![Supported Verions](https://img.shields.io/pypi/pyversions/amino_acid_feature_extraction.svg)](https://pypi.org/project/amino_acid_feature_extraction)
[![Wheel](https://img.shields.io/pypi/wheel/amino_acid_feature_extraction.svg)](https://pypi.org/project/amino_acid_feature_extraction)
[![GitHub](https://pyup.io/repos/github/simonholmes001/amino_acid_feature_extraction/shield.svg)](https://pyup.io/repos/github/simonholmes001/amino_acid_feature_extraction/)
[![license](https://img.shields.io/pypi/l/sphinx_rtd_theme.svg)](https://pypi.python.org/pypi/sphinx_rtd_theme/)

* Free software: MIT license

## Requirements

This repo was developed using python 3.7. Other requirements include:

- Sphinx==1.8.5
- twine==1.14.0
- flake8==3.7.8
- tox==3.14.0

## Installation

`pip install amino_acid_feature_extraction`

For other installation methods, please see https://amino-acid-feature-extraction.readthedocs.io/en/latest/installation.html

## Documentation

Please refer to https://amino-acid-feature-extraction.readthedocs.io.

## Development

To run all the tests run:

`tox`

# Usage

### Feature Extraction & Pre-Processing

The `download_feature_extraction.sh` file performs four tasks:
- uses a FTP request to download the aaindex1 file (see [below](#aaindex))
- performs pre-processing steps on the downloaded file to extract the index information
- creates the folders necessary in the basic file structure to store the data (will create a `data` folder in which
the downloaded `aaindex1` file is stored & an `output` folder in which the extracted features are stored)
- combines the features extracted from pubchem (see [below](#below)) to the features extracted from the `aaindex1` file

<a name="below"></a>The user should also use the [pubchem_API script](https://pypi.org/project/pubchem-api/#description) to download the amino acid
features described [here](#features). The output file from this should be saved in the `output` folder.

# Background

## Amino Acids

(Source: https://en.wikipedia.org/wiki/Amino_acid)

Amino acids are the monomers that, when chemically joined together, create polypeptides and proteins. There are about 500 amino acids known, although only 22 occur in nature, of which 20 of these are encoded in the genetic material (the remaining two amino acids are encoded by variant codons and their use in nature is rare).
The &alpha;-carbon of an amino acid is a chiral atom (with the exception of glycine). However, D-isomers are very rare in nature, with the vast majority of amino acids in biological systems
being of the L-format.

As proteins are polymers of amino acids, the 3-dimensional conformations that proteins adopt is determined by the chemical properties of the amino acids that comprise the protein in question.
In order to find algorithms that accurately predict protein 3D shape from the 1D primary sequence of amino acids of a protein, it is pertinent to derive features from the chemical properties
of the amino acids themselves.

Amino acid codes:

**Charged (side chains often form salt bridges)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:|
| Arginine      | Arg | R | [6322](https://pubchem.ncbi.nlm.nih.gov/compound/6322) |
| Lysine      | Lys | K | [5962](https://pubchem.ncbi.nlm.nih.gov/compound/5962) |
| Aspartic Acid      | Asp | D | [5960](https://pubchem.ncbi.nlm.nih.gov/compound/5960) |
| Glutamic Acide      | Glu | E | [33032](https://pubchem.ncbi.nlm.nih.gov/compound/33032) |

**Polar (form hydrogen bonds as proton donors or acceptors)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:|
| Glutamine      | Gln | Q | [5961](https://pubchem.ncbi.nlm.nih.gov/compound/5961) |
| Asparagine      | Asn | N | [6267](https://pubchem.ncbi.nlm.nih.gov/compound/6267) |
| Histidine      | His | H | [6274](https://pubchem.ncbi.nlm.nih.gov/compound/6274) |
| Serine      | Ser | S | [5951](https://pubchem.ncbi.nlm.nih.gov/compound/5951) |
| Threonine      | Thr | T | [6288](https://pubchem.ncbi.nlm.nih.gov/compound/6288) |
| Cysteine    | Cys | C | [5862](https://pubchem.ncbi.nlm.nih.gov/compound/5862) |

**Polar (Amphipathic (often found at the surface of proteins or lipid membranes, sometimes also classified as polar)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:|
| Tryptophan      | Trp | W | [6305](https://pubchem.ncbi.nlm.nih.gov/compound/6305) |
| Tyrosine      | Tyr | Y | [6057](https://pubchem.ncbi.nlm.nih.gov/compound/6057) |
| Methionine      | Met | M | [6137](https://pubchem.ncbi.nlm.nih.gov/compound/6137) |

**Hydrophobic (normally buried inside the protein core)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:|
| Alanine      | Ala | A | [5950](https://pubchem.ncbi.nlm.nih.gov/compound/5950) |
| Isoleucine      | Ile | I | [6306](https://pubchem.ncbi.nlm.nih.gov/compound/6306) |
| Leucine     | Leu | L | [6106](https://pubchem.ncbi.nlm.nih.gov/compound/6106) |
| Phenylalanine     | Phe | F | [6140](https://pubchem.ncbi.nlm.nih.gov/compound/6140) |
| Valine | Val | V | [6287](https://pubchem.ncbi.nlm.nih.gov/compound/6287) |
| Proline    | Pro | P | [614](https://pubchem.ncbi.nlm.nih.gov/compound/614) |
| Glycine    | Gly | G | [750](https://pubchem.ncbi.nlm.nih.gov/compound/750) |

# Feature Extraction

## Sources

The first set of features for each of the amino acids was extracted from the [PubChem data base](https://pubchem.ncbi.nlm.nih.gov/)
using the [pubchem-api](https://pypi.org/project/pubchem-api/).

From this request, the following information was retrieved <a name="features"></a>:


| Property | Notes |
| :-------------: |:-------------:|
| MolecularWeight| The molecular weight is the sum of all atomic weights of the constituent atoms in a compound, measured in g/mol. In the absence of explicit isotope labelling, averaged natural abundance is assumed. If an atom bears an explicit isotope label, 100% isotopic purity is assumed at this location |
| XLogP| Computationally generated octanol-water partition coefficient or distribution coefficient. XLogP is used as a measure of hydrophilicity or hydrophobicity of a molecule |
|TPSA| Topological polar surface area, computed by the algorithm described in the paper by Ertl et al |
|Complexity|The molecular complexity rating of a compound, computed using the Bertz/Hendrickson/Ihlenfeldt formula |
|Charge| The total (or net) charge of a molecule |
|HBondDonorCount| Number of hydrogen-bond donors in the structure|
|HBondAcceptorCount| Number of hydrogen-bond acceptors in the structure|
|RotatableBondCount| Number of rotatable bonds|
|HeavyAtomCount| Number of non-hydrogen atoms|
|AtomStereoCount| Total number of atoms with tetrahedral (sp3) stereo [e.g., (R)- or (S)-configuration]|
|DefinedAtomStereoCount| Number of atoms with defined tetrahedral (sp3) stereo|
|Volume3D|Analytic volume of the first diverse conformer (default conformer) for a compound|
|XStericQuadrupole3D|The x component of the quadrupole moment (Qx) of the first diverse conformer (default conformer) for a compound|
|YStericQuadrupole3D|The y component of the quadrupole moment (Qy) of the first diverse conformer (default conformer) for a compound|
|ZStericQuadrupole3D|The z component of the quadrupole moment (Qz) of the first diverse conformer (default conformer) for a compound|
|FeatureCount3D|Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D)|
|FeatureAcceptorCount3D|Number of hydrogen-bond acceptors of a conformer|
|FeatureDonorCount3D|Number of hydrogen-bond donors of a conformer|
|FeatureAnionCount3D|Number of anionic centers (at pH 7) of a conformer|
|FeatureCationCount3D|Number of cationic centers (at pH 7) of a conformer |
|FeatureRingCount3D|Number of rings of a conformer|
|FeatureHydrophobeCount3D|Number of hydrophobes of a conformer|
|ConformerModelRMSD3D|Conformer sampling RMSD in Å|
|EffectiveRotorCount3D|Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D)|
|ConformerCount3D|The number of conformers in the conformer model for a compound|

#### Second Set of Features

The second set of features collected come from the <a name="aaindex"></a> [AAindex: Amino Acid Index Database](https://www.genome.jp/aaindex/aaindex_help.html).

At the time of writing (March, 2020), this database currently consists of 566 indices of physical-chemical information concerning the amino acids.
The data used here come from the aaindex1, aaindex2 & aaindex3 files which can be downloaded [here](ftp://ftp.genome.jp/pub/db/community/aaindex/).
Explanations for each of the indices used can be found for [aaindex1](https://www.genome.jp/aaindex/AAindex/list_of_indices), for [aaindex2](https://www.genome.jp/aaindex/AAindex/list_of_matrices)
& for [aaindex3](https://www.genome.jp/aaindex/AAindex/list_of_potentials). The downloaded files should be put in a folder called `data/`.





