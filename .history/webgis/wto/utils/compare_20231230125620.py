import pandas as pd
import sys
#比较之前的country和现在新引入的差距
#比较国家和合作伙伴之间的关系

# 添加项目根目录到 Python 路径
project_root = 'f:\\zyy_wto\\webgis'
if project_root not in sys.path:
    sys.path.append(project_root)

# 读取 Excel 文件
df = pd.read_excel('F:/zyy_wto/data/Commercai.xlsx')
df.fillna(0, inplace=True)  # 将所有的 nan 值替换为 0