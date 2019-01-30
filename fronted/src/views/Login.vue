<template>
    <Row>
        <Row class="header" type="flex" justify="end">
            <router-link :to="{ name: 'Register'}"><Button type="text" style="color: #fff">注册</Button></router-link>
        </Row>
        <Row type="flex" justify="center" style="margin-top: 200px;">
            <Row style="width: 300px;">
                <Row class="login_title">登录</Row>
                <Input placeholder="请输入用户名" v-model="userName" clearable />
                <Input placeholder="请输入密码" v-model="passWord" type="password" clearable />
                <Button type="success" style="width: 100%" @click.native="login">登录</Button>
            </Row>
        </Row>
    </Row>
</template>

<script>
    import Ajax from '../utils/ajax'
    import { Button, Row, Input, Message} from 'element-ui'
    export default {
        name: "Login",
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
            login: function() {
                let data = {
                    username: this.userName,
                    password: this.passWord
                };
                Ajax.post('/messageBox/user/login/', data).then((data)=>{
                    if(data.flag == 0) {
                        Message({
                            message: '登录成功!',
                            type: 'success'
                        });
                        sessionStorage.setItem('username',data.user.username);
                        sessionStorage.setItem('userid',data.user.id);
                        this.$router.push({ name: 'QuestionList'});
                    } else {
                        Message.error(data.msg);
                    }
                });
            }
        }
    }
</script>

<style lang="less" scoped>
    @import "../assets/css/login.css";
</style>
