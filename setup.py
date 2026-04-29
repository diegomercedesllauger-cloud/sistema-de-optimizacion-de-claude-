```bash
cat > setup.py << 'EOF'
from setuptools import setup, find_packages

setup(
    name="sistema-agentes-diego",
    version="1.0.0",
    description="Sistema multiagente optimizado para Claude",
    author="Diego Mercedes Llauger (2026-0048)",
    author_email="diego@universidad.edu",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28",
        "pydantic>=1.9",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
EOF
```
