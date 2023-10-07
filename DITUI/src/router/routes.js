const routes= [
  { path: '/', redirect: '/dashboard' },
  {
    path: '/',
    component: () => import('@/layouts/default.vue'),
    children: [
      {
        path: 'dashboard',
        component: () => import('@/pages/dashboard.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'account-settings',
        name: 'account-settings',
        component: () => import('@/pages/account/account-settings.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'data-issues',
        name: 'dataQuality',
        component: () => import('@/pages/data/dataQuality.vue'),
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: '/',
    component: () => import('@/layouts/blank.vue'),
    children: [
      {
        path: 'login',
        component: () => import('@/pages/account/login.vue'),
      },
      {
        path: 'register',
        component: () => import('@/pages/account/register.vue'),
      },
      {
        path: '/:pathMatch(.*)*',
        component: () => import('@/pages/[...all].vue'),
      },
    ],
  },
]

export default routes
