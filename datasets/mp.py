from pymatgen.ext.matproj import MPRester
import json

def get_mp_cif(api_key, path):
    with MPRester(api_key=api_key) as mpr:
        data = mpr.query({'cif': {'$exists': True}, 'final_energy': {'$exists': True}}, ['material_id', 'cif', 'final_energy'])
    with open(path, 'w') as fout:
        json.dump(data, fout)
