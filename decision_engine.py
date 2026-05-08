import pandas as pd

df = pd.read_csv("readiness_data.csv - Sheet1.csv")

import pandas as pd

df = pd.read_csv("readiness_data.csv - Sheet1.csv")

df.columns = df.columns.str.strip()

results = []

for index, row in df.iterrows():

    energy = row["energy"]
    soreness = row["soreness"]

if energy <= 2:

    status = "MODIFY"
    reason = "Low energy"
    action = "Reduce training intensity"
    risk = "Moderate"

elif soreness >= 4:

    status = "MODIFY"
    reason = "High soreness"
    action = "Monitor recovery and workload"
    risk = "High"


elif row["movement"] <= 1:

    status = "MODIFY"
    reason = "Poor movement quality"
    action = "Add corrective movement work"
    risk = "Moderate"


else:

    status = "READY"
    reason = "Stable"
    action = "Continue normal training"
    risk = "Low"




 

results.append({
    "name": row["name"],
    "environment": row["environment"],
    "energy": energy,
    "soreness": soreness,
    "status": status,
    "reason": reason,
    "action": action,
    "risk": risk

})

results_df = pd.DataFrame(results)

results_df.to_csv("results.csv", index=False)

print("\nREADINESS DECISION OUTPUT\n")

for index, row in results_df.iterrows():

    print(
        row["name"],
        "|",
        row["environment"],
        "|",
        row["status"],
        "|",
        row["reason"],
        "|",
        row["action"], 
        "|",
        row["risk"],

    )




