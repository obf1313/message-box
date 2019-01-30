import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Login from './views/Login'
import Register from './views/Register'
import Answer from './views/Answer'
import Question from './views/Question'
import QuestionList from './views/QuestionList'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            redirect: '/Login'
        },
        {
            path: '/home',
            name: 'home',
            component: Home,
            children: [{
                path: 'Answer/:questionId',
                name: 'Answer',
                component: Answer
            },{
                path: 'Question/:userId',
                name: 'Question',
                component: Question
            },{
                path: 'QuestionList',
                name: 'QuestionList',
                component: QuestionList
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
