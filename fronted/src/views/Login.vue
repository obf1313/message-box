<template>
    <Row>
        <Row class="header" type="flex" justify="end">
            <router-link :to="{ name: 'Register'}"><Button type="text" style="color: #fff">注册</Button></router-link>
        </Row>
        <Row type="flex" justify="center" style="margin-top: 200px;">
            <Row style="width: 300px;">
                <Row class="login_title">登录</Row>
                <Input placeholder="请输入用户名" v-model="userName" clearable />
                <Input placeholder="请输入密码" v-model="passWord" clearable />
                <Button type="success" style="width: 100%">登陆</Button>
            </Row>
        </Row>
    </Row>
</template>

<script>
    import { Button, Row, Input} from 'element-ui'
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
        }
    }
</script>

<style lang="less" scoped>
    @import "../assets/css/login.css";
</style>
