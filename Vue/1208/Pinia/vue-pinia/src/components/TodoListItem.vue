<template>
    <div>
        <input type="checkbox" id="todo-txt" v-model="isDone">
        <!-- :class 는 todo.isDone의 참거짓 여부에 따라 클래스 적용 -> -->
        <label for="todo-txt" :class="{ 'is-done': todo.isDone }">{{ todo.text }}</label>
        <button @click="deleteTodo(todo.id)">삭제</button>
    </div>
</template>

<script setup>
    import { ref, watch } from 'vue'
    import { useTodoStore } from '@/stores/todo'
    const props = defineProps({
        todo: Object,
    })
    
    const store = useTodoStore()
    
    const deleteTodo = function (selectedId) {
        store.deleteTodo(selectedId)
    }

    const isDone = ref(props.todo.isDone)
    watch(isDone, () => {
        store.updateTodo(props.todo.id)
    })

</script>

<style scoped>
.is-done {
    text-decoration: line-through;
}
</style>