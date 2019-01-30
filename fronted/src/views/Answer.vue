<template>
    <Row class="contain">
        <AnswerQuestion :question="question"/>
        <Row class="title">全部问题</Row>
        <Row type="flex">
            <Input placeholder="请输入问题..."  prefix-icon="el-icon-search" v-model="keyword" style="width: 250px; margin-right: 10px;" @keyup.native.enter="searchQuestion" />
        </Row>
        <Card v-for="item in questionList" :key="item.id" class="question-content" shadow="hover">
            <Row type="flex" justify="space-between" align="middle">
                <Row><span class="question-time">{{item.pub_date}}</span><span class="question-title">{{ item.question_text }}</span></Row>
                <Button type="success" size="small" @click.native="toAnswer(item.id)">回答</Button>
            </Row>
        </Card>
    </Row>
</template>

<script>
    import Ajax from '../utils/ajax'
    import { Row, Card, Button, Input } from 'element-ui';
    import AnswerQuestion from '../components/AnswerQuestion'
    export default {
        name: "Answer",
        components: { Row, Card, Button, AnswerQuestion, Input },
        data() {
            return {
                questionId: '',
                userId: '',
                question: {},
                questionList: [],
                keyword: ''
            }
        },
        created: function () {
            // let Mock = require('mockjs');
            // let questionData = Mock.mock({
            //     'list|10':[{
            //         'id|+1':1,
            //         "title|+1": ["今天吃饭了吗？","作业做完了吗？"],
            //         "time|+1":[Mock.mock('@datetime'),Mock.mock('@datetime'),Mock.mock('@datetime')],
            //         "answer|+1": ["吃了","做完了",""]
            //     }]
            // });
            // this.questionList = questionData.list;
            // for(let i=0; i<questionData.list.length; i++) {
            //     if(questionData.list[i].id === questionId)
            //         this.question = questionData.list[i];
            // }

            this.questionId = this.$route.params.questionId;
            this.userId = sessionStorage.getItem('userid');
            // 获取问题列表
            this.getQuestionList(this.userId, this.questionId);
        },
        watch: {
            $route(){
                let questionId = this.$route.params.questionId;
                this.questionId = questionId;
                for(let i=0; i<this.questionList.length; i++) {
                    if(this.questionList[i].id === questionId)
                        this.question = this.questionList[i];
                }
            }
        },
        methods: {
            toAnswer: function(questionId) {
                this.$router.push({ name: 'Answer', params: { questionId: questionId }});
            },
            getQuestionList: function (userId, questionId) {
                let data = {
                    user_id : userId,
                    search_type: 1
                };
                Ajax.post('/messageBox/question/getQuestionList/', data).then((data)=>{
                    if(data.flag == 0) {
                        this.questionList = data.questionList;
                        for(let i=0; i<data.questionList.length; i++) {
                            if(data.questionList[i].id === questionId)
                                this.question = data.questionList[i];
                        }
                    }
                })
            },
            searchQuestion:function () {
                let questionId = this.questionId;
                let data = {
                    user_id : this.userId,
                    keyword: this.keyword,
                    search_type: 3
                };
                Ajax.post('/messageBox/question/getQuestionList/', data).then((data)=>{
                    if(data.flag == 0) {
                        this.questionList = data.questionList;
                        for(let i=0; i<data.questionList.length; i++) {
                            if(data.questionList[i].id === questionId)
                                this.question = data.questionList[i];
                        }
                    }
                })
            }
        }
    }
</script>

<style lang="less" scoped>
    @import "../assets/css/style.css";
</style>
