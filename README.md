# README

## Project Overview
The Campus SDN Network Management Platform is designed to address the issue of unstable network speeds in campus environments by utilizing the capabilities of Software-Defined Networking (SDN). This platform offers a comprehensive solution for network management, measurement, and analysis, enhancing both network performance and user experience.

## Key Features
- **Network Performance Optimization**: Manage and optimize the campus network topology and traffic control through SDN's global control.
- **Flexible Network Management**: Benefit from the programmability and flexibility of the SDN architecture to make real-time adjustments to the network structure.
- **Network Fault Diagnosis**: Leverage SDN's global control and visualization to quickly locate and resolve network faults.
- **Traffic Measurement and Analysis**: Employ open-source controllers for traffic measurement and analysis, providing data support for network optimization.
- **Improved User Experience**: Enhance the campus network experience for faculty and students to facilitate smooth teaching and learning processes.

## Design Approach
The platform is designed with a focus on creating a virtual network topology, traffic detection, and analysis modules, including:
- **Topology Creation Module**: Construct a virtual network based on a given topology structure.
- **Topology Retrieval Module**: Provide a complete view of the created topology, showing the connection relationships and detailed information.
- **Traffic Detection Module**: Utilize tools like Scapy to generate data packets and apply the Count-Min Sketch algorithm for traffic statistics.
- **Traffic Analysis Module**: Display the top k traffic flows based on user input.

## REST API Interface Design
The platform features a set of RESTful APIs for various operations:
- **Create Topology API**: `POST /api/create-topology`
- **Retrieve Topology API**: `GET /api/topology`
- **Count-Min Sketch Algorithm API**: `GET /api/countmin`
- **Top-k Traffic Analysis API**: `GET /api/topk`

## Innovations and Unique Features
- **Multi-threading**: Improve processing speed and reduce waiting time with a thread pool executor.
- **Real-time Topology Retrieval**: Offer network administrators an intuitive view of the network's structure and status.
- **Intelligent Topology Construction**: Simplify the construction of network topologies with intelligent virtual network building.

---

# 项目说明

## 项目概述
校园SDN网络管理平台旨在通过利用软件定义网络（SDN）的能力，解决校园环境中网络速度不稳定的问题。该平台为网络管理、测量和分析提供了全面的解决方案，增强了网络性能和用户体验。

## 主要功能
- **网络性能优化**：通过SDN的全局控制管理和优化校园网络拓扑和流量控制。
- **灵活的网络管理**：利用SDN架构的可编程性和灵活性，对网络结构进行实时调整。
- **网络故障诊断**：利用SDN的全局控制和可视化快速定位和解决网络故障。
- **流量测量与分析**：使用开源控制器进行流量测量和分析，为网络优化提供数据支持。
- **改善用户体验**：增强师生在校园网络上的体验，促进教学和学习的顺利进行。

## 设计方法
平台专注于创建虚拟网络拓扑、流量检测和分析模块，包括：
- **拓扑创建模块**：根据给定的拓扑结构构建虚拟网络。
- **拓扑获取模块**：提供已创建拓扑的完整视图，显示连接关系和详细信息。
- **流量检测模块**：使用Scapy等工具生成数据包，并应用Count-Min Sketch算法进行流量统计。
- **流量分析模块**：根据用户输入显示前k条流量。

## REST API 接口设计
平台具有一组RESTful API，用于各种操作：
- **创建拓扑API**：`POST /api/create-topology`
- **获取拓扑API**：`GET /api/topology`
- **Count-Min Sketch算法API**：`GET /api/countmin`
- **Top-k流量分析API**：`GET /api/topk`

## 创新与特色
- **多线程**：使用线程池执行器提高处理速度，减少等待时间。
- **实时拓扑获取**：为网络管理员提供网络结构和状态的直观视图。
- **智能拓扑构建**：通过智能虚拟网络构建简化网络拓扑的构建。
