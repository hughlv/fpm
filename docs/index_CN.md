![FPM](./assets/images/logo.png)

# FPM: 资金-生产力模型

[English](./index.md)

FPM 是一个将资金与生产力相关联的模型。它是一个简单的模型，可用于理解资金与公司生产力之间的关系。该模型基于资金是生产力的关键驱动因素的观点，并且二者之间的关系不是线性的。相反，这种关系很可能是非线性的，资金的回报递减。这意味着随着资金的增加，生产力的增长最终会趋于平缓。

## 背景

FPM 是一个将资金与生产力相关联的模型。它是一个简单的模型，可用于理解资金与生产力之间的关系。该模型基于资金是生产力的关键驱动因素的观点，并且二者之间的关系不是线性的。相反，这种关系很可能是非线性的，资金的回报递减。这意味着随着资金的增加，生产力的增长最终会趋于平缓。

## 模型

FPM 基于 SEM 模型构建。SEM 模型是一种统计模型，用于估计一组观察变量与一组潜在变量之间的关系。该模型基于观察变量是由潜在变量引起的观点，并且可以使用一组结构方程来估计二者之间的关系。

## 数据标准

为了使模型工作稳定，我们需要有足够的数据，并确保数据集中包含的公司具有透明的财务状况，并在市场上享有良好的声誉。此外，数据集中的公司应来自同一行业领域，以便它们具有类似的商业模式并可进行比较。

### 选择标准

从数据可比较的角度，本次研究筛选 2010 年左右设立的企业软件和云服务。这批公司位于中国的移动互联网高速发展的时期，互联网化的进度驱动了企业软件和云服务的需求，宏观经济环境良好，市场资金充裕，政策支持力度大。除了少数坚定不融资不上市的公司外，大部分公司都在这个时期进行了多轮次大额融资，追求上市为股东回报的主要目标。

### 数据指标

因各个资本市场的巨大差异，公司的股价和当前市值无法客观反应公司的经营情况，因此本模型中不考虑股价和市值。本模型中的数据指标包括：

- 融资总额 (Total Funds): financing_amount
- 融资次数 (Number of Financing Rounds): financing_rounds
- 融资年份 (Financing Year): financing_year
- 每一轮融资金额 (Amount per Financing Round): round_financing_amount
- 每一轮融资的投资者 (Investors per Round): investors
- 每一轮融资占比 (Financing Percentage per Round): financing_percentage
- 公司员工数 (Employee Count): employee_count
- 公司成立年份 (Year of Establishment): established_year
- 公司上市年份 (Year of Listing): listed_year
- 公司营收 (Revenue at IPO): revenue_at_ipo
