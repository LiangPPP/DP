from PETWorks import PETAnonymization, output
from PETWorks.attributetypes import *

originalData = "NHANES_hierarchy/NHANES.csv"
dataHierarchy = "NHANES_hierarchy/NHANES_hierarchy"

attributeTypes = {
    "RIAGENDR": QUASI_IDENTIFIER,
    "RIDAGEYR": QUASI_IDENTIFIER,
    "RIDRETH1": QUASI_IDENTIFIER,
    "DMDEDUC2": SENSITIVE_ATTRIBUTE,
    "DMDMARTL": SENSITIVE_ATTRIBUTE,
}

result = PETAnonymization(
    originalData,
    "k-anonymity",
    dataHierarchy,
    attributeTypes,
    maxSuppressionRate=0.6,
    k=6,
)

output(result, "output.csv")