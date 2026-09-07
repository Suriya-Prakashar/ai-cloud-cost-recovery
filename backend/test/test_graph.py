from app.graph.graph import cost_recovery_graph


result = cost_recovery_graph.invoke({})


print("\n========== COST RECOVERY GRAPH ==========")


print("\nBilling Data:")
print(result["billing_data"])


print("\nCost Analysis:")
print(result["cost_analysis"])


print("\nAnomaly:")
print(result["anomaly"])


print("\nService Analysis:")
print(result["service_analysis"])



print("\nInvestigated Resources:")

for resource in result.get(
    "investigated_resources",
    []
):
    print(resource)


print("\nEvidence:")

for item in result.get(
    "evidence",
    []
):
    print(item)

print("\nRoot Cause:")
print(result["root_cause"])