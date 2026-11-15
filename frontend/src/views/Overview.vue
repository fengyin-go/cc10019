<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "日志接入", "created": 0, "pending": 0, "abnormal": 0}, {"name": "事件解析", "created": 0, "pending": 0, "abnormal": 0}, {"name": "会话聚合", "created": 0, "pending": 0, "abnormal": 0}, {"name": "漏斗分析", "created": 0, "pending": 0, "abnormal": 0}, {"name": "留存计算", "created": 0, "pending": 0, "abnormal": 0}, {"name": "归因建模", "created": 0, "pending": 0, "abnormal": 0}, {"name": "用户画像", "created": 0, "pending": 0, "abnormal": 0}, {"name": "人群分群", "created": 0, "pending": 0, "abnormal": 0}, {"name": "AB实验", "created": 0, "pending": 0, "abnormal": 0}, {"name": "日志清洗", "created": 0, "pending": 0, "abnormal": 0}, {"name": "分析看板", "created": 0, "pending": 0, "abnormal": 0}, {"name": "异常告警", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据导出", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据源配置", "created": 0, "pending": 0, "abnormal": 0}, {"name": "指标管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "调度管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "通知分发", "created": 0, "pending": 0, "abnormal": 0}, {"name": "操作审计", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
