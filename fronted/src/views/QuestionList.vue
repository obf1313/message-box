<template>
    <Row class="contain">
        <Row class="title">待回答问题</Row>
        <Row type="flex">
            <Input v-model="keyword"
                   placeholder="请输入问题..."
                   prefix-icon="el-icon-search"
                   style="width: 250px; margin-right: 10px;"
                   @keyup.native.enter="searchQuestion" />
        </Row>
        <Row style="position: relative;">
            <Card v-for="(item,index) in questionList" :key="item.id" class="question-content" shadow="hover" :style="{ marginLeft: ifSee && seeIndex === index ? leftWidth+'px' : '0px' }">
                <Row type="flex" justify="space-between" align="middle">
                    <Row>
                        <span class="question-time">{{item.pub_date}}</span>
                        <span class="question-title">{{ item.question_text }}</span>
                    </Row>
                    <Button type="success"
                            size="small"
                            :disabled="item.answer===null"
                            @click.native="item.answer_text===null?toAnswer(item.id):seeAnswer(item.answer_text,index)"
                            style="width: 80px">
                        {{ item.answer_text===null?'回答':'查看回答' }}
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
        Button,
        Input,
        Card
    } from 'element-ui'

    export default {
        name: "QuestionList",
        components: {
            Row,
            Button,
            Input,
            Card
        },
        data() {
            return {
                questionList: [],
                keyword: '',
                ifSee: false,
                seeIndex: 1,
                leftWidth: 400
            }
        },
        created() {
            let userId = sessionStorage.getItem('userid')
            // 获取问题列表
            this.getQuestionList(userId)
        },
        methods: {
            getQuestionList: function (userId) {
                let data = {
                    user_id : userId,
                    search_type: 0
                }
                Ajax.post('/messageBox/question/getQuestionList/', data).then((data)=>{
                    if(data.flag == 0) {
                        this.questionList = data.questionList;
                    }
                })
            },
            toAnswer: function(questionId) {
                this.$router.push({ name: 'Answer', params: { questionId: questionId }});
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
