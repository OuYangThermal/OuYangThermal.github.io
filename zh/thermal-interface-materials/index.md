---
title: "导热界面材料怎么选？Pad、Gel、Grease与Insulator选型逻辑"
description: "从热阻、接触热阻、BLT、压缩、硬度、电气绝缘和可靠性选择导热界面材料，而不是只比较导热系数。"
permalink: /zh/thermal-interface-materials/
lang: zh-CN
alternate_en: /china-thermal-interface-material-supplier/
---

<div class="quick"><strong>直接回答</strong><p>导热界面材料（TIM）的选择顺序应是：先定义热源、冷端、间隙和装配方式，再确认是否需要电气绝缘，最后比较安装状态下的总热阻与可靠性。Pad、Gel、Grease和Insulator没有绝对优劣；真正决定结果的是压缩后的厚度、接触热阻、表面平整度、压力、工艺稳定性和老化后的界面状态。</p></div>

## TIM为什么不能只看W/m·K

导热系数 `k` 是材料属性，热阻 `R` 是具体热路径的结果。均匀材料层可用 `R = t/(kA)` 做初步估算，其中`t`为厚度、`A`为接触面积。但实际装配还存在材料两侧的接触热阻、局部空洞、压力不均和热扩散。

因此，8 W/m·K的厚垫片不一定优于更薄、更贴合的较低导热系数材料。供应商数据只有在测试方法、厚度、压力、温度和样品方向一致时才适合横向比较。

## Pad、Gel、Grease、Insulator怎么判断

| 材料 | 更适合的界面 | 主要风险 | 验证重点 |
| --- | --- | --- | --- |
| 导热垫片 Pad | 有明确间隙、需要预成型装配 | 压力过大、接触不足、压缩永久变形 | 公差栈、压缩后BLT、硬度方法、模切尺寸 |
| 导热凝胶 Gel | 器件高度变化大、希望降低装配应力 | 空洞、塌陷、泵出、挤出和固化异常 | 点胶质量、轨迹、混合比例、装配与循环后位置 |
| 导热脂 Grease | 平整、受控的薄界面 | 泵出、干化、污染和涂布不一致 | 薄BLT、涂布量、压力、温度循环与返修 |
| 导热绝缘材料 Insulator | 热路径同时承担电气隔离 | 边缘、孔位、污染或老化破坏绝缘 | 完整绝缘系统、厚度、安装压力和老化后电气测试 |

## 九个必须定义的参数

1. 最小、标称和最大间隙；
2. 接触面积与热源位置；
3. 允许温升或热阻预算；
4. 可接受的器件、PCB或壳体受力；
5. 压缩后的实际BLT；
6. 是否承担电气绝缘功能；
7. 贴装、点胶、固化、检测与返修方式；
8. 工作温度、循环、振动、湿度和污染环境；
9. 多批次一致性与供应商变更通知。

## 不同应用的选型侧重点

- **光模块：** 关注局部接触、壳体平整度、压缩力与DSP/光引擎机械风险。
- **AI服务器：** GPU、VRM、SSD和电源磁性器件的间隙、面积与装配条件不同，不能统一指定一种TIM。
- **IGBT / SiC：** 先确定绝缘位于模块内部还是外部界面，再平衡热阻和电气安全。
- **OBC / DC-DC / PCS：** 功率器件、磁性器件和PCB热路径通常需要分别选材。
- **储能：** 关注大面积间隙、公差、液冷板平整度、点胶节拍和循环可靠性。

## 建议的验证流程

先冻结图纸、装配和验收标准；再用同一夹具、压力、表面和温度对比现有材料与候选材料。样品通过不等于量产资格，还要检查可靠性、多批次、包装、工艺窗口、Pilot Build和变更管理。

继续阅读：[导热垫片]({{ '/zh/thermal-pad/' | relative_url }}) · [导热凝胶]({{ '/zh/thermal-gel/' | relative_url }}) · [IGBT / SiC导热绝缘]({{ '/zh/igbt-sic/' | relative_url }}) · [中文工程资源]({{ '/zh/engineering-resources/' | relative_url }})

英文深度页：[China TIM Supplier Evaluation]({{ '/china-thermal-interface-material-supplier/' | relative_url }})

需要评估实际界面时，可[Benchmark现有TIM]({{ '/benchmark-your-current-tim/' | relative_url }})或[联系Owen Ouyang（欧阳小辉）]({{ '/discuss-your-application/' | relative_url }})。

