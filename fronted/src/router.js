import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Login from './views/Login'
import Register from './views/Register'
import Answer from './views/Answer'
import Question from './views/Question'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/home'
        },
        {
            path: '/home',
            name: 'home',
            component: Home,
            children: [{
                path: 'Answer/:id',
                name: 'Answer',
                component: Answer
            },{
                path: 'Question/:userId',
                name: 'Question',
                component: Question
            }]
        },
        {
            path: '/Login',
            name: 'Login',
            component: Login
        },
        {
            path: '/Register',
            name: 'Register',
            component: Register
        }
  ]
})
