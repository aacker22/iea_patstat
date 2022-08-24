# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:06:29 2020

@author: TAV_M
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:42:59 2020

@author: TAV_M
"""

import os
import time
import pandas as pd
import datetime
import numpy as np
import csv

folder = r'C:\Repos\cetp\Patents'
os.chdir(folder)

## To be run just once
patents = pd.DataFrame(pd.read_csv("tls201_appln2.csv", sep = ",",  usecols=['appln_id','appln_auth','appln_nr','appln_kind','appln_filing_date','appln_filing_year','appln_nr_epodoc','appln_nr_original','ipr_type','receiving_office','internat_appln_id','int_phase','reg_phase','nat_phase','earliest_filing_date','earliest_filing_year','earliest_filing_id','earliest_publn_date','earliest_publn_year','earliest_pat_publn_id','granted','docdb_family_id','inpadoc_family_id','docdb_family_size','nb_citing_docdb_fam','nb_applicants','nb_inventors'], index_col = False))
patentsTitle = pd.DataFrame(pd.read_csv("tls202_appln_title.csv", sep = ",", usecols=['appln_id','appln_title_lg','appln_title'], index_col = False))
pivot="appln_id"
patentsTitleAll=patents.merge(patentsTitle,on=pivot,how="left")
dfCountriesAccessT4 = dfCountriesAccessT4.rename(columns={"Id":"Country"})
patentsTitleAll.to_csv("patents_out.csv",",", index=False)

from pandas_profiling import ProfileReport

profile = ProfileReport(patentsTitleAll, title="Pandas Profiling Report")