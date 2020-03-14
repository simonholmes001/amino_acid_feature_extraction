import pubchem_api

from pubchem_api import pubchem_api

base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
compound_cid_selector = "compound/cid/"
# search_id = "6322/"
property = "property/"
# output_property = "MolecularWeight/"
output_format = "CSV"
output_file_name = "test_data"
property_list = ["MolecularWeight", "XLogP", "TPSA", "Complexity", "Charge", "HBondDonorCount", "HBondAcceptorCount",
             "RotatableBondCount", "HeavyAtomCount", "AtomStereoCount", "DefinedAtomStereoCount", "Volume3D", "XStericQuadrupole3D",
             "YStericQuadrupole3D", "ZStericQuadrupole3D", "FeatureCount3D", "FeatureAcceptorCount3D", "FeatureDonorCount3D",
             "FeatureAnionCount3D", "FeatureCationCount3D", "FeatureRingCount3D", "FeatureHydrophobeCount3D", "ConformerModelRMSD3D",
             "EffectiveRotorCount3D", "ConformerCount3D"]

cid_list = ["5950", "6322", "6267", "5960", "5862", "5961", "33032", "750", "6274", "6306", "6106", "5962",
            "6137", "6140", "614", "5951", "6288", "6305", "6057", "6287"]

search_id = ','.join(cid_list)+"/"
output_property = ','.join(property_list)+"/"

pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)
