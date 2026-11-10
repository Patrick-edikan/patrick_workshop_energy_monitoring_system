"""
CTE 213 FINAL PROJECT
WORKSHOP ENERGY MONITORING, COST ESTIMATION AND MANAGEMENT SYSTEM

Author: Patrick Joseph Edikan
Department: Mechatronics Engineering
Level: ND II
Institution: Yaba College of Technology (YABATECH)

This program estimates workshop electricity consumption and cost.
The PLC energy-saving section is a software simulation only.
"""

import csv
from datetime import datetime


# -------------------- CALCULATION FUNCTIONS --------------------

def calculate_energy(power_watts, operating_hours):
    """Return energy consumption in kilowatt-hours (kWh)."""
    return (power_watts / 1000) * operating_hours


def calculate_cost(energy_kwh, tariff_per_kwh):
    """Return electricity cost in Naira."""
    return energy_kwh * tariff_per_kwh


def classify_machine(power_watts):
    """Classify a machine using its power rating."""
    if power_watts > 1500:
        return "High Power"
    elif power_watts > 800:
        return "Medium Power"
    else:
        return "Low Power"


def classify_workshop(total_energy):
    """Give a simple daily workshop energy-performance status."""
    if total_energy > 20:
        return "HIGH ENERGY CONSUMPTION"
    elif total_energy > 10:
        return "MEDIUM ENERGY CONSUMPTION"
    else:
        return "LOW ENERGY CONSUMPTION"


# -------------------- INPUT VALIDATION FUNCTIONS --------------------

def get_positive_integer(prompt):
    """Accept only a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a whole number, for example 3.")


def get_positive_number(prompt, allow_zero=False):
    """Accept a valid number; optionally allow zero."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0 or (allow_zero and value == 0):
                return value
            if allow_zero:
                print("Please enter zero or a positive number.")
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a number, for example 750 or 2.5.")


def get_machine_hours(prompt):
    """Accept operating hours from zero to 24."""
    while True:
        try:
            hours = float(input(prompt))
            if 0 <= hours <= 24:
                return hours
            print("Operating hours must be between 0 and 24.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 24.")


# -------------------- REPORT EXPORT FEATURE --------------------

def export_report(machines, tariff, total_energy, daily_cost,
                  monthly_energy, monthly_cost, total_saving):
    """Save the machine report and workshop summary as a CSV file."""
    filename = "workshop_energy_report.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["WORKSHOP ENERGY MONITORING REPORT"])
            writer.writerow(["Prepared by", "Patrick Joseph Edikan"])
            writer.writerow(["Department", "Mechatronics Engineering"])
            writer.writerow(["Institution", "Yaba College of Technology"])
            writer.writerow(["Report date", datetime.now().strftime("%Y-%m-%d %H:%M")])
            writer.writerow([])
            writer.writerow([
                "Machine", "Power (W)", "Hours/day", "Energy (kWh)",
                "Daily Cost (Naira)", "Power Classification"
            ])

            for machine in machines:
                writer.writerow([
                    machine["name"],
                    machine["power"],
                    machine["hours"],
                    round(machine["energy"], 2),
                    round(calculate_cost(machine["energy"], tariff), 2),
                    machine["classification"]
                ])

            writer.writerow([])
            writer.writerow(["Electricity tariff (Naira/kWh)", tariff])
            writer.writerow(["Total daily energy (kWh)", round(total_energy, 2)])
            writer.writerow(["Total daily cost (Naira)", round(daily_cost, 2)])
            writer.writerow(["Monthly energy (kWh)", round(monthly_energy, 2)])
            writer.writerow(["Monthly cost (Naira)", round(monthly_cost, 2)])
            writer.writerow(["Potential daily energy saving (kWh)", round(total_saving, 2)])
            writer.writerow([
                "Potential daily money saving (Naira)",
                round(calculate_cost(total_saving, tariff), 2)
            ])

        print(f"\nReport successfully saved as {filename}.")
    except OSError as error:
        print("The report could not be saved:", error)


# -------------------- MAIN PROGRAM --------------------

