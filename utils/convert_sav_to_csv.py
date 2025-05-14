"""
This file converts .sav files to .csv and saving it in './data/OD/ODS' 
"""

import pyreadstat

def od_sav_to_csv(od_path:str, od_year:str) -> None:
    """
    Saves the .sav OD file as a .csv file
    
    Args:
    od_path(string): OD .sav file location[path]
    od_year(string): OD research year 
    """

    clean_ods_path = "../data/OD/ODS/OD_"

    df, _ = pyreadstat.read_sav(od_path)
    df.to_csv(clean_ods_path + od_year + ".csv", index=False)


# ODs to be converted
od_07_path = "../data/OD/OD-2007/Banco de Dados-OD2007/OD_2007_v2d.sav"
od_97_path = "../data/OD/OD-1997/Banco de Dados/Domiciliar/OD97Zona.sav"
od_87_path = "../data/OD/OD-1987/Banco de Dados/OD_1987.sav"
od_77_path = "../data/OD/OD-1977/Banco de Dados/od77_CD.sav"

od_sav_to_csv(od_07_path, "2007")
od_sav_to_csv(od_97_path, "1997")
od_sav_to_csv(od_87_path, "1987")
od_sav_to_csv(od_77_path, "1977")