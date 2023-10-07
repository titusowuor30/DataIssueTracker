import routes from '@/router/routes'
import store from '@/store'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !store.state.auth.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
