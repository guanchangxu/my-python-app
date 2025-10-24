
```bash
# 1. 克隆项目
git clone <your-repo-url>
cd my-python-app

# 2. 设置环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. 设置预提交钩子
pre-commit install

# 5. 运行应用
python -m app.main