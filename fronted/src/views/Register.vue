<template>
    <Row>
        <Row class="header" type="flex" justify="end">
            <router-link :to="{ name: 'Login'}"><Button type="text" style="color: #fff">登录</Button></router-link>
        </Row>
        <Row type="flex" justify="center" style="margin-top: 200px;">
            <Row style="width: 300px;">
                <Row class="login_title">注册</Row>
                <Input placeholder="请输入用户名" v-model="userName" clearable />
                <Input type="password" placeholder="请输入密码" v-model="passWord" clearable />
                <Button type="success" style="width: 100%" @click.native="register">注册</Button>
            </Row>
        </Row>
    </Row>
</template>

<script>
    import {
        Button,
        Row,
        Input
    } from 'element-ui'
    import Ajax from '../utils/ajax'
    export default {
        name: "Register",
        mounted: ()=>{
        },
        data() {
            return {
                userName: '',
                passWord: ''
            }
        },
        components: {
            Button,
            Row,
            Input
        },
        methods: {
            register: function() {
                let data = {
                    username: this.userName,
                    password: this.passWord
                };
                Ajax.post('/messageBox/user/register/', data).then((response)=>{
                    if(response.flag==0) {
                        sessionStorage.setItem('username',this.userName);
                        sessionStorage.setItem('userid',response.id);
                        this.$router.push({ name: 'QuestionList'});
                    }
                });
            }
        }
    }
</script>

<style lang="less" scoped>
    @import "../assets/css/login.css";
</style>
