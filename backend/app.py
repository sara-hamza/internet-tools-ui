import requests
import socket
import subprocess
import json
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

def run_speed_test():
    try:
        response = requests.get("https://api.fast.com/netflix/speedtest?https=true", timeout=10)
        data = response.json()
        download_speed = data["downloadSpeed"] / 1_000_000
        upload_speed = data["uploadSpeed"] / 1_000_000
        ping = data["latency"]
        
        return {
            "Download Speed (Mbps)": round(download_speed, 2),
            "Upload Speed (Mbps)": round(upload_speed, 2),
            "Ping (ms)": round(ping, 2)
        }
    except Exception as e:
        return {"error": f"Speed test failed: {str(e)}"}

@app.route("/isp-performance", methods=["GET"])
def isp_performance_report():
    speed_results = run_speed_test()
    return jsonify(speed_results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

