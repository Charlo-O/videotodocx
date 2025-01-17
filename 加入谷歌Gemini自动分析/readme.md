# PDF 和 Markdown 文档分析工具

这是一个基于 Python 的桌面应用程序，用于处理和分析 PDF 文件和 Markdown 文件，并支持将它们合并成一个统一的文档。

## 功能特点

- PDF 文件处理和分析
  - 将 PDF 页面转换为图像
  - 使用 Google Gemini AI 分析图像内容
  - 支持批量处理多页 PDF
  - 实时预览处理结果

- Markdown 文件处理
  - 智能分段处理
  - 文本优化和整理
  - 自动匹配 PDF 页数进行分段

- 文档合并功能
  - PDF 和 Markdown 内容智能匹配
  - 预览合并结果
  - 导出为 Word 文档

- 其他特性
  - 多线程处理，保持界面响应
  - 错误处理和重试机制
  - 实时状态更新
  - 可视化预览界面

## 系统要求

- Python 3.6+
- 依赖库：
  - tkinter
  - PyMuPDF (fitz)
  - Pillow
  - python-docx
  - requests
  - markdown

## 安装步骤

1. 确保已安装 Python 3.6 或更高版本
2. 安装所需依赖：
```
bash
pip install PyMuPDF Pillow python-docx requests markdown
```
3. 配置 Google Gemini API：
   - 获取 API 密钥
   - 在代码中替换 `GOOGLE_API_KEY` 变量

## 使用说明

1. 启动程序：

```
bash
python pdftodocx2.py
```

2. PDF 处理流程：
   - 点击"选择 PDF 文件"按钮
   - 选择要处理的 PDF 文件
   - 等待处理完成
   - 点击"下载PDF分析"保存结果

3. Markdown 处理流程：
   - 点击"选择 MD 文件"按钮
   - 选择要处理的 Markdown 文件
   - 等待处理完成
   - 点击"下载MD分析"保存结果

4. 合并文档：
   - 确保已完成 PDF 和 MD 文件处理
   - 点击"合并预览"按钮
   - 在预览窗口查看效果
   - 点击"保存为Word文档"导出

## 主要类和方法

### PDFAnalyzer 类

- `process_pdf()`: PDF 文件处理
- `process_md()`: Markdown 文件处理
- `analyze_image()`: 图像内容分析
- `extract_images_from_pdf()`: PDF 图像提取
- `merge_pdf_md()`: 文档合并
- `calculate_similarity_with_api()`: 内容相似度计算
- `intelligently_match_content()`: 智能内容匹配

## 注意事项

1. API 使用：
   - 需要有效的 Google Gemini API 密钥
   - 注意 API 调用限制和计费

2. 文件处理：
   - 支持的 PDF 最大页数取决于系统内存
   - 建议处理清晰的 PDF 文档以获得更好的分析结果

3. 性能考虑：
   - 大文件处理可能需要较长时间
   - 保持网络连接稳定

## 错误处理

程序包含完整的错误处理机制：
- API 调用失败自动重试
- 文件处理异常捕获
- 用户友好的错误提示

## 设计思路
这段 Python 代码定义了一个名为 `PDFAnalyzer` 的类，旨在自动化分析和匹配 PDF 文档中的图像内容和 Markdown 文档中的文本内容。以下是对这段代码思路的详细分析：

**1. 核心目标与功能:**

这段代码的核心目标是将 PDF 文件中的每一页转换为图像，然后使用 Google Gemini API 分析这些图像的内容。同时，它也能处理 Markdown 文件，并使用 API 对 Markdown 内容进行优化和分段。最终，它尝试将 PDF 的图像分析结果与 Markdown 的分段内容进行智能匹配，并将匹配结果和原始数据保存到 Word 文档中。

**2. 类结构 (`PDFAnalyzer`):**

使用类来组织代码是一个良好的实践，它将数据（例如 `pdf_analysis_results`, `md_analysis_results`）和操作这些数据的方法封装在一起。`PDFAnalyzer` 类包含了所有与 PDF 和 Markdown 分析相关的逻辑。

**3. 关键模块和库:**

代码开头导入了多个必要的 Python 库，每个库都有特定的用途：

*   **`tkinter`:** 用于创建图形用户界面 (GUI)，包括窗口、按钮、文本框等，方便用户操作。
*   **`tkinter.filedialog`:** 提供打开和保存文件对话框，让用户选择 PDF 和 Markdown 文件，以及保存分析结果。
*   **`tkinter.scrolledtext`:** 创建带有滚动条的文本区域，用于显示 PDF 和 Markdown 的分析结果。
*   **`tkinter.messagebox`:** 用于显示警告和信息提示框。
*   **`fitz` (PyMuPDF):** 用于处理 PDF 文件，核心功能是将 PDF 页面转换为图像。
*   **`requests`:** 用于发送 HTTP 请求到 Google Gemini API，进行图像分析和文本相似度计算。
*   **`PIL` (Pillow):** 用于图像处理，例如显示图像在 GUI 中。
*   **`io`:** 用于处理内存中的数据流，例如在不保存到磁盘的情况下处理图像数据。
*   **`datetime`:** 用于生成时间戳，用于创建唯一的文件名。
*   **`docx`:** 用于创建和修改 Microsoft Word 文档，用于保存分析结果。
*   **`threading`:** 用于创建和管理线程，使得耗时的操作（如 PDF 处理和 API 调用）在后台运行，避免阻塞 GUI。
*   **`markdown`:** 虽然被导入，但在提供的代码片段中似乎没有直接使用。可能是为了将来扩展功能或者是一个遗留的导入。
*   **`docx.shared`:**  用于设置 Word 文档的一些属性，例如图片的大小。
*   **`base64`:** 用于将图像数据编码为 base64 字符串，以便通过 API 发送。
*   **`PIL.ImageTk`:** 用于在 `tkinter` 中显示 `PIL` 图像。
*   **`time`:** 用于添加延迟，例如在 API 调用失败时进行重试。
*   **`numpy`:** 虽然被导入，但在核心逻辑中没有直接使用。可能用于未来更复杂的图像处理或数据分析。

