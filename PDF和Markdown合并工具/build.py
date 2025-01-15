import PyInstaller.__main__
import os
import sys

# 增加递归限制
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# 构建参数列表
args = [
    os.path.join(current_dir, 'pdf4.py'),  # 使用完整路径指向主程序文件
    '--name=PDF和Markdown合并工具',  # 生成的exe名称
    '--windowed',  # 使用GUI模式
    '--onefile',  # 打包成单个文件
    '--distpath=' + parent_dir,  # 输出到上级目录
    '--workpath=' + os.path.join(parent_dir, 'build'),  # 指定工作目录
    '--specpath=' + parent_dir,  # 指定spec文件目录
    '--clean',  # 添加清理选项
    '--debug=all',  # 添加调试信息
]

# 如果图标文件存在，则添加图标参数
icon_path = os.path.join(current_dir, 'pdf.ico')
if os.path.exists(icon_path):
    args.append('--icon=' + icon_path)

# 打印当前工作目录和参数
print(f"当前工作目录: {os.getcwd()}")
print(f"脚本目录: {current_dir}")
print(f"父目录: {parent_dir}")
print(f"主程序路径: {os.path.join(current_dir, 'pdf4.py')}")
print(f"参数列表: {args}")

# 确保主程序文件存在
if not os.path.exists(os.path.join(current_dir, 'pdf4.py')):
    print("错误：找不到 pdf4.py 文件！")
    sys.exit(1)

try:
    # 运行 PyInstaller
    PyInstaller.__main__.run(args)
    print("打包完成！")
except Exception as e:
    print(f"打包过程中出现错误：{str(e)}") 