import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../views/HomePage.vue')
    },
    {
      path: '/about',
      component: () => import('../views/AboutPage.vue')
    },
    {
      path: '/contact',
      component: () => import('../views/ContactPage.vue')
    },
    {
      path: '/login',
      component: () => import('../views/LoginPage.vue')
    },
    {
      path: '/register',
      component: () => import('../views/RegisterPage.vue')
    },
	{
		path: '/persons',
		component: () => import('../views/PersonsPage.vue')
	},
	{
		path: '/positions',
		component: () => import('../views/PositionsPage.vue')
	},

	// This route will match any path that hasn't matched any of the routes above
    {
      path: '/:catchAll(.*)',
      component: () => import('../views/NotFoundPage.vue')
	},
  ]
})

export default router
