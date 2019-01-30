<template>
    <Row>
        <Row class="title">{{question.question_text}}</Row>
        <Row style="margin-bottom: 10px">
            <Input type="textarea" :rows="8" placeholder="请输入回答内容" v-model="answerContent" @keyup.ctrl.enter.native="answerQuestion" style="font-size: 14px;"/>
        </Row>
        <Row type="flex" justify="end" style="margin-bottom: 40px">
            <Button size="small" @click.native="reset">重置</Button>
            <Button type="success" size="small" @click.native="answerQuestion">回答</Button>
        </Row>
    </Row>
</template>

<script>
    import Ajax from '../utils/ajax'
    import { Row, Input, Button, Message } from 'element-ui'
    export default {
        name: "AnswerQuestion",
        components: { Row, Input, Button },
        props: { question: Object },
        data() {
            return {
                answerContent: ''
            }
        },
        methods: {
            reset: function () {
                this.answerContent = '';
            },
            answerQuestion: function () {
                let data = {question_id: this.question.id, answer: this.answerContent}
                Ajax.post('/messageBox/question/AnswerQuestion/', data).then((data)=>{
                    if(data.flag == 0) {
                        Message({
                            message: '回答成功！',
                            type: 'success'
                        });
                    } else {
                        Message.error('回答失败！')
                    }
                })
            }
        }
    }
</script>

<style lang="less" scoped>
    .title{
        font-size: 25px;
        color: #67C23A;
        text-align: left;
        padding-bottom: 5px;
        border-bottom: 2px solid #67C23A;
        margin-bottom: 20px;
    }
</style>
