# Import functions
from cohortextractor import (
    StudyDefinition, 
    Measure,
    patients, 
)

from codelists import *

index_date = "2020-01-01"

# Specifiy study defeinition
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "today"},
        "rate": "universal",
    },
    
    # define the study index date
    index_date = index_date,


    # This line defines the study population
    population = patients.satisfying("(NOT died) AND (registered)",        
        died = patients.died_from_any_cause(
		    on_or_before=index_date,
		    returning="binary_flag"
	    ),
        registered = patients.registered_as_of(index_date),
    ),

    age=patients.age_as_of(index_date,
        return_expectations={
        "rate" : "universal",
        "int" : {"distribution" : "population_ages"}
        }),

    age_group = patients.categorised_as({
            "0": "DEFAULT",
            "0 - under 16": """ age < 16""",
            "16 - under 30": """ age >= 16 AND age < 30""",
            "30 - under 40": """ age >= 30 AND age < 40""",
            "40 - under 50": """ age >= 40 AND age < 50""",
            "50 - under 55": """ age >= 50 AND age < 55""",
            "55 - under 60": """ age >= 55 AND age < 60""",
            "60 - under 65": """ age >= 60 AND age < 65""",
            "65 - under 70": """ age >= 65 AND age < 70""",
            "70 - under 75": """ age >= 70 AND age < 75""",
            "75 - under 80": """ age >= 75 AND age < 80""",
            "80 - under 85": """ age >= 80 AND age < 85""",
            "85 plus": """ age >=  85""", 
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0 - under 16": 0.05,
                    "16 - under 30": 0.1,
                    "30 - under 40": 0.1,
                    "40 - under 50": 0.1,
                    "50 - under 55": 0.1,
                    "55 - under 60": 0.05,
                    "60 - under 65": 0.1,
                    "65 - under 70": 0.1,
                    "70 - under 75": 0.05,
                    "75 - under 80": 0.1,
                    "80 - under 85": 0.1,
                    "85 plus": 0.05,
                }
            },
        },),

    stp = patients.registered_practice_as_of("index_date",
        returning="stp_code",
        return_expectations={
             "category": {"ratios": {"STP1": 0.5, "STP2": 0.5}},
        },),

    first_dose=patients.with_these_clinical_events(first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    second_dose=patients.with_these_clinical_events(second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    any_first_dose=patients.with_these_clinical_events(any_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    any_second_dose=patients.with_these_clinical_events(any_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    az_first_dose=patients.with_these_clinical_events(az_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    az_second_dose=patients.with_these_clinical_events(az_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    pf_first_dose=patients.with_these_clinical_events(pf_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    pf_second_dose=patients.with_these_clinical_events(pf_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    mo_first_dose=patients.with_these_clinical_events(mo_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    mo_second_dose=patients.with_these_clinical_events(mo_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    nx_first_dose=patients.with_these_clinical_events(nx_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    nx_second_dose=patients.with_these_clinical_events(nx_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    jn_first_dose=patients.with_these_clinical_events(jn_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    jn_second_dose=patients.with_these_clinical_events(jn_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    gs_first_dose=patients.with_these_clinical_events(gs_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    gs_second_dose=patients.with_these_clinical_events(gs_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    vl_first_dose=patients.with_these_clinical_events(vl_first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    vl_second_dose=patients.with_these_clinical_events(vl_second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    )

measures = [
    Measure(id="first_dose_stp",
        numerator="first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="second_dose_stp",
        numerator="second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="vl_second_dose_stp",
        numerator="vl_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="vl_first_dose_stp",
        numerator="vl_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="pf_second_dose_stp",
        numerator="pf_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="pf_first_dose_stp",
        numerator="pf_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="nx_second_dose_stp",
        numerator="nx_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="nx_first_dose_stp",
        numerator="nx_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="mo_second_dose_stp",
        numerator="mo_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="mo_first_dose_stp",
        numerator="mo_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="jn_second_dose_stp",
        numerator="jn_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="jn_first_dose_stp",
        numerator="jn_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="gs_second_dose_stp",
        numerator="gs_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="gs_first_dose_stp",
        numerator="gs_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="az_second_dose_stp",
        numerator="az_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="az_first_dose_stp",
        numerator="az_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="any_second_dose_stp",
        numerator="any_second_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),

    Measure(id="any_first_dose_stp",
        numerator="any_first_dose",
        denominator="population",
        group_by = ["stp", "age_group"]),
    ]
