import { createRouter, createWebHistory } from 'vue-router'

import Overview from '@/views/Overview.vue'
const Ingest = () => import('@/views/ingest/index.vue')
const Parser = () => import('@/views/parser/index.vue')
const Session = () => import('@/views/session/index.vue')
const Funnel = () => import('@/views/funnel/index.vue')
const Retention = () => import('@/views/retention/index.vue')
const Attribution = () => import('@/views/attribution/index.vue')
const Profile = () => import('@/views/profile/index.vue')
const Cohort = () => import('@/views/cohort/index.vue')
const Abtest = () => import('@/views/abtest/index.vue')
const Cleanse = () => import('@/views/cleanse/index.vue')
const Dashboard = () => import('@/views/dashboard/index.vue')
const Alert = () => import('@/views/alert/index.vue')
const Export = () => import('@/views/export/index.vue')
const Source = () => import('@/views/source/index.vue')
const Metric = () => import('@/views/metric/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Notify = () => import('@/views/notify/index.vue')
const Audit = () => import('@/views/audit/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'overview', component: Overview },
    { path: '/ingest', name: 'ingest', component: Ingest },
    { path: '/parser', name: 'parser', component: Parser },
    { path: '/session', name: 'session', component: Session },
    { path: '/funnel', name: 'funnel', component: Funnel },
    { path: '/retention', name: 'retention', component: Retention },
    { path: '/attribution', name: 'attribution', component: Attribution },
    { path: '/profile', name: 'profile', component: Profile },
    { path: '/cohort', name: 'cohort', component: Cohort },
    { path: '/abtest', name: 'abtest', component: Abtest },
    { path: '/cleanse', name: 'cleanse', component: Cleanse },
    { path: '/dashboard', name: 'dashboard', component: Dashboard },
    { path: '/alert', name: 'alert', component: Alert },
    { path: '/export', name: 'export', component: Export },
    { path: '/source', name: 'source', component: Source },
    { path: '/metric', name: 'metric', component: Metric },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/notify', name: 'notify', component: Notify },
    { path: '/audit', name: 'audit', component: Audit },
  ],
})

export default router
