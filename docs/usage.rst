=====
Usage
=====

To run the project, download the project files from the github repository using
the following command::

    git clone https://github.com/simonholmes001/amino_acid_feature_extraction.git

::

    cd

into the folder containing the repo & run the following command to execute the project::

    bash -i feature_extraction.sh

Running the::

    feature_extraction.sh

script provides all of the functionalities required in
order to create a dataset of amino acid chemical & physical properties:

- Creates a virtual environment in which to run the code
- FTP request to download the aaindex1 file (see [below](#aaindex))
- API call to the [PubChem database](https://pubchem.ncbi.nlm.nih.gov/) to extract physical-chemical data (see [here](#pubchem))
- Data pre-processing steps to extract the index information
- Creates the folder structure necessary in the basic file structure to store the data (will create a ./data folder in which the downloaded `aaindex1` file is stored & an ./output folder in which the extracted features are stored)
- Combines the features extracted from PubChem to the features extracted from the `aaindex1` file
- Standardises the features
- Saves all the data in a csv file & in a numpy array
