import Vue from 'vue'
import Router from 'vue-router'
import store from '../store/store'
import Login from '@/components/login'
import Register from '@/components/register'
import RetrievePW from '@/components/retrievePW'
import LorR from '@/components/LorR'
import MainPage from '@/components/MainPage'
import Test from '@/components/Test'
import Test1 from '@/components/Test1'
import Test2 from '@/components/Test2'
import change_basic_Info from '@/components/Change_BasicInfo'
import change_pride from '@/components/Change_Pride'
import change_profile_photo from '@/components/Change_Profile_Photo'
import change_edu from '@/components/Change_Edu'
import change_job_info from '@/components/Change_Job_Info'
import change_self_desc from '@/components/Change_Self_Desc'
import show_job_info from '@/components/Show_Job_Info'
import show_pride_info from '@/components/Show_Pride_Info'
import show_school_info from '@/components/Show_School_Info'
import show_self_desc from '@/components/Show_Self_Desc'
import show_top_info from '@/components/Show_top_Info'
import show_work_info from '@/components/Show_Work_Info'
import user_info_all from '@/components/User_Info_All'
Vue.use(Router)

const routes = [
  {
    path: '/',
    redirect: '/LorR'
  },
  {
    path: '/LorR',
    name: 'LorR',
    component: LorR,
    children: [
      {
        path: '/',
        redirect: '/L'
      },
      {
        path: '/L',
        name: 'Login',
        component: Login
      },
      {
        path: '/R',
        name: 'Register',
        component: Register
      }
    ]
  },
  {
    path: '/forgetPW',
    name: 'RetrievePW',
    component: RetrievePW
  },
  {
    path: '/mainpage',
    name: 'mainpage',
    meta: {
      requireAuth: true
    },
    component: MainPage,
    children: [
      {
        path:"/user_info_all",
        name:"user_info_all",
        component:user_info_all
     },
      {
        path: '/test2',
        name: 'Test2',
        component: Test2
      }
    ]
    
  }, 
  {
    path:"/change_job_info",
    name:"change_job_info",
    component:change_job_info
  }
 

 
]

const router = new Router({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
    if (store.state.token) { // 通过vuex state获取当前的token是否存在
      next()
    } else {
      next({
        path: '/LorR',
        query: {redirect: to.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
    }
  } else {
    next()
  }
})

export default router