**4. 工作流程和方法职责:**

代码的主要功能通过不同的方法实现，以下是关键方法的职责：

*   **`__init__(self, root)`:** 构造函数，初始化 GUI 界面，设置窗口标题，创建按钮和文本区域，并初始化用于存储分析结果的列表。
*   **`process_md(self)`:**
    *   允许用户选择 Markdown 文件。
    *   读取 Markdown 文件内容。
    *   调用 Google Gemini API 对 Markdown 内容进行优化和分段，分段数量与 PDF 页数一致。
    *   将分段后的内容显示在 Markdown 文本区域。
    *   使用线程来执行 API 调用，避免阻塞 GUI。
*   **`save_md_analysis(self)`:** 将 Markdown 的分析结果（分段后的内容）保存到 Word 文档。
*   **`process_pdf(self)`:**
    *   允许用户选择 PDF 文件。
    *   调用 `extract_images_from_pdf` 将 PDF 每一页转换为图像。
    *   遍历每一张图像，调用 `analyze_image` 使用 Google Gemini API 分析图像内容。
    *   将分析结果和图像显示在 PDF 文本区域。
    *   使用线程来执行 PDF 处理和 API 调用。
*   **`analyze_image(self, image_data)`:**
    *   接收图像数据（bytes）。
    *   将图像数据编码为 base64 字符串。
    *   构建 JSON 数据，包含图像的 base64 编码和提示语，发送到 Google Gemini API。
    *   处理 API 返回的分析结果。
    *   包含重试机制，以处理可能出现的 API 调用失败。
*   **`extract_images_from_pdf(self, pdf_path)`:**
    *   使用 `fitz` 库打开 PDF 文件。
    *   遍历 PDF 的每一页。
    *   将每一页渲染成 PNG 格式的图像数据。
    *   返回一个包含每页图像数据的列表。
*   **`save_analysis(self)`:** 将 PDF 的分析结果（页码、分析文本、图像）保存到 Word 文档。
*   **`merge_pdf_md(self)`:**
    *   创建一个新的顶级窗口用于预览合并的内容。
    *   将 Markdown 的分段内容和对应的 PDF 图像显示在预览窗口中。
*   **`save_merged_document(self, preview_content)`:** 将合并预览窗口中的内容保存到 Word 文档。
*   **`calculate_similarity_with_api(self, text1, text2)`:**
    *   调用 Google Gemini API 计算两个文本的相似度，返回一个 0 到 1 的数值。
*   **`intelligently_match_content(self, similarity_threshold=0.6)`:**
    *   尝试将 PDF 的图像分析结果与 Markdown 的分段内容进行智能匹配。
    *   使用 `calculate_similarity_with_api` 计算 PDF 图像的描述和 Markdown 段落的相似度。
    *   根据设定的阈值判断是否匹配。
    *   显示匹配结果。

**5. GUI 结构:**

*   使用 `tkinter` 创建了简单的 GUI 界面。
*   包含一行按钮，分别用于选择 PDF、下载 PDF 分析结果、选择 MD 文件、下载 MD 分析结果和合并预览。
*   使用 `PanedWindow` 创建了左右两个可调整大小的文本区域，分别用于显示 PDF 和 Markdown 的处理信息。

**6. API 集成逻辑:**

*   代码使用 `requests` 库与 Google Gemini API 进行交互。
*   `GOOGLE_API_KEY` 和 `GOOGLE_API_URL` 定义了 API 的密钥和端点。
*   发送 POST 请求到 API，请求体为 JSON 格式，包含了需要分析的图像数据或文本数据，以及相关的配置参数。
*   对 API 的响应进行解析，提取分析结果。
*   在 `analyze_image` 方法中包含了错误处理和重试机制，提高了程序的健壮性。

**7. 线程的使用:**

*   `process_pdf` 和 `process_md` 方法都使用了 `threading.Thread` 来执行耗时的操作。
*   这样可以避免在处理大文件或等待 API 响应时，GUI 界面卡死，提高了用户体验。

**8. 智能匹配的思路:**

*   `intelligently_match_content` 方法是这段代码的一个亮点。它尝试通过计算 PDF 图像的描述和 Markdown 段落之间的语义相似度来实现自动匹配。
*   使用 `calculate_similarity_with_api` 方法调用 Google Gemini API 来进行相似度计算。
*   通过设置一个相似度阈值 (`similarity_threshold`) 来判断两个内容是否足够相似，从而进行匹配。

**9. 设计原则:**

*   **模块化:** 代码被组织成一个类，不同的功能被封装在不同的方法中，提高了代码的可读性和可维护性。
*   **分离关注点:** GUI 的创建和事件处理与核心的 PDF/Markdown 处理和 API 交互逻辑分离。
*   **用户友好性:** 通过 GUI 提供操作界面，使用户可以方便地选择文件和查看结果。
*   **错误处理:** 代码中包含了 `try...except` 块来处理可能出现的异常，例如文件读取错误、API 调用失败等。
*   **异步操作:** 使用线程来执行耗时操作，避免阻塞 GUI。

总的来说，这段代码的思路清晰，功能明确，通过结合 PDF 处理库、HTTP 请求库、Word 文档处理库和强大的 Google Gemini API，实现了一个自动化分析和匹配 PDF 与 Markdown 文档内容的工具。代码结构良好，并考虑了用户体验和错误处理。

