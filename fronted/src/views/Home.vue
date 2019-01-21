<template>
    <Row>
        <Row class="header" type="flex" justify="space-between" align="middle">
            <Row style="color: #fff">
                Message - Box
            </Row>
            <Row type="flex" justify="end" v-if="ifLogin">
                <Button type="text" style="color: #fff; margin-right: 20px">{{ username }}</Button>
                <Button type="text" style="color: #fff" @click.native="exitLogin">退出登录</Button>
            </Row>
            <Row type="flex" justify="end" v-else>
                <router-link :to="{ name: 'Login'}"><Button type="text" style="color: #fff; margin-right: 20px">登录</Button></router-link>
                <router-link :to="{ name: 'Register'}"><Button type="text" style="color: #fff">注册</Button></router-link>
            </Row>
        </Row>
        <Row>
            <router-view/>
        </Row>
    </Row>
</template>

<script>
    import { Row, Button } from 'element-ui';
    export default {
        name: 'Home',
        components: {
            Row,
            Button
        },
        data() {
          return {
              ifLogin: false,
              username: ''
          }
        },
        mounted() {
            let username = sessionStorage.getItem('username');
            if(username) {
                this.ifLogin = true;
                this.username = username;
            }
        },
        methods: {
            exitLogin: function() {
                sessionStorage.clear();
                this.$router.push({ name: 'Login', params: {}});
            }
        }
    }
</script>

<style lang="less" scoped>
    .header{
        width: 100%;
        padding: 10px 20px;
        background-color: #67C23A;
    }
</style>
