<template>
    <Row>
        <Row class="header" type="flex" justify="space-between" align="middle">
            <Row style="color: #fff">
                Message - Box
            </Row>
            <Row type="flex" justify="end" v-if="ifLogin">
                <Dropdown trigger="click" style="display: flex; align-items: center; margin-right: 20px; cursor: pointer">
                    <span style="color: #fff">{{ username }}<i class="el-icon-arrow-down el-icon--right"></i></span>
                    <DropdownMenu slot="dropdown">
                        <DropdownItem @click.native="toAllQuestion">全部问题</DropdownItem>
                        <DropdownItem>个人信息</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
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
    import {
        Row,
        Button,
        Dropdown,
        DropdownMenu,
        DropdownItem
    } from 'element-ui';
    export default {
        name: 'Home',
        components: {
            Row,
            Button,
            Dropdown,
            DropdownMenu,
            DropdownItem
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
            },
            toAllQuestion: function () {
                this.$router.push({ name: 'QuestionList'});
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
