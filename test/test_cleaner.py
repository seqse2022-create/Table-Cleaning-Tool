import pandas as pd
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core.cleaner import 清洗数据, 分组统计


def test_清洗数据去重():
    """测试去重功能"""
    df = pd.DataFrame({"姓名": ["张三", "张三", "李四"], "分数": [90, 90, 85]})
    结果 = 清洗数据(df)
    assert len(结果) == 2


def test_清洗数据填充缺失值():
    """测试缺失值填充"""
    df = pd.DataFrame({"姓名": ["张三", "李四"], "分数": [90, None]})
    结果 = 清洗数据(df)
    assert 结果["分数"].isna().sum() == 0


def test_分组统计():
    """测试分组统计"""
    df = pd.DataFrame({"城市": ["惠州", "惠州", "广州"], "分数": [90, 80, 85]})
    结果 = 分组统计(df)
    assert 结果["惠州"] == 85.0
    assert 结果["广州"] == 85.0
