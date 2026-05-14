# Warehouse_safety_ai
An AI-based safety monitoring system that uses 3D depth data to detect hazards and visualize them
 The Core Logic
Object Identification: Categorizes items like Humans, Boxes, and Pallets using labels.

Safety Threshold: Implements a strict 1.0-meter proximity limit.

Volume Filter: Ignores small objects (noise) to prevent unnecessary stops, focusing only on significant physical hazards.

Visualizations
Generates a 3D Occupancy Visualization (Top-Down view):

Red Dots: Immediate hazards within the 1.0m limit.

Green Dots: Safe objects outside the danger zone.

Blue Dots: Small objects filtered out by the volume threshold.

Dashed Red Line: The critical safety boundary at 1.0m.
