import pandas as pd


def 读取数据(文件路径: str) -> pd.DataFrame:
    """读取 CSV 文件"""
    return pd.read_csv(文件路径)


def 清洗数据(df: pd.DataFrame) -> pd.DataFrame:
    """去重 + 填充缺失值"""
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df


def 分组统计(df: pd.DataFrame) -> pd.Series:
    """按城市分组求分数均值"""
    return df.groupby("城市")["分数"].mean()


def 导出数据(df: pd.DataFrame, 输出路径: str) -> None:
    """导出清洗后 CSV"""
    df.to_csv(输出路径, index=False, encoding="utf-8-sig")
