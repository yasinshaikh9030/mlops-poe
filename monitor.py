import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame(
    {
        "age": [22, 25, 28, 30, 24, 27, 26, 29],
        "salary": [20000, 25000, 30000, 35000, 22000, 28000, 27000, 32000],
    }
)

current_data = pd.DataFrame(
    {
        "age": [35, 40, 38, 42, 36, 45, 39, 41],
        "salary": [50000, 60000, 55000, 65000, 52000, 70000, 58000, 62000],
    }
)

report = Report([DataDriftPreset()])

result = report.run(reference_data=reference_data, current_data=current_data)

result.save_html("monitoring_report.html")

print("Monitoring completed successfully!")
print("Report saved as monitoring_report.html")
