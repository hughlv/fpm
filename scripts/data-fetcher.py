
# 将数据转换为DataFrame并保存到文件
df = pd.DataFrame(companies)
df.to_csv("china_enterprise_software_companies.csv", index=False)