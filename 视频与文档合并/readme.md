# videotodocx - 视频文本分析工具

videotodocx 是一款功能强大的桌面应用程序，结合了视频分析和文本处理功能，利用人工智能技术在视频内容和 Markdown 文档之间建立有意义的连接。

## 主要功能

### 视频分析
- 使用场景检测和运动分析自动提取关键帧
- AI 驱动的图像内容分析
- 提取帧的可视化预览和描述
- 支持 MP4 视频格式

### Markdown 文档处理
- Markdown 文档的语义分析
- 基于视频关键帧的智能文本分段
- 关键词提取和内容优化
- 上下文感知的文本组织

### 集成功能
- 将视频帧与相应的 Markdown 段落合并
- 保存前的内容预览
- 导出为 Word 文档（.docx）
- 多线程处理以提升性能

## 系统要求

- Python 3.x
- 必需的 Python 包：
  - tkinter
  - requests
  - Pillow
  - python-docx
  - markdown
  - moviepy
  - opencv-python
  - numpy
  - scikit-learn

## 安装说明

1. 克隆仓库
2. 安装所需包：
```
bash
pip install -r requirements.txt
```
## 配置说明

使用前需要进行以下配置：
1. 获取 Google AI API 密钥（Gemini 2.0 Flash）
2. 在代码中更新 `GOOGLE_API_KEY` 变量

## 使用说明

1. 启动应用程序：
```bash
python vtod4.py
```

2. 基本工作流程：
   - 点击"选择视频文件"处理视频文件
   - 点击"选择 MD 文件"分析 Markdown 文档
   - 使用"合并预览"查看组合结果
   - 使用下载按钮保存分析结果

### 详细操作步骤

1. 视频处理：
   - 选择视频文件后，程序会自动分析视频内容
   - 提取关键帧并进行 AI 分析
   - 可以预览分析结果和关键帧图像
   - 可以将分析结果保存为 Word 文档

2. Markdown 处理：
   - 选择 Markdown 文件后，程序会进行语义分析
   - 自动分段并提取关键词
   - 可以预览优化后的文本内容
   - 可以将分析结果保存为 Word 文档

3. 合并功能：
   - 可以将视频分析和文本分析结果合并
   - 提供合并预览功能
   - 可以调整内容布局
   - 导出为完整的分析报告

## 输出格式

工具可以生成以下类型的输出：
- 视频分析报告（.docx）
- Markdown 分析文档（.docx）
- 视频文本组合分析文档（.docx）

## 注意事项

1. 性能考虑：
   - 处理大型视频文件可能需要较长时间
   - 建议使用高质量的网络连接以确保 AI API 调用稳定
   - 建议预留足够的系统内存

2. 文件格式：
   - 视频仅支持 MP4 格式
   - Markdown 文件需要使用 UTF-8 编码
   - 导出文档使用 .docx 格式
## 技术详解

### 核心技术架构

1. 视频处理模块
   - 使用 OpenCV (cv2) 进行视频帧提取和场景检测
   - 采用帧差法和光流法进行运动检测
   - 使用 K-means 聚类算法优化关键帧选择
   - 基于 moviepy 实现视频时间轴控制

2. AI 分析模块
   - 集成 Google Gemini 2.0 Flash API
   - 支持图像内容理解和语义分析
   - 实现多重重试机制和错误处理
   - 异步处理避免 UI 阻塞

3. 文本处理模块
   - Markdown 文档语义分析
   - 基于 AI 的文本分段和关键词提取
   - 智能文本优化和重组
   - 上下文关联分析

### 关键算法说明

1. 场景检测算法
```
python
def scene_detection(prev_frame, current_frame):
# 帧差法检测场景变化
diff = cv2.absdiff(prev_frame, current_frame)
mean_diff = np2.mean(diff)
return mean_diff > THRESHOLD # 阈值判断
```

2. 运动检测算法

```
python
def motion_detection(prev_frame, current_frame):
# 光流法检测运动
flow = cv2.calcOpticalFlowFarneback(
prev_frame, current_frame,
None, 0.5, 3, 15, 3, 5, 1.2, 0
)
magnitude = np2.sqrt(flow[..., 0]2 + flow[..., 1]2)
return np2.mean(magnitude) > MOTION_THRESHOLD
```

3. 关键帧优化
```
python:readme.md
def optimize_keyframes(keypoints):
# K-means 聚类优化关键帧选择
kmeans = KMeans(n_clusters=8)
points_array = np2.array(keypoints).reshape(-1, 1)
kmeans.fit(points_array)
return sorted(kmeans.cluster_centers_.flatten().tolist())
```

### 系统架构设计

1. 多线程处理
   - 使用 threading 模块实现并行处理
   - 主线程负责 UI 交互
   - 工作线程处理耗时操作
   - 线程间通信使用队列和事件

2. UI 设计
   - 基于 tkinter 构建界面
   - 使用 PanedWindow 实现分屏显示
   - ScrolledText 支持长文本展示
   - 动态图像加载和显示

3. 数据流设计
```
readme.md
视频输入 -> 帧提取 -> 场景分析 -> AI处理 -> 结果存储
↓
文本输入 -> 语义分析 -> 分段处理 -> 关键词提取
↓
合并处理 -> 预览生成 -> 文档导出
```
### 性能优化策略

1. 视频处理优化
   - 采用跳帧处理减少计算量
   - 图像缓存机制避免重复处理
   - 自适应分辨率调整

2. API 调用优化
   - 请求队列管理
   - 失败重试机制
   - 结果缓存
   - 并发请求控制

3. 内存管理
   - 大文件分块处理
   - 及时释放无用资源
   - 图像压缩和缓存清理

### 扩展性设计

1. 模块化结构
   - 核心功能模块独立封装
   - 统一的接口定义
   - 插件式架构支持

2. 配置管理
   - 外部配置文件支持
   - 运行时参数调整
   - 多环境配置

3. API 适配
   - 支持多种 AI 服务提供商
   - 统一的 API 封装层
   - 便捷的服务切换机制

## 常见问题

1. API 调用失败：
   - 检查网络连接
   - 验证 API 密钥是否正确
   - 确认 API 调用限额

2. 程序运行缓慢：
   - 检查系统资源使用情况
   - 考虑减小视频文件大小
   - 确保系统满足最低配置要求

## 技术支持

如果遇到问题或需要帮助，请：
- 提交 Issue
- 查看项目文档
- 联系开发团队

## 许可证

[添加许可证信息]

## 贡献指南

[添加贡献指南]

## 更新日志

### v1.0.0
- 初始版本发布
- 实现基本的视频分析功能
- 实现基本的 Markdown 处理功能
- 添加合并预览功能