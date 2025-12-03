<template>
    <div>
        <h1>Child Component</h1>
        Parent's message: {{ propsName }}
        <GrandChild :props-name="propsName" @update-name="updateName"/>
        <button @click="buttonClick('someEvent')">Emit!</button>
        <button @click="sendData">send data</button>
    </div>
</template>

<script setup>
import GrandChild from '@/components/GrandChild.vue';

defineProps({
    propsName: String
});

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function() {
    emit('someEvent')
}

const sendData = function() {
    emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
    emit('updateName')
}
</script>

<style scoped>

</style>