<template>
    <Row class="contain">
        <AnswerQuestion :question="question"/>
        <Row class="title">待回答问题</Row>
        <Card v-for="item in questionData" :key="item.id" class="question-content" shadow="hover">
            <Row type="flex" justify="space-between" align="middle">
                <Row><span class="question-time">{{item.time}}</span><span class="question-title">{{ item.title }}</span></Row>
                <Button type="success" size="small" @click.native="toAnswer(item.id)">回答</Button>
            </Row>
        </Card>
    </Row>
</template>

<script>
    import { Row, Card, Button } from 'element-ui';
    import AnswerQuestion from '../components/AnswerQuestion'
    export default {
        name: "Answer",
        components: { Row, Card, Button, AnswerQuestion },
        data() {
            return {
                id: '',
                question: {},
                answerContent: '',
                questionData: []
            }
        },
        created: function () {
            let Mock = require('mockjs');
            let questionData = Mock.mock({
                'list|10':[{
                    'id|+1':1,
                    "title|+1": ["今天吃饭了吗？","作业做完了吗？"],
                    "time|+1":[Mock.mock('@datetime'),Mock.mock('@datetime'),Mock.mock('@datetime')]
                }]
            });
            this.questionData = questionData.list;
            let id = parseInt(this.$route.params.id);
            for(let i=0; i<questionData.list.length; i++) {
                if(questionData.list[i].id === id)
                    this.question = questionData.list[i];
            }
        },
        watch: {
            $route(){
                let id = parseInt(this.$route.params.id);
                this.id = id;
                for(let i=0; i<this.questionData.length; i++) {
                    if(this.questionData[i].id === id)
                        this.question = this.questionData[i];
                }
            }
        },
        methods: {
            toAnswer: function(id) {
                this.$router.push({ name: 'Answer', params: { id: id }});
            }
        }
    }
</script>

<style lang="less" scoped>
    .contain{
        padding: 50px 100px;
    }
    .title{
        font-size: 35px;
        color: #67C23A;
        text-align: left;
        padding-bottom: 5px;
        border-bottom: 2px solid #67C23A;
        margin-bottom: 20px;
    }
    .question-content{
        margin-bottom: 10px;
    }
    .question-time{
        font-size: 12px;
        color: #666;
        margin-right: 15px;
    }
    .question-title{
        font-size: 18px;
        color: #67C23A;
    }
</style>
