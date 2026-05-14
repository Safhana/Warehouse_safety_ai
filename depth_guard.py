import numpy as np
import matplotlib.pyplot as plt
import time

class WarehouseSafetyAI:
    def __init__(self):
        self.LIMIT_M = 1.0      
        self.MIN_VOL = 20        
        self.ZONE_A = 2.0        
        self.alarm_active = False

    def get_3d_volume(self, bbox):
        width, height = bbox[2], bbox[3]
        return (width * height) / 10 

    def process_sensor_data(self, data_feed):
        print("\n" + "!"*50)
        print("  SYSTEM STATUS: WAREHOUSE OCCUPANCY MONITOR")
        print("!"*50)
        
        x_points, z_points, color_map = [], [], []

        for item in data_feed:
            oid = item["id"]
            name = item["label"]
            z_dist = item["depth"]
            vol = self.get_3d_volume(item["bbox"])

            x_points.append(item["bbox"][0]) 
            z_points.append(z_dist)

            msg = "SAFE"
            dot_color = 'green'

            if z_dist < self.LIMIT_M:
                if vol > self.MIN_VOL:
                    msg = " HAZARD (Inside 1.0m limit)"
                    self.alarm_active = True
                    dot_color = 'red'
                else:
                    msg = "IGNORE (Below minimum volume size)"
                    dot_color = 'blue'
            elif z_dist <= self.ZONE_A:
                msg = "SAFE (Zone A)"
            else:
                msg = "SAFE (Zone B)"
            
            color_map.append(dot_color)
            print(f"{oid} ({name}): {z_dist}m away | STATUS: {msg}")
            time.sleep(0.2) 

        print("-" * 50)
        final_msg = " ZONE BLOCKED" if self.alarm_active else " ZONE CLEAR"
        print(f"DECISION: {final_msg}")
        
        self.generate_plot(x_points, z_points, color_map, data_feed)

    def generate_plot(self, x, z, colors, feed):
        plt.figure(figsize=(9, 6))
        plt.scatter(x, z, c=colors, s=400, alpha=0.7, edgecolors='black')
        
        for i, item in enumerate(feed):
            plt.text(x[i]+12, z[i], f"{item['label']}", fontsize=10, fontweight='bold')

        plt.axhline(y=self.LIMIT_M, color='red', linestyle='--', label='1.0m Proximity Limit')
        
        plt.title("3D Occupancy Visualization (Top-Down)")
        plt.xlabel("Horizontal Field of View (Pixels)")
        plt.ylabel("Distance from Sensor (Meters)")
        plt.ylim(0, 3) 
        plt.legend()
        plt.grid(alpha=0.3)
        plt.show()

vision_input = [
    {"id": "Obj_101", "label": "Cardboard Box", "bbox": [100, 200, 50, 50], "depth": 0.8},
    {"id": "Obj_102", "label": "Human", "bbox": [400, 150, 60, 180], "depth": 2.5},
    {"id": "Obj_103", "label": "Pallet", "bbox": [600, 500, 100, 30], "depth": 1.2},
    {"id": "Obj_104", "label": "Small Tool", "bbox": [250, 300, 10, 10], "depth": 0.5}
]

if __name__ == "__main__":
    system = WarehouseSafetyAI()
    system.process_sensor_data(vision_input)
