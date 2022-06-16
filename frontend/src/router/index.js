import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginPage from '../views/LoginPage'
import SignupPage from '../views/SignupPage'
import HomePage from '../views/HomePage'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    component: LoginPage,
    beforeEnter: (to, from, next) => {
      // Your are free to add whatever logic here.
      // On first visit
      next("/login")
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupPage
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