def main():
    print("=" * 60)
    print(" WORKSHOP ENERGY MONITORING, COST ESTIMATION")
    print("             AND MANAGEMENT SYSTEM")
    print("=" * 60)
    print("Developed by: Patrick Joseph Edikan")
    print("Department: Mechatronics Engineering")
    print("Level: ND II")
    print("Institution: Yaba College of Technology (YABATECH)")
    print("-" * 60)

    # Lists store the details of all workshop machines.
    machines = []

    number_of_machines = get_positive_integer(
        "\nEnter the number of workshop machines: "
    )

    # Collect information for each machine.
    for index in range(number_of_machines):
        print(f"\nMACHINE {index + 1}")

        while True:
            name = input("Enter machine name: ").strip()
            if name:
                break
            print("Machine name cannot be empty.")

        power = get_positive_number("Enter power rating in watts: ")
        hours = get_machine_hours("Enter daily operating hours (0-24): ")

        energy = calculate_energy(power, hours)

        machine = {
            "name": name,
            "power": power,
            "hours": hours,
            "energy": energy,
            "classification": classify_machine(power)
        }
        machines.append(machine)
        print(f"{name} has been recorded successfully.")

    # Obtain the user's local electricity tariff.
    tariff = get_positive_number(
        "\nEnter electricity tariff in Naira per kWh: ",
        allow_zero=True
    )

    # Calculate total workshop energy and cost.
    total_energy = sum(machine["energy"] for machine in machines)
    daily_cost = calculate_cost(total_energy, tariff)
    monthly_energy = total_energy * 30
    monthly_cost = daily_cost * 30

    # Display the energy report for each machine.
    print("\n" + "=" * 60)
    print("                DAILY MACHINE REPORT")
    print("=" * 60)

    for machine in machines:
        machine_cost = calculate_cost(machine["energy"], tariff)
        print(f"\nMachine: {machine['name']}")
        print(f"Power rating: {machine['power']:.2f} W")
        print(f"Operating hours: {machine['hours']:.2f} hours")
        print(f"Energy consumption: {machine['energy']:.2f} kWh")
        print(f"Daily electricity cost: N{machine_cost:,.2f}")
        print(f"Power classification: {machine['classification']}")

    # Identify the machine with the highest energy consumption.
    highest_machine = max(machines, key=lambda item: item["energy"])

    # Count machines whose power rating is above 1000 watts.
    machines_above_1000w = sum(
        1 for machine in machines if machine["power"] > 1000
    )

    # Display the overall workshop summary.
    print("\n" + "=" * 60)
    print("                  WORKSHOP SUMMARY")
    print("=" * 60)
    print(f"Total daily energy: {total_energy:.2f} kWh")
    print(f"Total daily electricity cost: N{daily_cost:,.2f}")
    print(f"Estimated monthly energy (30 days): {monthly_energy:.2f} kWh")
    print(f"Estimated monthly cost (30 days): N{monthly_cost:,.2f}")
    print(f"Highest energy-consuming machine: {highest_machine['name']}")
    print(f"Energy used by that machine: {highest_machine['energy']:.2f} kWh")
    print(f"Machines above 1000 W: {machines_above_1000w}")
    print(f"Workshop status: {classify_workshop(total_energy)}")

    # PLC-inspired energy-saving simulation.
    # Assumption: eligible machines operate for one fewer hour per day,
    # or for their full operating time if it is less than one hour.
    print("\n" + "=" * 60)
    print("           PLC ENERGY-SAVING SIMULATION")
    print("=" * 60)
    print("Simulation: reduce operating time by up to one hour")
    print("for each machine rated above 1000 W.")
    print("This is a software estimate, not a real PLC control signal.")

    total_saving = 0

    for machine in machines:
        if machine["power"] > 1000 and machine["hours"] > 0:
            reduced_hours = min(1, machine["hours"])
            saving = calculate_energy(machine["power"], reduced_hours)
            total_saving += saving

            print(f"\nMachine: {machine['name']}")
            print(f"Simulated reduction: {reduced_hours:.2f} hour(s)")
            print(f"Estimated energy saving: {saving:.2f} kWh")

    daily_saving = calculate_cost(total_saving, tariff)
    monthly_saving = daily_saving * 30
    remaining_energy = total_energy - total_saving
    remaining_cost = calculate_cost(remaining_energy, tariff)

    print("\n" + "=" * 60)
    print("                   SAVINGS SUMMARY")
    print("=" * 60)
    print(f"Potential daily energy saving: {total_saving:.2f} kWh")
    print(f"Potential daily money saving: N{daily_saving:,.2f}")
    print(f"Potential monthly money saving: N{monthly_saving:,.2f}")
    print(f"Estimated energy after saving: {remaining_energy:.2f} kWh")
    print(f"Estimated daily cost after saving: N{remaining_cost:,.2f}")

    # Ask whether the user wants to export the report.
    while True:
        choice = input("\nSave the report as a CSV file? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            export_report(
                machines, tariff, total_energy, daily_cost,
                monthly_energy, monthly_cost, total_saving
            )
            break
        elif choice in ("no", "n"):
            print("Report was not exported.")
            break
        else:
            print("Please enter yes or no.")

    print("\n" + "=" * 60)
    print("Thank you for using the Workshop Energy Monitoring")
    print("and Management System.")
    print("Developed by Patrick Joseph Edikan.")
    print("=" * 60)


# Start the program.
if __name__ == "__main__":
    main()
