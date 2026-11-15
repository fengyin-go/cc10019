<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">数据埋点日志分析平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向终端埋点日志的接入清洗、事件解析、会话聚合、漏斗分析、留存计算与归因建模的数据埋点日志分析平台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "日志接入", path: "/ingest" }, { label: "事件解析", path: "/parser" }, { label: "会话聚合", path: "/session" }, { label: "漏斗分析", path: "/funnel" }, { label: "留存计算", path: "/retention" }, { label: "归因建模", path: "/attribution" }, { label: "用户画像", path: "/profile" }, { label: "人群分群", path: "/cohort" }, { label: "AB实验", path: "/abtest" }, { label: "日志清洗", path: "/cleanse" }, { label: "分析看板", path: "/dashboard" }, { label: "异常告警", path: "/alert" }, { label: "数据导出", path: "/export" }, { label: "数据源配置", path: "/source" }, { label: "指标管理", path: "/metric" }, { label: "调度管理", path: "/schedule" }, { label: "通知分发", path: "/notify" }, { label: "操作审计", path: "/audit" }]
</script>
