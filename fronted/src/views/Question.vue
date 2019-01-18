<template>
    <Row class="contain">
        <PersonQuestion :person="person" />
        <Row class="title">{{person.name}} 收到的问题：</Row>
        <Card v-for="item in questionData" :key="item.id" class="question-content" shadow="hover">
            <Row type="flex" justify="space-between" align="middle">
                <Row><span class="question-time">{{item.time}}</span><span class="question-title">{{ item.title }}</span></Row>
                <Button type="success" size="small" :disabled="item.answer===''" >{{item.answer===''?'暂无回答':'查看回答'}}</Button>
            </Row>
        </Card>
    </Row>
</template>

<script>
    import { Row, Card, Button } from 'element-ui';
    import PersonQuestion from '../components/PersonQuestion'
    export default {
        name: "Question",
        components: { Row, Card, Button, PersonQuestion },
        data() {
            return {
                person: {
                    id: 1,
                    name: '小朋友'
                },
                questionData: []
            }
        },
        created: function () {
            let Mock = require('mockjs');
            let questionData = Mock.mock({
                'list|10':[{
                    'id|+1':1,
                    "title|+1": ["今天吃饭了吗？","作业做完了吗？"],
                    "time|+1":[Mock.mock('@datetime'),Mock.mock('@datetime'),Mock.mock('@datetime')],
                    "answer|+1": ["吃了","做完了",""]
                }]
            });
            this.questionData = questionData.list;
        }
    }
</script>

<style scoped>
    @import "../assets/css/style.css";
</style>
