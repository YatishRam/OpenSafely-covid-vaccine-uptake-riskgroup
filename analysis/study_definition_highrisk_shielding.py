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
        (NOT died) AND 
        (registered) AND 
        (shield)
        """,
        died = patients.died_from_any_cause(
		    on_or_before=index_date,
		    returning="binary_flag"
	    ),
        registered = patients.registered_as_of(index_date),
        shield = patients.with_these_clinical_events(shield_code,
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
            "0 - under 16": """ age < 16""",
            "16 - under 40": """ age >= 16 AND age < 40""",
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
                    "16 - under 40": 0.1,
                    "40 - under 50": 0.1,
                    "50 - under 55": 0.1,
                    "55 - under 60": 0.1,
                    "60 - under 65": 0.1,
                    "65 - under 70": 0.1,
                    "70 - under 75": 0.1,
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