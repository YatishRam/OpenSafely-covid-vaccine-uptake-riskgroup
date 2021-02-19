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
    population = patients.satisfying(
        """
        age >= 16 AND 
        (NOT died) AND
        (registered) AND
        (diab)
        """,        
        died = patients.died_from_any_cause(
		    on_or_before=index_date,
		    returning="binary_flag"
	    ),
        pop_age = patients.age_as_of(index_date),
        registered = patients.registered_as_of(index_date),
        diab = patients.with_these_clinical_events(diab_code,
                                                        between = ["index_date", "index_date + 1 month"],
                                                        returning="binary_flag",
                                                        return_expectations= { "incidence": 0.6 },
                                                    )
    ),

    age=patients.age_as_of(index_date,
        return_expectations={
        "rate" : "universal",
        "int" : {"distribution" : "population_ages"}
        }),

    age_group = patients.categorised_as({
            "0": "DEFAULT",
            "16 - under 40": " age >= 16 AND age < 40",
            "40 - under 50": " age >= 40 AND age < 50",
            "50 - under 65": " age >= 50 AND age < 65",
            "65 plus": " age >= 65",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "16 - under 40": 0.5,
                    "40 - under 50": 0.125,
                    "50 - under 65": 0.25,
                    "65 plus": 0.125,
                }
            },
        },
    ),

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
    ]
