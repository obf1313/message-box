<template>
    <Row>
        <Row class="title">向 {{person.username}} 提问：</Row>
        <Row style="margin-bottom: 10px">
            <Input type="textarea" :rows="8" placeholder="请输入提问内容" v-model="questionContent" style="font-size: 14px;"/>
        </Row>
        <Row type="flex" justify="end" style="margin-bottom: 40px">
            <Button size="small" @click.native="resetContent">重置</Button>
            <Button type="success" size="small" @click.native="askQuestion">提问</Button>
        </Row>
    </Row>
</template>

<script>
    import Ajax from '../utils/ajax'
    import { Row, Input, Button } from 'element-ui'
    export default {
        name: "PersonQuestion",
        components: { Row, Input, Button },
        props: { person: Object },
        data() {
            return {
                questionContent: ''
            }
        },
        methods: {
            resetContent: function () {
                this.questionContent = '';
            },
            askQuestion: function () {
                let data = {
                    user_id : this.person.id,
                    question: this.questionContent
                }
                Ajax.post('/messageBox/question/AskQuestion/', data).then((data)=>{
                    if(data.flag==0) {
                        this.$emit("addQuestion",data.question);
                        this.questionContent = '';
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .title{
        font-size: 25px;
        color: #67C23A;
        text-align: left;
        padding-bottom: 5px;
        border-bottom: 2px solid #67C23A;
        margin-bottom: 20px;
    }
</style>
