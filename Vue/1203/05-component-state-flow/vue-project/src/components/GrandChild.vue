<template>
    <div>
        <h1>GrandChild Component</h1>
        GrandParent's message: {{ propsName }}
        <button @click="updateName">GrandChild update name</button>
    </div>
</template>

<script setup>
defineProps({
    propsName: String
});

const emit = defineEmits(['updateName'])

const updateName = function() {
    emit('updateName')
}
</script>

<style scoped>

</style>