<template>
    <Row class="contain">
        <PersonQuestion :person="person" @addQuestion="addQuestion" />
        <Row class="title">{{person.username}} 收到的问题：</Row>
        <Row style="position: relative;">
            <Card v-for="(item,index) in questionList" :key="item.id" class="question-content" shadow="hover" :style="{ marginLeft: ifSee && seeIndex === index ? leftWidth+'px' : '0px' }">
                <Row type="flex" justify="space-between" align="middle">
                    <Row>
                        <span class="question-time">{{item.pub_date}}</span>
                        <span class="question-title">{{ item.question_text }}</span>
                    </Row>
                    <Button type="success"
                            size="small"
                            :disabled="item.answer_text===null"
                            @click.native="item.answer_text===null?'':seeAnswer(item.answer_text,index)">
                        {{item.answer_text===null?'暂无回答':'查看回答'}}
                    </Button>
                </Row>
            </Card>
            <Card v-for="(item,index) in questionList" :key="index" class="question-content-hidden" shadow="hover" :style="{top: index*84+'px', width: ifSee && seeIndex === index ? leftWidth-20+'px' : '0px'}">
                <Row type="flex" justify="center" align="middle" class="question-title" style="height: 32px">{{ item.answer_text===null? '':item.answer_text }}</Row>
            </Card>
        </Row>
    </Row>
</template>

<script>
    import Ajax from '../utils/ajax'
    import {
        Row,
        Card,
        Button
    } from 'element-ui';
    import PersonQuestion from '../components/PersonQuestion'
    export default {
        name: "Question",
        components: {
            Row,
            Card,
            Button,
            PersonQuestion
        },
        data() {
            return {
                person: {},
                questionList: [],
                ifSee: false,
                seeIndex: 0,
                leftWidth: 400
            }
        },
        created: function () {
            // let Mock = require('mockjs');
            // let questionData = Mock.mock({
            //     'list|10':[{
            //         'id|+1':1,
            //         "question_text|+1": ["今天吃饭了吗？","作业做完了吗？"],
            //         "pub_date|+1":[Mock.mock('@datetime'),Mock.mock('@datetime'),Mock.mock('@datetime')],
            //         "answer|+1": ["吃了","做完了",""]
            //     }]
            // });
            // this.questionList = questionData.list;

            // 获取该用户信息
            this.getUserInfo(this.$route.params.userId);
            // 获取该用户下提问列表
            this.getQuestionList(this.$route.params.userId);
        },
        methods: {
            getUserInfo: function (id) {
                let data = {
                    user_id : id
                }
                Ajax.post('/messageBox/user/getUserInfo/', data).then((data)=>{
                    if(data.flag==0) {
                        this.person = data.user
                    }
                })
            },
            getQuestionList: function (id) {
                let data = {
                    user_id : id,
                    search_type: 0
                }
                Ajax.post('/messageBox/question/getQuestionList/', data).then((data)=>{
                    if(data.flag==0) {
                        this.questionList = data.questionList;
                    }
                })
            },
            addQuestion: function (question) {
                this.questionList.unshift(question)
            },
            seeAnswer: function (answer_text,index) {
                this.seeIndex = index
                this.ifSee = true
            }
        }
    }
</script>

<style scoped>
    @import "../assets/css/style.css";
    .question-content-hidden {
        position: absolute;
        left: 0;
        z-index: -99;
        border-left: 10px solid #67C23A;
    }
</style>
