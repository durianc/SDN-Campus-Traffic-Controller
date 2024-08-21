from flask import Flask, render_template, g,jsonify,request
import random
import time
import numpy as np
import get_topo
import CountMinSketch
import TopK
import subprocess

app = Flask(__name__)
alert_info = []


@app.route('/')
def index():
    return render_template('index.html', alert_info=alert_info)

@app.route('/api/create-topology', methods=['POST'])
def api_create_topology():
    data = request.get_json()
    file_path = data.get('file')
    controller_ip = data.get('controller', {}).get('ip')
    controller_port = data.get('controller', {}).get('port')

    command = f"sudo mn --custom {file_path} --topo mytopo --controller=remote,ip={controller_ip},port={controller_port} --switch ovsk,protocols=OpenFlow13"
    subprocess.Popen(command, shell=True)

    return jsonify({"result": "success"})

@app.route('/api/topology', methods=['GET'])
def api_topology():
    topology = get_topo.get_topology()
    return jsonify(topology)

@app.route('/api/countmin', methods=['GET'])
def api_countmin():
    file_name = request.args.get('file')  # 获取前端传递的选项值
    file_path = f"traces/{file_name}.pcap"  # 构建文件路径
    print(f"counting {file_name}")
    result = CountMinSketch.do_CountMin(file_path)  # 调用do_CountMin函数并传递文件路径参数
    return jsonify(result)


@app.route('/api/topk', methods=['GET'])
def api_topk():
    k = int(request.args.get('k'))  # 获取前端传递的k值
    file_name = request.args.get('file')  # 获取前端传递的选项值
    file_path = f"traces/{file_name}.pcap"  # 构建文件路径
    print(f"begin to analyze {file_name}")
    result = TopK.analyze_packets(file_path, k)  # 调用analyze_packets函数并传递文件路径参数和k值
    return jsonify(result)

if __name__ == '__main__':
    # traffic = generate_traffic()
    # process_traffic(traffic)
    app.run()

