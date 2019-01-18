<template>
    <Row>
        <Row class="title">{{question.title}}</Row>
        <Row style="margin-bottom: 10px">
            <Input type="textarea" :rows="8" placeholder="请输入内容" v-model="answerContent" style="font-size: 14px;"/>
        </Row>
        <Row type="flex" justify="end" style="margin-bottom: 40px">
            <Button size="small">重置</Button>
            <Button type="success" size="small">回答</Button>
        </Row>
    </Row>
</template>

<script>
    import { Row, Input, Button } from 'element-ui'
    export default {
        name: "AnswerQuestion",
        components: { Row, Input, Button },
        props: { question: Object },
        data() {
            return {
                answerContent: ''
            }
        }
    }
</script>

<style lang="less" scoped>
    .title{
        font-size: 35px;
        color: #67C23A;
        text-align: left;
        padding-bottom: 5px;
        border-bottom: 2px solid #67C23A;
        margin-bottom: 20px;
    }
</style>
