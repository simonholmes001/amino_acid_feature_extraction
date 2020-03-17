# Amino Acid Feature Extraction

[![Build Status](https://img.shields.io/travis/simonholmes001/amino_acid_feature_extraction.svg)](https://travis-ci.com/simonholmes001/amino_acid_feature_extraction)
[![docs](https://readthedocs.org/projects/amino-acid-feature-extraction/badge/?version=latest)](https://amino-acid-feature-extraction.readthedocs.io/en/latest/?badge=latest)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/build.png?b=master)](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/build-status/master)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/simonholmes001/amino_acid_feature_extraction/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)
[![license](https://img.shields.io/pypi/l/sphinx_rtd_theme.svg)](https://pypi.python.org/pypi/sphinx_rtd_theme/)

* Free software: MIT license

## Requirements

This project was developed in python3.7. All other requirements are installed via the creation
of a conda virtual environment when the `feature_extraction.sh` script is run.

## Documentation

Please refer to https://amino-acid-feature-extraction.readthedocs.io.

## Development

(Work in progress, unit tests not completed)
To run all the tests run:

`tox`

# Usage

### Feature Extraction & Pre-Processing

To run the project, download the project files from the github repository using
the following command:

`git clone https://github.com/simonholmes001/amino_acid_feature_extraction.git`

`cd` into the folder containing the repo & run the following command to execute the project:

`bash -i feature_extraction.sh`

Running the `feature_extraction.sh` script provides all of the functionalities required in
order to create a dataset of amino acid chemical & physical properties:
- Creates a virtual environment in which to run the code
- FTP request to download the aaindex1 file (see [below](#aaindex))
- API call to the [PubChem database](https://pubchem.ncbi.nlm.nih.gov/) to extract physical-chemical data (see [here](#pubchem))
- Data pre-processing steps to extract the index information
- Creates the folder structure necessary in the basic file structure to store the data (will create a `data` folder in which
the downloaded `aaindex1` file is stored & an `output` folder in which the extracted features are stored)
- Combines the features extracted from pubchem (see [below](#below)) to the features extracted from the `aaindex1` file
- Standardises the features
- Saves all the data in a csv file & in a numpy array

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

**Polar (Amphipathic (often found at the surface of proteins or lipid membranes, sometimes also classified as polar)**:
| Serine      | Ser | S | [5951](https://pubchem.ncbi.nlm.nih.gov/compound/5951) |
| Threonine      | Thr | T | [6288](https://pubchem.ncbi.nlm.nih.gov/compound/6288) |
| Cysteine    | Cys | C | [5862](https://pubchem.ncbi.nlm.nih.gov/compound/5862) |


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

## Sources <a name="pubchem"></a>

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
The data used here come from the aaindex1 file, which can be downloaded [here](ftp://ftp.genome.jp/pub/db/community/aaindex/).
Explanations for this index can be found here [aaindex1](https://www.genome.jp/aaindex/AAindex/list_of_indices).
