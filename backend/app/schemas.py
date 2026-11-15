"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class IngestEntry(BaseModel):
    """接入配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 日志来源
    field_2: str | None = None  # 传输协议
    field_3: str | None = None  # 数据格式
    field_4: str | None = None  # 分隔符
    field_5: str | None = None  # 字符编码
    field_6: str | None = None  # 批量大小
    field_7: str | None = None  # 接收端口

class ParserEntry(BaseModel):
    """解析规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 事件类型
    field_2: str | None = None  # 字段映射
    field_3: str | None = None  # 类型转换
    field_4: str | None = None  # 校验表达式
    field_5: str | None = None  # 默认填充
    field_6: str | None = None  # 事件版本
    field_7: str | None = None  # 解析优先级

class SessionEntry(BaseModel):
    """会话规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 用户标识
    field_2: str | None = None  # 会话超时分钟
    field_3: str | None = None  # 跨天切分
    field_4: str | None = None  # 跨设备合并
    field_5: str | None = None  # 最小事件数
    field_6: str | None = None  # 归因窗口
    field_7: str | None = None  # 输出粒度

class FunnelEntry(BaseModel):
    """漏斗定义明细结构。"""

    field_0: str | None = None  # 漏斗编号
    field_1: str | None = None  # 漏斗名称
    field_2: str | None = None  # 步骤序列
    field_3: str | None = None  # 步骤事件
    field_4: str | None = None  # 转化窗口小时
    field_5: str | None = None  # 严格顺序
    field_6: str | None = None  # 最大间隔秒
    field_7: str | None = None  # 漏斗版本

class RetentionEntry(BaseModel):
    """留存配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 初始事件
    field_2: str | None = None  # 回访事件
    field_3: str | None = None  # 留存窗口天
    field_4: str | None = None  # 分群维度
    field_5: str | None = None  # 基数口径
    field_6: str | None = None  # 去重策略
    field_7: str | None = None  # 输出周期

class AttributionEntry(BaseModel):
    """归因规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 归因模型
    field_2: str | None = None  # 转化事件
    field_3: str | None = None  # 触点事件
    field_4: str | None = None  # 回溯窗口天
    field_5: str | None = None  # 衰减系数
    field_6: str | None = None  # 首次末次
    field_7: str | None = None  # 权重配置

class ProfileEntry(BaseModel):
    """画像标签明细结构。"""

    field_0: str | None = None  # 标签编号
    field_1: str | None = None  # 标签名称
    field_2: str | None = None  # 计算规则
    field_3: str | None = None  # 数据来源
    field_4: str | None = None  # 更新频率
    field_5: str | None = None  # 标签层级
    field_6: str | None = None  # 值域定义
    field_7: str | None = None  # 失效天数

class CohortEntry(BaseModel):
    """分群定义明细结构。"""

    field_0: str | None = None  # 分群编号
    field_1: str | None = None  # 分群名称
    field_2: str | None = None  # 筛选条件
    field_3: str | None = None  # 基准日期
    field_4: str | None = None  # 分群大小
    field_5: str | None = None  # 刷新频率
    field_6: str | None = None  # 标签绑定
    field_7: str | None = None  # 分群版本

class AbtestEntry(BaseModel):
    """实验方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 实验名称
    field_2: str | None = None  # 分流比例
    field_3: str | None = None  # 实验组配置
    field_4: str | None = None  # 对照组配置
    field_5: str | None = None  # 核心指标
    field_6: str | None = None  # 最小样本
    field_7: str | None = None  # 置信水平

class CleanseEntry(BaseModel):
    """清洗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 空值策略
    field_3: str | None = None  # 格式校验
    field_4: str | None = None  # 异常剔除
    field_5: str | None = None  # 去重键
    field_6: str | None = None  # 规则版本
    field_7: str | None = None  # 生效日期

class DashboardEntry(BaseModel):
    """看板配置明细结构。"""

    field_0: str | None = None  # 看板编号
    field_1: str | None = None  # 看板名称
    field_2: str | None = None  # 关联指标
    field_3: str | None = None  # 图表类型
    field_4: str | None = None  # 刷新间隔秒
    field_5: str | None = None  # 布局模板
    field_6: str | None = None  # 可见范围
    field_7: str | None = None  # 分享有效期

class AlertEntry(BaseModel):
    """告警规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 监控指标
    field_2: str | None = None  # 告警阈值
    field_3: str | None = None  # 持续触发
    field_4: str | None = None  # 告警级别
    field_5: str | None = None  # 静默分钟
    field_6: str | None = None  # 通知渠道
    field_7: str | None = None  # 升级策略

class ExportEntry(BaseModel):
    """导出任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 导出范围
    field_2: str | None = None  # 导出格式
    field_3: str | None = None  # 字段列表
    field_4: str | None = None  # 分隔符
    field_5: str | None = None  # 编码类型
    field_6: str | None = None  # 压缩方式
    field_7: str | None = None  # 目标路径

class SourceEntry(BaseModel):
    """源端连接明细结构。"""

    field_0: str | None = None  # 连接编号
    field_1: str | None = None  # 连接类型
    field_2: str | None = None  # 接入地址
    field_3: str | None = None  # 认证方式
    field_4: str | None = None  # 连接池
    field_5: str | None = None  # 超时秒
    field_6: str | None = None  # 重试上限
    field_7: str | None = None  # 负责人

class MetricEntry(BaseModel):
    """指标口径明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 指标名称
    field_2: str | None = None  # 计算公式
    field_3: str | None = None  # 统计粒度
    field_4: str | None = None  # 时间范围
    field_5: str | None = None  # 筛选条件
    field_6: str | None = None  # 精度位数
    field_7: str | None = None  # 口径版本

class ScheduleEntry(BaseModel):
    """调度计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 调度表达式
    field_3: str | None = None  # 时区
    field_4: str | None = None  # 最大并发
    field_5: str | None = None  # 超时终止
    field_6: str | None = None  # 依赖检查
    field_7: str | None = None  # 通知策略

class NotifyEntry(BaseModel):
    """通知规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 触发事件
    field_2: str | None = None  # 通知渠道
    field_3: str | None = None  # 接收列表
    field_4: str | None = None  # 消息模板
    field_5: str | None = None  # 合并窗口
    field_6: str | None = None  # 重复抑制
    field_7: str | None = None  # 优先级

class AuditEntry(BaseModel):
    """审计日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 操作类型
    field_2: str | None = None  # 操作对象
    field_3: str | None = None  # 操作详情
    field_4: str | None = None  # 操作来源
    field_5: str | None = None  # 执行时间
    field_6: str | None = None  # 影响范围
    field_7: str | None = None  # 回滚能力
