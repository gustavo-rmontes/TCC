import pandas as pd
from dbfread import DBF


def convert_dbf_to_csv(dbf_od_path: str, od_year: str) -> None:
    """
    Convert a DBF file to CSV format and save it to data/OD/ODs_clean 

    Args:
        dbf_od_path (str): Path to the DBF file.
        od_year (str): Year of the OD research.
    """
    dbf = DBF(dbf_od_path)
    df = pd.DataFrame(iter(dbf))

    clean_folder = '../../data/OD/ODs_clean/'
    df.to_csv(clean_folder+'OD_'+od_year+'.csv', index=False)
