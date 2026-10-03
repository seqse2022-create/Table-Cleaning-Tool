from core.cleaner import 读取数据, 清洗数据, 分组统计, 导出数据


def main():
    df = 读取数据("data.csv")
    df = 清洗数据(df)
    print(分组统计(df))
    导出数据(df, "cleaned.csv")


if __name__ == "__main__":
    main()