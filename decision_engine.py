import pandas as pd

df = pd.read_csv("readiness_data.csv - Sheet1.csv")

import pandas as pd

df = pd.read_csv("readiness_data.csv - Sheet1.csv")

df.columns = df.columns.str.strip()

results = []

for index, row in df.iterrows():

    energy = row["energy"]
    soreness = row["soreness"]

    if energy <= 2 or soreness >= 4:

        status = "MODIFY"
        reason = "Low energy or high soreness"

    else:

        status = "READY"
        reason = "Stable"

    results.append({
        "name": row["name"],
        "status": status,
        "reason": reason
    })

results_df = pd.DataFrame(results)

results_df.to_csv("results.csv", index=False)

print(results_df)



