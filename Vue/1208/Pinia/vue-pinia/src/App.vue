<template>
  <div>
    <h1>Todo Project</h1>
    <div>
      <h2>완료된 Todo의 개수: {{ store.doneTodoCount }}</h2>
      <TodoList />
      <TodoForm />
    </div>
  </div>
</template>

<script setup>
  // 연습 
  // 1번
  // import { useCounterStore } from '@/stores/counter'
  // 2번 store 라는 객체 반환받기
  // const store = useCounterStore()

  import TodoForm from '@/components/TodoForm.vue'
  import TodoList from '@/components/TodoList.vue'
  import { useTodoStore } from '@/stores/todo'

  const store = useTodoStore()

</script>

<style scoped>

</style>