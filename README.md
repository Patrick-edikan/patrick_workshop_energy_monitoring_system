# Workshop Energy Monitoring, Cost Estimation and Management System

**Author:** Patrick Joseph Edikan  
**Institution:** Yaba College of Technology (YABATECH)  
**Department:** Mechatronics Engineering  
**Level:** ND II  
**Course:** CTE 213

## What it does

This Python program estimates the daily and monthly electrical energy consumption and electricity cost of machines in a workshop. It accepts each machine's name, power rating and daily operating hours, then produces individual machine reports and a workshop summary.

It also classifies machines by power rating, identifies the machine with the highest energy consumption, and estimates possible savings using a PLC-inspired operating-time reduction simulation.

## How to run it

1. Install Python 3.
2. Save the program as `workshop_energy_monitor.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python workshop_energy_monitor.py
```

On Android, the program can be run using Pydroid 3.

## Sample output

A sample calculation using two machines:

- Grinding machine: 1500 W, 4 hours/day
- Drilling machine: 750 W, 3 hours/day
- Electricity tariff: N100 per kWh

The program calculates:

- Grinding machine: 6.00 kWh/day, N600.00/day
- Drilling machine: 2.25 kWh/day, N225.00/day
- Total: 8.25 kWh/day, N825.00/day
- Estimated monthly energy: 247.50 kWh
- Estimated monthly cost: N24,750.00

The PLC-inspired simulation reduces the daily operating time of machines rated above 1000 W by up to one hour. In this example, the grinding machine's estimated saving is 1.50 kWh/day, equivalent to N150.00/day at the example tariff.

## My own twist

I added a PLC-inspired energy-saving simulation. It estimates the energy and money that could be saved by reducing the operating time of machines rated above 1000 W by up to one hour per day.

I also added CSV report export, allowing the workshop results to be saved and opened in spreadsheet applications such as Microsoft Excel.

**Note:** The PLC feature is a software simulation. It does not communicate with or control a physical PLC or machine. The energy and cost figures are estimates based on the power ratings, operating hours and tariff entered by the user. Monthly figures assume 30 days of similar operation.

## What I learned

I practised writing Python functions, storing machine data in lists, using loops and conditional statements, validating user input, and calculating energy consumption in kWh. I also learned how a simple software program can support energy monitoring and management in a workshop.

## Author

Patrick Joseph Edikan  
ND II, Mechatronics Engineering  
Yaba College of Technology (YABATECH)
