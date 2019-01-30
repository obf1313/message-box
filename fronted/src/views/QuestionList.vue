<template>
    <Row class="contain">
        <Row class="title">待回答问题</Row>
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
    import { Row, Button, Input, Card } from 'element-ui'

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
                keyword: ''
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
                    search_type: 1
                }
                Ajax.post('/messageBox/question/getQuestionList/', data).then((data)=>{
                    if(data.flag == 0) {
                        this.questionList = data.questionList;
                    }
                })
            },
            toAnswer: function(questionId) {
                this.$router.push({ name: 'Answer', params: { questionId: questionId }});
            }
        }
    }
</script>

<style scoped>

</style>
