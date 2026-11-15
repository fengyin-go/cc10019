"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import ingest as router_ingest
from app.routers import parser as router_parser
from app.routers import session as router_session
from app.routers import funnel as router_funnel
from app.routers import retention as router_retention
from app.routers import attribution as router_attribution
from app.routers import profile as router_profile
from app.routers import cohort as router_cohort
from app.routers import abtest as router_abtest
from app.routers import cleanse as router_cleanse
from app.routers import dashboard as router_dashboard
from app.routers import alert as router_alert
from app.routers import export as router_export
from app.routers import source as router_source
from app.routers import metric as router_metric
from app.routers import schedule as router_schedule
from app.routers import notify as router_notify
from app.routers import audit as router_audit

ROUTERS = [router_ingest, router_parser, router_session, router_funnel, router_retention, router_attribution, router_profile, router_cohort, router_abtest, router_cleanse, router_dashboard, router_alert, router_export, router_source, router_metric, router_schedule, router_notify, router_audit]
