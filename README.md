# Humanoid-robot-simulation-using-ai-agent-for-MATLAB-and-MuJoCo-collaboration
After analyzing the kinematic parameters through MATLAB, the performance parameters of the humanoid robot are then analyzed based on the physical coupling simulation of Mujoco.

This project integrates AI into MuJoCo-based humanoid simulation.

- Simulation: MuJoCo + MATLAB
- AI Module: Motion analysis and optimization suggestion
- Goal: Build an AI-assisted simulation-to-deployment pipeline

# claude需要遵守的协议
## 1. 环境保护与防污染 (核心原则)
- **严禁全局安装**：禁止使用 `npm install -g` 或任何会修改系统全局环境变量的命令。
- **Conda 优先**：所有 Python 依赖必须在当前的 Conda 环境内安装，禁止使用系统的 Python 路径。
- **禁止删除系统文件**
- **禁止修改注册表**：严禁执行任何涉及 Windows 注册表修改或系统文件夹 (`C:\Windows`, `C:\Program Files`) 的操作。
- **静默运行**：在安装库之前，先用 `pip list` 或 `conda list` 检查，已有的库严禁重复安装。
## 2. 授权操作空间 (给 Claude 的“绿灯”)
- **项目内操作**：你可以自由创建、修改和删除**当前项目文件夹**内的任何文件。
- **虚拟环境维护**：如果代码运行报错缺少依赖，你被授权在**当前激活的 Conda 环境**内使用 `pip install` 安装必要的 Python 库。
- **临时文件**：如需产生缓存或临时数据，请统一存放于项目根目录下的 `./temp/`  文件夹内。
- **Shell 指令**：允许使用 PowerShell 执行文件操作、运行仿真脚本（如 MuJoCo 或 MATLAB 脚本）。
## 3. 机器人科研特定规范
- **路径处理**：在 Windows 下路径请优先使用双反斜杠 `\\` 或原始字符串 `r'...'`，避免转义错误。
- **仿真保护**：修改 `URDF` 或 `XML` 模型文件前，必须先创建 `.bak` 备份。
## 4. 报错处理流程
1. 遇到权限错误 (Access Denied)，**严禁**尝试提权，应立即停止并向用户报告。
2. 遇到环境冲突，优先尝试在当前 Conda 环境内解决，而不是寻找系统级替代方案。
