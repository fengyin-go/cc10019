# 数据埋点日志分析平台

面向终端埋点日志的接入清洗、事件解析、会话聚合、漏斗分析、留存计算与归因建模的数据埋点日志分析平台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 日志接入 | `ingest` | 接入配置 | 配置编号、日志来源、传输协议 |
| 事件解析 | `parser` | 解析规则 | 规则编号、事件类型、字段映射 |
| 会话聚合 | `session` | 会话规则 | 规则编号、用户标识、会话超时分钟 |
| 漏斗分析 | `funnel` | 漏斗定义 | 漏斗编号、漏斗名称、步骤序列 |
| 留存计算 | `retention` | 留存配置 | 配置编号、初始事件、回访事件 |
| 归因建模 | `attribution` | 归因规则 | 规则编号、归因模型、转化事件 |
| 用户画像 | `profile` | 画像标签 | 标签编号、标签名称、计算规则 |
| 人群分群 | `cohort` | 分群定义 | 分群编号、分群名称、筛选条件 |
| AB实验 | `abtest` | 实验方案 | 方案编号、实验名称、分流比例 |
| 日志清洗 | `cleanse` | 清洗规则 | 规则编号、目标字段、空值策略 |
| 分析看板 | `dashboard` | 看板配置 | 看板编号、看板名称、关联指标 |
| 异常告警 | `alert` | 告警规则 | 规则编号、监控指标、告警阈值 |
| 数据导出 | `export` | 导出任务 | 任务编号、导出范围、导出格式 |
| 数据源配置 | `source` | 源端连接 | 连接编号、连接类型、接入地址 |
| 指标管理 | `metric` | 指标口径 | 指标编号、指标名称、计算公式 |
| 调度管理 | `schedule` | 调度计划 | 计划编号、关联任务、调度表达式 |
| 通知分发 | `notify` | 通知规则 | 规则编号、触发事件、通知渠道 |
| 操作审计 | `audit` | 审计日志 | 日志编号、操作类型、操作对象 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数据分析与数据应用
