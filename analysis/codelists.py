from cohortextractor import (
    codelist,
    codelist_from_csv
)

# Vaccination doses
first_dose_code = codelist("COVRX1_COD", system="snomed")
second_dose_code = codelist("COVRX2_COD", system="snomed")

az_first_dose_code = codelist("AZD1RX_COD", system="snomed")
az_second_dose_code = codelist("AZD2RX_COD", system="snomed")

pf_first_dose_code = codelist("PFD1RX_COD", system="snomed")
pf_second_dose_code = codelist("PFD2RX_COD", system="snomed")

mo_first_dose_code = codelist("MOD1RX_COD", system="snomed")
mo_second_dose_code = codelist("MOD2RX_COD", system="snomed")

nx_first_dose_code = codelist("NXD1RX_COD", system="snomed")
nx_second_dose_code = codelist("NXD2RX_COD", system="snomed")

jn_first_dose_code = codelist("JND1RX_COD", system="snomed")
jn_second_dose_code = codelist("JND2RX_COD", system="snomed")

gs_first_dose_code = codelist("GSD1RX_COD", system="snomed")
gs_second_dose_code = codelist("GSD2RX_COD", system="snomed")

vl_first_dose_code = codelist("VLD1RX_COD", system="snomed")
vl_second_dose_code = codelist("VLD2RX_COD", system="snomed")

# Risk groups
chd_code = codelist("CHD_COV_COD", system="snomed")
resp_code = codelist("RESP_COV_COD", system="snomed")
ckd_code = codelist("CKD_COV_COD", system="snomed")
cld_code = codelist("CLD_COD", system="snomed")
diab_code = codelist("DIAB_COD", system="snomed")
immdx_code = codelist("IMMDX_COV_COD", system="snomed")
cns_code = codelist("CNS_COV_COD", system="snomed")
spln_code = codelist("SPLN_COV_COD", system="snomed")
obesity_code = codelist("SEV_OBESITY", system="snomed")
learndis_code = codelist("LEARNDIS_COD", system="snomed")
mental_code = codelist("SEV_MENTAL_COD", system="snomed")

clinical_riskgroup_codes = codelist_from_csv("codelists-local/clinical-riskgroup-disease.csv",
                                    system="snomed",
                                    column="code",)

all_riskgroup_codes = codelist_from_csv("codelists-local/all-riskgroup-disease.csv",
                                    system="snomed",
                                    column="code",)

# Covid shielding
shield_code = codelist("SHIELD_COD", system="snomed")

# Household member of shielding patient
hhld_code = codelist("HHLD_IMDEF", system="snomed")

# Healthcare worker
hcw_carehome_code = codelist("CAREHOME_COD", system="snomed")
hcw_nursehome_code = codelist("NURSEHOME_COD", system="snomed")
hcw_domcare_code = codelist("DOMCARE_COD", system="snomed")

# Carer
carer_code = codelist("CARER_COD", system="snomed")

# Patient in long term residential care
longres_code = codelist("LONGRES_COD", system="snomed")