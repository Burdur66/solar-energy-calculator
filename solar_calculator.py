# Solar Production Calculator
# Bu program güneş paneli sisteminizin tahmini günlük ve aylık enerji üretimini hesaplar.

def solar_production_calculator():
    print("=== Solar Production Calculator ===")

    # Kurulu güç al (kW)
    installed_capacity = float(input("Kurulu güç (kW): "))

    # Günlük ortalama güneş saati al
    daily_sun_hours = float(input("Günlük ortalama güneş saati: "))

    # Sistem verimi al (% olarak), sonra 0-1 aralığına dönüştür
    system_efficiency_percent = float(input("Sistem verimi (% olarak, örn: 80): "))
    system_efficiency = system_efficiency_percent / 100

    # Günlük tahmini üretim hesapla
    daily_production = installed_capacity * daily_sun_hours * system_efficiency

    # Aylık tahmini üretim hesapla (30 gün üzerinden)
    monthly_production = daily_production * 30

    # Sonuçları yazdır
    print(f"\nTahmini Günlük Üretim: {daily_production:.2f} kWh")
    print(f"Tahmini Aylık Üretim: {monthly_production:.2f} kWh")

if __name__ == "__main__":
    solar_production_calculator()
