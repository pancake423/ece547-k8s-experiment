import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import subprocess
from datetime import datetime

plt.ion()  # turning interactive mode on

timestamps = []
replicas = []
avg_cpu = []

# returns a dict of HPA data
def collect_hpa_data():
    result = subprocess.run(
        ["sudo", "kubectl", "get", "hpa"],
        capture_output = True, # Python >= 3.7 only
        text = True # Python >= 3.7 only
    )
    data = {}
    lines = result.stdout.split("\n")
    word_start = 0
    for i, char in enumerate(lines[0]):
        if char == " " and (i + 1 >= len(lines[0]) or lines[0][i+1] != " "):
            # last character of a column
            key = lines[0][word_start:i+1].strip()
            value = lines[1][word_start:i+1].strip()
            data[key] = value
            word_start = i+1

    return data

# add current values of timestamp, replicas, metric
def collect():
    data = collect_hpa_data()
    timestamps.append(datetime.now().strftime("%H:%M:%S"))
    replicas.append(int(data["REPLICAS"]))
    try:
        avg_cpu.append(int(data["TARGETS"].split(":")[1].split("%")[0]))
    except:
        avg_cpu.append(0)



fig, ax = plt.subplots(2, 1)
plt.tight_layout()

# the update loop
while(True):
    # update the data
    collect()

    # clear old plots
    for axis in ax:
        plt.sca(axis)
        plt.cla()

    ax[0].set_title("Number of Replicas")
    ax[1].set_title("CPU Utilization")
    ax[1].set_ylabel("average pct utilization")

    # plot new data
    ax[0].plot(timestamps, replicas,color = 'b')
    ax[1].plot(timestamps, avg_cpu, color = 'r')
    ax[1].plot([timestamps[0], timestamps[-1]], [70, 70], color = 'g', linestyle="dashed")

    ax[0].xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax[1].xaxis.set_major_locator(MaxNLocator(nbins=10))

    plt.pause(5)
