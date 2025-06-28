print("=== Solar Production Calculator ===")

power_kw = float(input("Installed power (kW): "))
sun_hours = float(input("Average daily sun hours: "))
efficiency_percent = float(input("System efficiency (% as number, e.g., 80): "))

efficiency = efficiency_percent / 100  # yüzdeyi ondalığa çevir

daily_production = power_kw * sun_hours * efficiency
monthly_production = daily_production * 30

print(f"\nEstimated Daily Production: {daily_production:.2f} kWh")
print(f"Estimated Monthly Production: {monthly_production:.2f} kWh")

input("\nPress Enter to exit...")
