# 📡 TDMA Wireless Network Scheduler Simulation

A Python-based simulation framework modeling **Time Division Multiple Access (TDMA)** in wireless communication systems. This project evaluates dynamic time-slot allocation, throughput efficiency, collision avoidance, and transmission latency across multiple sensor/transceiver nodes.

---

## 🚀 Key Features

- **Slot Allocation Logic:** Deterministic and dynamic time-slot scheduling algorithms for multi-node wireless links.
- **Performance Metrics:** Measures packet throughput, end-to-end latency, and channel efficiency under varying traffic loads.
- **Collision-Free Transmission:** Demonstrates conflict-free scheduling over shared communication mediums.
- **Modular Architecture:** Structured for easy integration with wireless sensor network (WSN) parameters and IoT testbeds.

---

## 🛠️ Tech Stack & Prerequisites

- **Language:** Python 3.x
- **Libraries:** NumPy, Matplotlib

---

## 📂 Project Architecture

```
├── scheduler.py         # Core TDMA slot allocation logic & simulation engine
├── nodes.py             # Transceiver / node traffic generation profiles
├── plot_results.py      # Throughput and latency visualization scripts
└── README.md            # Project overview and run instructions
```

---

## 💻 Installation & Execution

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Malathi014/tdma-wireless-scheduler.git](https://github.com/Malathi014/tdma-wireless-scheduler.git)
   cd tdma-wireless-scheduler
   ```

2. **Install Required Packages:**
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the Scheduler Simulation:**
   ```bash
   python scheduler.py
   ```

---

## 📊 Analytical Scope

Designed for core electronics and telecommunication studies, demonstrating Medium Access Control (MAC) sublayer dynamics in distributed embedded and IoT networks.
