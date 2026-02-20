import csv
from fastapi.responses import FileResponse

def export_to_csv(records):
    filename = "weather_export.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Temperature", "Humidity", "Description"])

        for r in records:
            writer.writerow([r.location, r.avg_temperature, r.humidity, r.description])

    return filename