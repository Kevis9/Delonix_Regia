<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <h2>我是测试页面1号</h2>
    </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    data () {
        return {
            msg: '欢迎进入vue的世界'
        }
    }
}
</script>

<style scoped>
h1, h2 {
    font-weight: normal;
    color: #42b983;
}
</style>